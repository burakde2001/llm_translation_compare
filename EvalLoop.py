import mauve
import pyperclip
import asyncio

from deepeval.metrics import HallucinationMetric, GEval, AnswerRelevancyMetric, BiasMetric, SummarizationMetric
from deepeval.test_case import LLMTestCaseParams, LLMTestCase
from dotenv import load_dotenv
from mauve.utils import featurize_tokens_from_model
from transformers import AutoTokenizer, AutoModel

from custom_metrics.grammatical_and_spelling_correctness.grammatical_and_spelling_correctness import \
    GrammaticalAndSpellingCorrectnessMetric
from custom_metrics.grice_maxims.grice_maxims import GriceMaximsMetric

load_dotenv()

#Dafür gedacht, um menschlichen Referenztext p nicht bei jedem Durchlauf zu wiederholen, falls p immer gleich ist. Basiert auf compute_mauve.py, ist aber verkürzt und vereinfacht.
async def featurize_text(texts):
    tokenizer = AutoTokenizer.from_pretrained("gpt2-large") # Default model
    model = AutoModel.from_pretrained("gpt2-large")
    texts = [sen for sen in texts if len(sen) > 0]  # Remove empty strings.
    tokenized_texts = [
        tokenizer.encode(sen, return_tensors='pt', truncation=True, max_length=1024)
        for sen in texts
    ]
    features = featurize_tokens_from_model(model, tokenized_texts, batch_size=1, name="p").detach().cpu().numpy()
    return features


class EvalLoop:

    correctness_metric = GEval(
                name="correctness",
                criteria="Determine whether the actual output is correct.",
                evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
                model="gpt-4o"
            )
    hallucination_metric = HallucinationMetric(threshold=0.5, model="gpt-4o")
    answer_relevancy_metric = AnswerRelevancyMetric(
        threshold=0.5,
        include_reason=True,
        model="gpt-4o"
    )
    bias_metric = BiasMetric(threshold=0.5, model="gpt-4o")
    summarization_metric = SummarizationMetric(threshold=0.5, model="gpt-4o")
    grammatical_and_spelling_correctness_metric = GrammaticalAndSpellingCorrectnessMetric(threshold=0.5, model="gpt-4o")
    grice_maxims_metric = GriceMaximsMetric(threshold=0.5, model="gpt-4o")

    def __init__(self, eval_set, metric, context):
        self.eval_set = eval_set
        self.metric = metric
        self.context = context
        self.worker_metric = None


    async def eval_by_metric(self, metric, test_case):
        if metric == "correctness":
            self.worker_metric = self.correctness_metric
        elif metric == "hallucination":
            self.worker_metric = self.hallucination_metric
        elif metric == "answer relevancy":
            self.worker_metric = self.answer_relevancy_metric
        elif metric == "bias":
            self.worker_metric = self.bias_metric
        elif metric == "summarization":
            self.worker_metric = self.summarization_metric
        elif metric == "grammatical and spelling correctness":
            self.worker_metric = self.grammatical_and_spelling_correctness_metric
        elif metric == "grice maxims":
            self.worker_metric = self.grice_maxims_metric
        try:
            await self.worker_metric.a_measure(test_case)
            await asyncio.sleep(0.1)
            print(self.worker_metric.score)
            print(self.worker_metric.reason)
        except Exception as e:
            print("Fehler bei a_measure:", e)


    async def evaluate(self):
        scores=[]
        try:
            for case in self.eval_set:
                test_case = LLMTestCase(
                    input=case[0],
                    actual_output=case[1],
                    context=self.context
                )
                await self.eval_by_metric(self.metric, test_case)
                scores.append(str(self.worker_metric.score))
            pyperclip.copy("\n".join(scores))
            print("evaluated {}".format(self.metric))
        except Exception as e:
            return str(e)


    async def evaluate_summarization(self, to_summarize):
        scores = []
        try:
            for case in self.eval_set:
                test_case = LLMTestCase(
                    input=to_summarize,
                    actual_output=case[1],
                    context=self.context
                )
                await self.eval_by_metric(self.metric, test_case)
                scores.append(str(self.worker_metric.score))
            pyperclip.copy("\n".join(scores))
            print("evaluated {}".format(self.metric))
        except Exception as e:
            return str(e)

    async def evaluate_mauve(self, reference):
        scores = []
        try:
            ref_features = await featurize_text(reference)
            for case in self.eval_set:
                mauve_result = mauve.compute_mauve(
                    p_features=ref_features,
                    q_text=case[1],
                    device_id=0
                )
                scores.append(str(mauve_result.mauve))
            pyperclip.copy("\n".join(scores))
            print("evaluated {}".format(self.metric))
        except Exception as e:
            return str(e)
