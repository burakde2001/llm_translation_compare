import asyncio

from dotenv import load_dotenv

from EvalLoop import EvalLoop
from results.results_rag_gemini import africa_ww2_results_gemini
from results.results_rag_gpt import africa_ww2_results_gpt35turbo

load_dotenv()

to_summarize="""
>Afrika im Zweiten Weltkrieg

Kriegsschauplatz Ostafrika

Als Italien unter Mussolini 1940 an der Seite der Achsenmächte in den Krieg einstieg, bedeutete das für die Briten eine akute Gefährdung der von ihnen kontrollierten Handelsrouten durch das Rote Meer. Die britischen Truppen in Ägypten und Sudan waren den italienischen Truppen in Eritrea, Äthiopien und Libyen zahlenmäßig unterlegen. Der erste Zusammenstoß der beiden Mächte fand im Sommer 1940 in Somalia statt. Der Nordwesten des Landes war britisch, der Osten italienisch. Von Äthiopien (damals: Abessinien) aus begann die italienische Armee, in der auch viele Afrikaner kämpften, eine Offensive in den britischen Teil Somalias. In wenigen Tagen zwangen die Italiener die Briten, sich aus Somalia zurückzuziehen.

Im Winter 1941 erfolgte die Gegenoffensive der Alliierten, die von abessinischen Partisanen in Äthiopien unterstützt wurde, aus zwei Hauptrichtungen: Im Süden aus Kenia, damals Britisch Ostafrika, und aus dem Sudan im Westen. Im April des Jahres brachten britische, südafrikanische und äthiopische Verbände Addis Abeba unter Kontrolle. Der Sieg über die italienischen Streitkräfte im Norden des Landes unter dem Kommando des Herzogs von Aosta erfolgte am 18. Mai 1941. Die Feindseligkeiten in anderen Landesteilen sowie in der italienischen Kolonie Eritrea dauerten aber an, bis 1943 Italien auf die Seite der Alliierten wechselte.

Auch in Libyen kam es zu wechselseitigen Angriffen und Gegenangriffen zwischen Italien und Großbritannien, mit dem Ergebnis, dass die Italiener im Februar 1941 beinahe gezwungen waren, Libyen zu verlassen. Aufgrund der Gefahr durch die einbrechenden italienischen Linien in Libyen, und dem damit drohenden Verlust des gesamten Landes und seines Kolonialgebietes an Großbritannien, ersuchte Benito Mussolini in Berlin um militärische Unterstützung.
__

>Rommels Afrikafeldzug

Adolf Hitler sah sich gezwungen, deutsche Truppen in diesen Konflikt einzubinden (siehe Afrikakorps), um die Schwächung der Achse Berlin-Rom, durch eine Niederlage Italiens gegen Großbritannien, zu verhindern. Erster Kommandeur der deutschen Truppen wurde Generalleutnant Erwin Rommel, der später den Spitznamen „Wüstenfuchs“ bekam. Im Gegensatz zur geplanten, defensiven Haltung des Afrikakorps hielt Rommel ein offensives Vorgehen gegen die britischen Truppen für unbedingt notwendig. Er startete rasche Angriffe mittels mechanisierter Streitkräfte (Panzer), die für die Wüste ideal geeignet waren. Durch Rommels erfolgreiche Taktik des mobilen Wüstenkriegs wurden die überlegenen britischen Truppen über 800 Kilometer zurückgeworfen.

Die schnellen Erfolge führten auf britischer Seite zu einem tiefen Schock. Der deutsche Vormarsch stoppte Mitte April bei der ägyptischen Grenzstadt Sollum östlich von Tobruk. Hier hatte das Afrikakorps bereits mit Versorgungsengpässen zu kämpfen.

Im November begannen britische Truppen mit Gegenangriffen und warfen das deutsche Afrikakorps bis Ende 1941 auf seine Ausgangsstellung am Westrand der Cyrenaika zurück.

Im Januar 1942 ergriff Rommel wieder die Initiative. Mit der Hilfe Albert Kesselrings Luftflotte führte er eine Offensive an, die die deutschen Truppen bis El-Alamein brachte. Danach versuchte er erfolgreich Tobruk einzunehmen. Doch der Angriff auf Alexandria scheiterte am zahlenmäßig überlegenen Widerstand der Briten, die unter Bernard Montgomery einen Gegenschlag begannen. Im Zuge dieses Vorstoßes wurde das Afrikakorps erneut nach Libyen zurückgedrängt.

Im November 1942 landeten amerikanische und britische Truppen in Casablanca und Algier. Von dem Zeitpunkt an mussten die Deutschen an zwei Fronten kämpfen. Aufgrund der kritischen Situation an der Ostfront konnte das Oberkommando der Wehrmacht (OKW) jedoch nur unzureichende Verstärkung entsenden, Rommels Afrikakorps war überfordert.

Nachschubprobleme und die Unterlegenheit der Deutschen und Italiener gaben im Frühjahr 1943 unter anderem den Ausschlag für den vollständigen Sieg der Westalliierten in Afrika.

Der Afrikafeldzug kostete ungefähr 84 000 Soldaten das Leben, davon 35 500 Briten und 18 600 Deutsche.
__

Kriegsschauplatz Westafrika

Nach der Waffenruhe zwischen Frankreich und Deutschland war unklar, ob sich die französischen Kolonien der Résistance oder dem Vichy-Regime anschlossen. Französisch-Kamerun und Französisch-Äquatorialafrika bekannten sich zu de Gaulle, Französisch-Westafrika und Algerien hingegen zu Vichy.

Dakar war der wichtigste strategische Punkt auf diesem Kriegsschauplatz, weil dort große Goldreserven der Banque de France lagerten. Außerdem hätten die Alliierten durch die Kontrolle des Hafens von Dakar den (militärischen) Schiffsverkehr besser schützen können.

Im September 1940 versuchte eine kleine alliierte Flotte, den Hafen einzunehmen, und scheiterte. Der Angriff wurde jedoch nur halbherzig geführt, da de Gaulle kein französisches Blut vergießen wollte. Von britischer Seite wurde 1941/42 die Operation Postmaster durchgeführt, ein Kommandounternehmen gegen Handelsschiffe der Achsenmächte an der Küste Westafrikas.

"""
reference="""
In Ostafrika marschierte 1940 Mussolinis Italien aus den Kolonien Eritrea und Somalia, sowie dem besetzten Äthiopien, was damals auch Abessinien genannt wurde, in die britische Kolonie Somaliland ein. Da die britischen Truppen zahlenmäßig unterlegen waren, mussten sie sich zurückziehen.
Etwa ein Jahr später, im Winter 1941, starteten die Briten eine Gegenoffensive aus Sudan im Westen und Kenia, damals Britisch Ostafrika, im Süden. Die Truppen, sowie britische Kolonialtruppen als auch afrikanische Partisanen vor allem aus Äthiopien, eroberten Addis Abeba, die Hauptstadt von Äthiopien, im April zurück. Die Alliierten erzielten wichtige Siege und eroberten weitere Gebiete zurück bis 1943, wo Italien auf die Seite der Alliierten wechselte.
Ebenfalls im Frühjahr 1941 kam es in Nordafrika vor allem in der italienischen Kolonie Libyen zu Kämpfen zwischen den Italienern und den Briten. Hier waren die britischen Truppen erfolgreicher, was dazu führte, dass die Italiener im Februar fast gezwungen waren, sich aus Libyen zurückzuziehen. Um zu verhindern, dass das ganze Kolonialgebiet Italiens im südlichen Mittelmeer an die Briten fiel, bat Mussolini Hitler um militärische Unterstützung.
Daraufhin sendete Hitler deutsche Truppen, den Afrikakorps, nach Nordafrika, um eine Niederlage Italiens gegen Großbritannien zu unterbinden. Erster Kommandeur war Generalleutnant Erwin Rommel, der eventuell den Spitznamen "Wüstenfuchs" bekam. Mit einer Reihe von Panzern startete Rommel einen großen Offensivfeldzug, den Afrikafeldzug.
Am Anfang erzielte Rommel schnelle und wichtige Erfolge mit seiner Taktik des mobilen Wüstenkriegs. In kurzer Zeit konnten deutsche Truppen die Briten um bis zu 800 Kilometer zurückdrängen und bis nach Ägypten vorstoßen. Jedoch kam es zu Versorgungsengpässen, was den Briten die Chance gab, die Deutschen wieder zurückzudrängen.
Im Januar 1942 startete Rommel mit Hilfe der Luftflotte unter Führung von Albert Kesselring in der die deutschen Truppen die libysche Stadt Tobruk und die ägyptische Stadt El-Alamein eroberten. Allerdings konnte er die ägyptische Stadt Alexandria aufgrund heftigen Widerstands der Briten nicht erobern, und wurde erneut nach Libyen zurückgedrängt.
Ab November 1942 mussten die Deutschen und Italiener an zwei Fronten kämpfen, denn Truppen aus Amerika und Großbritannien landeten im Westen in Casablanca und Algier. Von diesem Zeitpunkt an wurden die Nachschubprobleme und Unterlegenheit der Achsenmächte verstärkt, der Afrikakorps war immer weiter überfordert. Schließlich erlangten die Alliierten im Frühjahr 1943 einen vollständigen Sieg in Nordafrika.
Etwa 84000 Soldaten verloren im Afrikafeldzug ihr Leben, darunter circa 35500 Briten und 18600 Deutsche.
Weiterhin gab es kleinere Kämpfe zwischen den Achsenmächten und den Alliierten in westlichen Teilen Afrikas.   
"""
# print("Summarization")
# print("=== GPT 3.5-turbo")
# eval_summarization_gpt35turbo = EvalLoop(africa_ww2_results_gpt35turbo, "summarization", [""])
# asyncio.run(eval_summarization_gpt35turbo.evaluate_summarization(to_summarize))
#
# print("=== Gemini 1.5 Pro")
# eval_summarization_gemini = EvalLoop(africa_ww2_results_gemini, "summarization", [""])
# asyncio.run(eval_summarization_gemini.evaluate_summarization(to_summarize))
#
# print("G-Eval Correctness")
# print("=== GPT 3.5-turbo")
# eval_correctness_gpt35turbo = EvalLoop(africa_ww2_results_gpt35turbo, "correctness", [""])
# asyncio.run(eval_correctness_gpt35turbo.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_correctness_gemini = EvalLoop(africa_ww2_results_gemini, "correctness", [""])
# asyncio.run(eval_correctness_gemini.evaluate())
#
# print("Hallucination")
# print("=== GPT 3.5-turbo")
# eval_hallucination_gpt35turbo = EvalLoop(africa_ww2_results_gpt35turbo, "hallucination", [to_summarize])
# asyncio.run(eval_hallucination_gpt35turbo.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_hallucination_gemini = EvalLoop(africa_ww2_results_gemini, "hallucination", [to_summarize])
# asyncio.run(eval_hallucination_gemini.evaluate())
#
# print("Answer relevancy")
# print("=== GPT 3.5-turbo")
# eval_answer_relevancy_gpt35turbo = EvalLoop(africa_ww2_results_gpt35turbo, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_gpt35turbo.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_answer_relevancy_gemini = EvalLoop(africa_ww2_results_gemini, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_gemini.evaluate())
#
# print("Grammatical and Spelling Correctness")
# print("=== GPT 3.5-turbo")
# eval_bias_gpt35turbo = EvalLoop(africa_ww2_results_gpt35turbo, "grammatical and spelling correctness", [""])
# asyncio.run(eval_bias_gpt35turbo.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_grammatical_and_spelling_correctness_gemini = EvalLoop(africa_ww2_results_gemini, "grammatical and spelling correctness", [""])
# asyncio.run(eval_grammatical_and_spelling_correctness_gemini.evaluate())
#
# print("Grice Maxims")
# print("=== GPT 3.5-turbo")
# eval_grice_maxims_gpt35turbo = EvalLoop(africa_ww2_results_gpt35turbo, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_gpt35turbo.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_grice_maxims_gemini = EvalLoop(africa_ww2_results_gemini, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_gemini.evaluate())
#
# print("Naturalness")
# print("=== GPT 3.5-turbo")
# eval_naturalness_gpt35turbo = EvalLoop(africa_ww2_results_gpt35turbo, "naturalness", [""])
# asyncio.run(eval_naturalness_gpt35turbo.evaluate_mauve(reference))
#
# print("=== Gemini 1.5 Pro")
# eval_naturalness_gemini = EvalLoop(africa_ww2_results_gemini, "naturalness", [""])
# asyncio.run(eval_naturalness_gemini.evaluate_mauve(reference))
