from typing import List, Optional, Union

from deepeval.metrics import BaseMetric
from deepeval.metrics.indicator import metric_progress_indicator
from deepeval.metrics.utils import initialize_model, trimAndLoadJson, check_llm_test_case_params, construct_verbose_logs
from deepeval.models import DeepEvalBaseLLM
from deepeval.test_case import LLMTestCaseParams, LLMTestCase, ConversationalTestCase
from deepeval.utils import get_or_create_event_loop

from custom_metrics.grice_maxims.schema import Reason
from custom_metrics.grice_maxims.template import GriceMaximsTemplate

required_params: List[LLMTestCaseParams] = [
    LLMTestCaseParams.INPUT,
    LLMTestCaseParams.ACTUAL_OUTPUT,
]


class GriceMaximsMetric(BaseMetric):
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
                quantity_score, quality_score, relation_score, manner_score, reason = self._a_generate_reason(test_case.input, test_case.actual_output)
                self.reason = reason
                total_score = float(quantity_score) + float(quality_score) + float(relation_score) + float(manner_score)
                self.score = total_score
                self.score = (
                    0
                    if self.strict_mode and self.score < self.threshold
                    else self.score
                )
                self.success = self.score >= self.threshold
                self.verbose_logs = construct_verbose_logs(
                    self,
                    steps=[
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
            self,
            async_mode=True,
            _show_indicator=_show_indicator,
        ):
            quantity_score, quality_score, relation_score, manner_score, reason = await self._a_generate_reason(test_case.input, test_case.actual_output)
            self.reason = reason
            total_score = float(quantity_score) + float(quality_score) + float(relation_score) + float(manner_score)
            print(quantity_score, quality_score, relation_score, manner_score)
            self.score = total_score
            self.score = (
                0
                if self.strict_mode and self.score < self.threshold
                else self.score
            )
            self.success = self.score >= self.threshold
            self.verbose_logs = construct_verbose_logs(
                self,
                steps=[
                    f"Score: {self.score}\nReason: {self.reason}",
                ],
            )

            return self.score

    async def _a_generate_reason(self, input: str, actual_output: str) -> str:
        if self.include_reason is False:
            return None

        prompt = GriceMaximsTemplate.generate_reason(
            input=input,
            actual_output=actual_output,
        )
        if self.using_native_model:
            res, cost = await self.model.a_generate(prompt)
            self.evaluation_cost += cost
            data = trimAndLoadJson(res, self)
            return data["quantity_score"], data["quality_score"], data["relation_score"], data["manner_score"], data["reason"]
        else:
            try:
                res: Reason = await self.model.a_generate(
                    prompt=prompt, schema=Reason
                )
                return res.reason
            except TypeError:
                res = await self.model.a_generate(prompt)
                data = trimAndLoadJson(res, self)
                return data["quantity_score"], data["quality_score"], data["relation_score"], data["manner_score"], data["reason"]

    def _generate_reason(self, input: str, actual_output: str) -> str:
        if self.include_reason is False:
            return None

        prompt = GriceMaximsTemplate.generate_reason(
            input=input,
            actual_output=actual_output,
        )

        if self.using_native_model:
            res, cost = self.model.generate(prompt)
            self.evaluation_cost += cost
            data = trimAndLoadJson(res, self)
            return data["quantity_score"], data["quality_score"], data["relation_score"], data["manner_score"], data["reason"]
        else:
            try:
                res: Reason = self.model.generate(prompt=prompt, schema=Reason)
                return res.reason
            except TypeError:
                res = self.model.generate(prompt)
                data = trimAndLoadJson(res, self)
                return data["quantity_score"], data["quality_score"], data["relation_score"], data["manner_score"], data["reason"]
