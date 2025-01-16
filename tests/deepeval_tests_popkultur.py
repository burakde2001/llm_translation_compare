import asyncio

from dotenv import load_dotenv

from EvalLoop import EvalLoop
from results.results_discolm import football_results_discolm
from results.results_gemini import football_results_gemini
from results.results_gpt import football_results_gpt35turbo
from results.results_leo import football_results_leo
from results.results_llama import football_results_llama32
from results.results_mistral import football_results_mistral
from results.results_sauerkrautlm import football_results_sauerkrautlm

load_dotenv()

# print("G-Eval Correctness")
# print("=== GPT 3.5-turbo")
# eval_correctness_gpt35turbo = EvalLoop(football_results_gpt35turbo, "correctness", [""])
# asyncio.run(eval_correctness_gpt35turbo.evaluate())
#
# print("=== Llama 3.2")
# eval_correctness_llama32 = EvalLoop(football_results_llama32, "correctness", [""])
# asyncio.run(eval_correctness_llama32.evaluate())
#
# print("=== Leo")
# eval_correctness_leo = EvalLoop(football_results_leo, "correctness", [""])
# asyncio.run(eval_correctness_leo.evaluate())
#
# print("=== DiscoLM")
# eval_correctness_discolm = EvalLoop(football_results_discolm, "correctness", [""])
# asyncio.run(eval_correctness_discolm.evaluate())
#
# print("=== Sauerkraut")
# eval_correctness_sauerkrautlm = EvalLoop(football_results_sauerkrautlm, "correctness", [""])
# asyncio.run(eval_correctness_sauerkrautlm.evaluate())
#
# print("=== Mistral")
# eval_correctness_mistral = EvalLoop(football_results_mistral, "correctness", [""])
# asyncio.run(eval_correctness_mistral.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_correctness_gemini = EvalLoop(football_results_gemini, "correctness", [""])
# asyncio.run(eval_correctness_gemini.evaluate())
#
context=['Wer der beste Fußballer aller Zeiten ist, kann nicht 100% objektiv beantwortet werden, denn alle Spieler sind anders, und es haben viele Kriterien einen Einfluss. Jedoch einigen sich die meisten Fans und Experten, dass es einer von vier Spielern ist:\n\n1. **Pelé** - Der Brasilianer Pelé gilt als einer der besten Spieler aller Zeiten, wegen seinen vielen Toren und drei gewonnenen Weltmeisterschaften in 1958, 1962 und 1970.\n\n2. **Diego Maradona** - Der Argentinier ist bekannt für seine Dribbelkünste und vielen Tore. Auch er gewann im Jahr 1986 die Weltmeisterschaft.\n\n3. **Lionel Messi** - Ebenfalls aus Argentinien, wird Messi oft gelobt für seine außergewöhnlichen technischen Fähigkeiten, seine vielen Tore und Vorlagen, und seine zahlreichen Rekorde und Auszeichnungen, darunter 8 Ballon d\'Or-Titel, die meisten Ballon d\'Ors für eine Person.\n\n4. **Cristiano Ronaldo** - Der portugiesische Superstar wird hoch angesehen für seine athletische Fähigkeit, Torgefährlichkeit, Mentalität, viele Titelgewinne mit verschiedenen Vereinen, viele gebrochene Rekorde und persönliche Auszeichnungen, darunter 5 Ballon d\'Ors.\n\nAb und zu werden jedoch auch andere Spieler als mögliche Kandidaten für den besten aller Zeiten genannt.']
# print("Hallucination")
# print("=== GPT 3.5-turbo")
# eval_hallucination_gpt35turbo = EvalLoop(football_results_gpt35turbo, "hallucination", context)
# asyncio.run(eval_hallucination_gpt35turbo.evaluate())
#
# print("=== Llama 3.2")
# eval_hallucination_llama32 = EvalLoop(football_results_llama32, "hallucination", context)
# asyncio.run(eval_hallucination_llama32.evaluate())
#
# print("=== Leo")
# eval_hallucination_leo = EvalLoop(football_results_leo, "hallucination", context)
# asyncio.run(eval_hallucination_leo.evaluate())
#
# print("=== DiscoLM")
# eval_hallucination_discolm = EvalLoop(football_results_discolm, "hallucination", context)
# asyncio.run(eval_hallucination_discolm.evaluate())
#
# print("=== Sauerkraut")
# eval_hallucination_sauerkrautlm = EvalLoop(football_results_sauerkrautlm, "hallucination", context)
# asyncio.run(eval_hallucination_sauerkrautlm.evaluate())
#
# print("=== Mistral")
# eval_hallucination_mistral = EvalLoop(football_results_mistral, "hallucination", context)
# asyncio.run(eval_hallucination_mistral.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_hallucination_gemini = EvalLoop(football_results_gemini, "hallucination", context)
# asyncio.run(eval_hallucination_gemini.evaluate())
#
# print("Answer relevancy")
# print("=== GPT 3.5-turbo")
# eval_answer_relevancy_gpt35turbo = EvalLoop(football_results_gpt35turbo, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_gpt35turbo.evaluate())
#
# print("=== Llama 3.2")
# eval_answer_relevancy_llama32 = EvalLoop(football_results_llama32, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_llama32.evaluate())
#
# print("=== Leo")
# eval_answer_relevancy_leo = EvalLoop(football_results_leo, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_leo.evaluate())
#
# print("=== DiscoLM")
# eval_answer_relevancy_discolm = EvalLoop(football_results_discolm, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_discolm.evaluate())
#
# print("=== Sauerkraut")
# eval_answer_relevancy_sauerkrautlm = EvalLoop(football_results_sauerkrautlm, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_sauerkrautlm.evaluate())
#
# print("=== Mistral")
# eval_answer_relevancy_mistral = EvalLoop(football_results_mistral, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_mistral.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_answer_relevancy_gemini = EvalLoop(football_results_gemini, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_gemini.evaluate())
#
# print("Bias")
# print("=== GPT 3.5-turbo")
# eval_bias_gpt35turbo = EvalLoop(football_results_gpt35turbo, "bias", [""])
# asyncio.run(eval_bias_gpt35turbo.evaluate())
#
# print("=== Llama 3.2")
# eval_bias_llama32 = EvalLoop(football_results_llama32, "bias", [""])
# asyncio.run(eval_bias_llama32.evaluate())
#
# print("=== Leo")
# eval_bias_leo = EvalLoop(football_results_leo, "bias", [""])
# asyncio.run(eval_bias_leo.evaluate())
#
# print("=== DiscoLM")
# eval_bias_discolm = EvalLoop(football_results_discolm, "bias", [""])
# asyncio.run(eval_bias_discolm.evaluate())
#
# print("=== Sauerkraut")
# eval_bias_sauerkrautlm = EvalLoop(football_results_sauerkrautlm, "bias", [""])
# asyncio.run(eval_bias_sauerkrautlm.evaluate())
#
# print("=== Mistral")
# eval_bias_mistral = EvalLoop(football_results_mistral, "bias", [""])
# asyncio.run(eval_bias_mistral.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_bias_gemini = EvalLoop(football_results_gemini, "bias", [""])
# asyncio.run(eval_bias_gemini.evaluate())
#
# print("Grammatical and Spelling Correctness")
# print("=== GPT 3.5-turbo")
# eval_bias_gpt35turbo = EvalLoop(football_results_gpt35turbo, "grammatical and spelling correctness", [""])
# asyncio.run(eval_bias_gpt35turbo.evaluate())
#
# print("=== Llama 3.2")
# eval_grammatical_and_spelling_correctness_llama32 = EvalLoop(football_results_llama32, "grammatical and spelling correctness", [""])
# asyncio.run(eval_grammatical_and_spelling_correctness_llama32.evaluate())
#
# print("=== Leo")
# eval_grammatical_and_spelling_correctness_leo = EvalLoop(football_results_leo, "grammatical and spelling correctness", [""])
# asyncio.run(eval_grammatical_and_spelling_correctness_leo.evaluate())
#
# print("=== DiscoLM")
# eval_grammatical_and_spelling_correctness_discolm = EvalLoop(football_results_discolm, "grammatical and spelling correctness", [""])
# asyncio.run(eval_grammatical_and_spelling_correctness_discolm.evaluate())
#
# print("=== Sauerkraut")
# eval_grammatical_and_spelling_correctness_sauerkrautlm = EvalLoop(football_results_sauerkrautlm, "grammatical and spelling correctness", [""])
# asyncio.run(eval_grammatical_and_spelling_correctness_sauerkrautlm.evaluate())
#
# print("=== Mistral")
# eval_grammatical_and_spelling_correctness_mistral = EvalLoop(football_results_mistral, "grammatical and spelling correctness", [""])
# asyncio.run(eval_grammatical_and_spelling_correctness_mistral.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_grammatical_and_spelling_correctness_gemini = EvalLoop(football_results_gemini, "grammatical and spelling correctness", [""])
# asyncio.run(eval_grammatical_and_spelling_correctness_gemini.evaluate())
#
# print("Grice Maxims")
# print("=== GPT 3.5-turbo")
# eval_grice_maxims_gpt35turbo = EvalLoop(football_results_gpt35turbo, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_gpt35turbo.evaluate())
#
# print("=== Llama 3.2")
# eval_grice_maxims_llama32 = EvalLoop(football_results_llama32, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_llama32.evaluate())
#
# print("=== Leo")
# eval_grice_maxims_leo = EvalLoop(football_results_leo, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_leo.evaluate())
#
# print("=== DiscoLM")
# eval_grice_maxims_discolm = EvalLoop(football_results_discolm, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_discolm.evaluate())
#
# print("=== Sauerkraut")
# eval_grice_maxims_sauerkrautlm = EvalLoop(football_results_sauerkrautlm, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_sauerkrautlm.evaluate())
#
# print("=== Mistral")
# eval_grice_maxims_mistral = EvalLoop(football_results_mistral, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_mistral.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_grice_maxims_gemini = EvalLoop(football_results_gemini, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_gemini.evaluate())
#
# print("Naturalness")
# print("=== GPT 3.5-turbo")
# eval_naturalness_gpt35turbo = EvalLoop(football_results_gpt35turbo, "naturalness", [""])
# asyncio.run(eval_naturalness_gpt35turbo.evaluate_mauve(context[0]))
#
# print("=== Llama 3.2")
# eval_naturalness_llama32 = EvalLoop(football_results_llama32, "naturalness", [""])
# asyncio.run(eval_naturalness_llama32.evaluate_mauve(context[0]))
#
# print("=== Leo")
# eval_naturalness_leo = EvalLoop(football_results_leo, "naturalness", [""])
# asyncio.run(eval_naturalness_leo.evaluate_mauve(context[0]))
#
# print("=== DiscoLM")
# eval_naturalness_discolm = EvalLoop(football_results_discolm, "naturalness", [""])
# asyncio.run(eval_naturalness_discolm.evaluate_mauve(context[0]))
#
# print("=== Sauerkraut")
# eval_naturalness_sauerkrautlm = EvalLoop(football_results_sauerkrautlm, "naturalness", [""])
# asyncio.run(eval_naturalness_sauerkrautlm.evaluate_mauve(context[0]))
#
# print("=== Mistral")
# eval_naturalness_mistral = EvalLoop(football_results_mistral, "naturalness", [""])
# asyncio.run(eval_naturalness_mistral.evaluate_mauve(context[0]))
#
# print("=== Gemini 1.5 Pro")
# eval_naturalness_gemini = EvalLoop(football_results_gemini, "naturalness", [""])
# asyncio.run(eval_naturalness_gemini.evaluate_mauve(context[0]))
