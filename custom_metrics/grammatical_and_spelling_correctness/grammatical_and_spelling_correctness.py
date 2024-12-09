from typing import Optional, Union, List

from deepeval.metrics import BaseMetric
from deepeval.metrics.indicator import metric_progress_indicator
from deepeval.metrics.utils import initialize_model, check_llm_test_case_params, construct_verbose_logs, trimAndLoadJson
from deepeval.models import DeepEvalBaseLLM
from deepeval.test_case import LLMTestCase, ConversationalTestCase, LLMTestCaseParams
from deepeval.utils import get_or_create_event_loop, prettify_list

from custom_metrics.grammatical_and_spelling_correctness.schema import GrammaticalAndSpellingCorrectnessVerdict, Reason, \
    Verdicts, ErroneousText
from custom_metrics.grammatical_and_spelling_correctness.template import GrammaticalAndSpellingCorrectnessTemplate

required_params: List[LLMTestCaseParams] = [
    LLMTestCaseParams.INPUT,
    LLMTestCaseParams.ACTUAL_OUTPUT,
]


class GrammaticalAndSpellingCorrectnessMetric(BaseMetric):
    def __init__(
        self,
        threshold: float = 0.5,
        model: Optional[Union[str, DeepEvalBaseLLM]] = None,
        include_reason: bool = True,
        async_mode: bool = True,
        strict_mode: bool = False,
        verbose_mode: bool = False,
    ):
        self.threshold = 1 if strict_mode else threshold
        self.model, self.using_native_model = initialize_model(model)
        self.evaluation_model = self.model.get_model_name()
        self.include_reason = include_reason
        self.async_mode = async_mode
        self.strict_mode = strict_mode
        self.verbose_mode = verbose_mode

    def measure(
        self,
        test_case: Union[LLMTestCase, ConversationalTestCase],
        _show_indicator: bool = True,
    ) -> float:
        if isinstance(test_case, ConversationalTestCase):
            test_case = test_case.turns[0]
        check_llm_test_case_params(test_case, required_params, self)

        self.evaluation_cost = 0 if self.using_native_model else None
        with metric_progress_indicator(self, _show_indicator=_show_indicator):
            if self.async_mode:
                loop = get_or_create_event_loop()
                loop.run_until_complete(
                    self.a_measure(test_case, _show_indicator=False)
                )
            else:
                self.erroneous_text: List[str] = self._generate_erroneous(
                    test_case.actual_output
                )
                self.verdicts: List[GrammaticalAndSpellingCorrectnessVerdict] = (
                    self._generate_verdicts(test_case.actual_output)
                )
                self.score = self._calculate_score(test_case.actual_output)
                self.reason = self._generate_reason(test_case.input)
                self.success = self.score >= self.threshold
                self.verbose_logs = construct_verbose_logs(
                    self,
                    steps=[
                        f"ErroneousText:\n{prettify_list(self.erroneous_text)}",
                        f"Verdicts:\n{prettify_list(self.verdicts)}",
                        f"Score: {self.score}\nReason: {self.reason}",
                    ],
                )

                return self.score

    async def a_measure(
        self,
        test_case: Union[LLMTestCase, ConversationalTestCase],
        _show_indicator: bool = True,
    ) -> float:
        if isinstance(test_case, ConversationalTestCase):
            test_case = test_case.turns[0]
        check_llm_test_case_params(test_case, required_params, self)

        self.evaluation_cost = 0 if self.using_native_model else None
        with metric_progress_indicator(
            self, async_mode=True, _show_indicator=_show_indicator
        ):
            self.erroneous_text: List[str] = await self._a_generate_erroneous(
                test_case.actual_output
            )
            self.verdicts: List[GrammaticalAndSpellingCorrectnessVerdict] = (
                await self._a_generate_verdicts(test_case.actual_output)
            )
            self.score = self._calculate_score(test_case.actual_output)
            self.reason = await self._a_generate_reason(test_case.input)
            self.success = self.score >= self.threshold
            self.verbose_logs = construct_verbose_logs(
                self,
                steps=[
                    f"ErroneousText:\n{prettify_list(self.erroneous_text)}",
                    f"Verdicts:\n{prettify_list(self.verdicts)}",
                    f"Score: {self.score}\nReason: {self.reason}",
                ],
            )

            return self.score

    async def _a_generate_reason(self, input: str) -> str:
        if self.include_reason is False:
            return None

        erroneous_text_pieces = []
        for verdict in self.verdicts:
            if verdict.verdict.strip().lower() == "yes":
                erroneous_text_pieces.append(verdict.reason)

        prompt = GrammaticalAndSpellingCorrectnessTemplate.generate_reason(
            erroneous_text_pieces=erroneous_text_pieces,
            input=input,
            score=format(self.score, ".2f"),
        )
        if self.using_native_model:
            res, cost = await self.model.a_generate(prompt)
            self.evaluation_cost += cost
            data = trimAndLoadJson(res, self)
            return data["reason"]
        else:
            try:
                res: Reason = await self.model.a_generate(
                    prompt=prompt, schema=Reason
                )
                return res.reason
            except TypeError:
                res = await self.model.a_generate(prompt)
                data = trimAndLoadJson(res, self)
                return data["reason"]

    def _generate_reason(self, input: str) -> str:
        if self.include_reason is False:
            return None

        erroneous_text_pieces = []
        for verdict in self.verdicts:
            if verdict.verdict.strip().lower() == "yes":
                erroneous_text_pieces.append(verdict.reason)

        prompt = GrammaticalAndSpellingCorrectnessTemplate.generate_reason(
            erroneous_text_pieces=erroneous_text_pieces,
            input=input,
            score=format(self.score, ".2f"),
        )

        if self.using_native_model:
            res, cost = self.model.generate(prompt)
            self.evaluation_cost += cost
            data = trimAndLoadJson(res, self)
            return data["reason"]
        else:
            try:
                res: Reason = self.model.generate(prompt=prompt, schema=Reason)
                return res.reason
            except TypeError:
                res = self.model.generate(prompt)
                data = trimAndLoadJson(res, self)
                return data["reason"]

    async def _a_generate_verdicts(self, actual_output: str) -> List[GrammaticalAndSpellingCorrectnessVerdict]:
        if len(self.erroneous_text) == 0:
            return []

        prompt = GrammaticalAndSpellingCorrectnessTemplate.generate_verdicts(
            actual_output=actual_output,
            erroneous_text_pieces=self.erroneous_text,
        )
        if self.using_native_model:
            res, cost = await self.model.a_generate(prompt)
            self.evaluation_cost += cost
            data = trimAndLoadJson(res, self)
            return [GrammaticalAndSpellingCorrectnessVerdict(**item) for item in data["verdicts"]]
        else:
            try:
                res: Verdicts = await self.model.a_generate(
                    prompt, schema=Verdicts
                )
                return [item for item in res.verdicts]
            except TypeError:
                res = await self.model.a_generate(prompt)
                data = trimAndLoadJson(res, self)
                return [
                    GrammaticalAndSpellingCorrectnessVerdict(**item) for item in data["verdicts"]
                ]

    def _generate_verdicts(self, actual_output: str) -> List[GrammaticalAndSpellingCorrectnessVerdict]:
        if len(self.erroneous_text) == 0:
            return []

        prompt = GrammaticalAndSpellingCorrectnessTemplate.generate_verdicts(
            actual_output=actual_output,
            erroneous_text_pieces=self.erroneous_text,
        )
        if self.using_native_model:
            res, cost = self.model.generate(prompt)
            self.evaluation_cost += cost
            data = trimAndLoadJson(res, self)
            return [GrammaticalAndSpellingCorrectnessVerdict(**item) for item in data["verdicts"]]
        else:
            try:
                res: Verdicts = self.model.generate(prompt, schema=Verdicts)
                return [item for item in res.verdicts]
            except TypeError:
                res = self.model.generate(prompt)
                data = trimAndLoadJson(res, self)
                return [
                    GrammaticalAndSpellingCorrectnessVerdict(**item) for item in data["verdicts"]
                ]

    async def _a_generate_erroneous(
        self,
        actual_output: str,
    ) -> List[str]:
        prompt = GrammaticalAndSpellingCorrectnessTemplate.generate_erroneous(
            actual_output=actual_output,
        )
        if self.using_native_model:
            res, cost = await self.model.a_generate(prompt)
            self.evaluation_cost += cost
            data = trimAndLoadJson(res, self)
            return data["erroneous_text"]
        else:
            try:
                res: ErroneousText = await self.model.a_generate(
                    prompt, schema=ErroneousText
                )
                return res.erroneous_text
            except TypeError:
                res = await self.model.a_generate(prompt)
                data = trimAndLoadJson(res, self)
                return data["erroneous_text"]

    def _generate_erroneous(
        self,
        actual_output: str,
    ) -> List[str]:
        prompt = GrammaticalAndSpellingCorrectnessTemplate.generate_erroneous(
            actual_output=actual_output,
        )
        if self.using_native_model:
            res, cost = self.model.generate(prompt)
            self.evaluation_cost += cost
            data = trimAndLoadJson(res, self)
            return data["erroneous_text"]
        else:
            try:
                res: ErroneousText = self.model.generate(prompt, schema=ErroneousText)
                return res.erroneous_text
            except TypeError:
                res = self.model.generate(prompt)
                data = trimAndLoadJson(res, self)
                return data["erroneous_text"]

    def _calculate_score(self, actual_output):
        number_of_verdicts = len(self.verdicts)
        if number_of_verdicts == 0:
            return 1
        else:
            score = 1 - number_of_verdicts / len(actual_output.split())
            return 0 if self.strict_mode and score < self.threshold else score

    def is_successful(self) -> bool:
        if self.error is not None:
            self.success = False
        else:
            try:
                self.success = self.score >= self.threshold
            except:
                self.success = False
        return self.success

    @property
    def __name__(self):
        return "Grammatical and Spelling Correctness"
