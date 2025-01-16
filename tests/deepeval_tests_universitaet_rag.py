import asyncio

from dotenv import load_dotenv

from EvalLoop import EvalLoop
from results.results_rag_gemini import kit_results_gemini
from results.results_rag_gpt import kit_results_gpt35turbo

load_dotenv()

context_de=["""Deutsche und Deutschen gleichgestellte Bewerberinnen und Bewerber: Deutsche, EU-Staatsangehörige und Nicht-EU-Staatsangehörige mit deutscher Hochschulreife sind zum Studium am KIT berechtigt, wenn sie eine der folgenden Qualifikationen vorweisen können:
	                -1. Allgemeine Hochschulreife (Abitur)
	                -2. (einschlägige) Fachgebundene Hochschulreife (nicht Fachhochschulreife)
	                -3. Deltaprüfung der Universität Mannheim (für Inhaberinnen und Inhaber einer Fachhochschulreife)
	                -4. Eine anerkannte berufliche Aufstiegsfortbildung (z.B. Technikerin und Techniker, Meisterin und Meister) oder eine Eignungsprüfung für beruflich Qualifizierte
            Weitere Möglichkeiten siehe §58 Landeshochschulgesetz.
            Deutsche Staatsangehörige mit ausländischem Schulabschluss müssen sich vom zuständigen Regierungspräsidium die Gleichwertigkeit Ihres Abschlusses mit dem deutschen Abitur bescheinigen lassen.

            Nicht-EU-Staatsangehörige: Aus einigen Ländern ist das Schulabschlusszeugnis als direkte Hochschulzugangsberechtigung in Deutschland anerkannt. In vielen Fällen muss aber zusätzlich zum Schulabschluss noch eine Hochschulaufnahmeprüfung und/oder ein erfolgreiches Studienjahr im Heimatland und/oder die deutsche Feststellungsprüfung mit gültigen Dokumenten nachgewiesen werden, um in Deutschland ein Bachelorstudium aufnehmen zu dürfen. Die länderspezifischen Regelungen kannst du in der Zulassungsdatenbank des DAAD oder auf der Seite Anabin (nur in deutscher Sprache) der Zentralstelle für ausländisches Bildungswesen (ZAB) nachlesen.

            Deutschkenntnisse für ausländische Bewerberinnen und Bewerber: Um ein deutschsprachiges Studium aufnehmen zu können, müssen ausländische Bewerberinnen und Bewerber entsprechende Sprachkenntnisse nachweisen. Für die Bewerbung benötigst du mindestens Kenntnisse auf B1-Niveau. Alle Zertifikate werden akzeptiert, für die Bewerbung reicht aber bereits eine Teilnahmebescheinigung am B1-Kurs. Zur Einschreibung / Immatrikulation musst du die DSH2 oder eines der anerkannten Äquivalente vorlegen.

            Alle Bewerberinnen und Bewerber: Zusätzlich ist für alle Bewerberinnen und Bewerber unabhängig der Staatsangehörigkeit die Teilnahme am fachspezifischen Studienorientierungsverfahren Voraussetzung für eine Immatrikulation."""]
context_en=["""German applicants and those with German-equivalent applicant status: Germans, EU nationals, and non-EU nationals with a German university entrance qualification are eligible to study at KIT if they have one of the following qualifications:
                	-1. General university entrance qualification (Abitur)
                	-2. (relevant) Fachgebundene Hochschulreife (subject-linked university entrance qualification, not Fachhochschulreife / university of applied sciences entrace qualification)
                	-3. Delta examination of the University of Mannheim (for holders of a Fachhochschulreife)
                	-4. a recognized diploma of advanced vocational training (e.g. technician, Meister diploma for craftsman) or an aptitude test for vocationally qualified persons
            For additional possibilities, see §58 of the Landeshochschulgesetz (State Higher Education Act).
            German citizens with foreign school-leaving qualifications must have the equivalence of their qualification with the German Abitur certified by the responsible Regierungspraesidium (regional authority).

            Foreign nationals (non-EU): In Germany, the school leaving certificate of institutions in certain countries is accepted as direct means to enter university. In order to start your bachelor's studies in Germany, a university entrange test and / or one completed year of education at an institute of higher education and / or the "Feststellungsprüfung" (test of aptitude of foreign applicants for studies at universities in Germany) needs to be demonstrated in addition in most cases. You can find country-specific regulations in the "Zulassungsdatenbank des DAAD" (database on adimission requirements of the German Academy Exchange Service) or in the Anabin database (database of the "Zentralstelle für ausländisches Bildungswesen", only available in German).

            Knowledge of the German language for foreign nationals: In order to be accepted into a study program taught in German, foreign nationals need to demonstrate knowledge of the German language. For your application, you need to demonstrate knowledge of level B1. All such certificates are accepted, even a certificate of attendance of a B1 course. During the enrollment process, you need to submit a DSH2 certificate or an accepted equivalent thereof.

            All applicants: For all applicants, regardless of their nationality, participation in the subject-specific study orientation interview is a prerequisite for enrollment."""]
reference="""
Ja, um als internationaler Student an der KIT Informatik sturien zu können, musst du folgende Voraussetzungen erfüllen:
1. Falls du eine deutsche Hochschulreife hast, sind eine allgemeine Hochschulreife, d.h. Abitur, eine einschlägige fachgebundene Hochschulreife, eine Deltaprüfung der Universität Mannheim für Inhaber bzw. Inhaberinnen einer Fachhochschulreife, eine anerkannte berufliche Aufstiegsfortbildung z.B. als Techniker bzw. Technikerin oder Meister bzw. Meisterin, oder eine Eignungsprüfung für beruflich Qualifizierte, als Qualifikation zugelassen.
2. Falls du einen ausländischen Schulabschluss hast, musst du schauen, ob dein Schulabschluss als direkte Hochschulzugangsberechtigung in Deutschland anerkannt ist. Wenn nicht, dann musst du zusätzlich eine Hochschulaufnahmeprüfung und/oder ein erfolgreiches Studienjahr im Heimatland und/oder die deutsche Feststellungsprüfung mit gültigen Dokumenten bestehen und nachweisen, um in Deutschland ein Bachelorstudium anfangen zu dürfen. Länderspezifische Regelungen kannst du in der Zulassungsdatenbank des DAAD oder auf der Seite Anabin (nur in deutscher Sprache) der Zentralstelle für ausländisches Bildungswesen (ZAB) nachlesen.
3. Deutschkenntnisse auf mindestens B1-Niveau. Alle Zertifikate werden akzeptiert, für die Bewerbung reicht aber bereits eine Teilnahmebescheinigung am B1-Kurs. Zur Einschreibung bzw. Immatrikulation musst du die DSH2 oder eines der anerkannten Äquivalente vorlegen.
4. Teilnahme am fachspezifischen Studienorientierungsverfahren
Wenn du all diese Voraussetzungen erfüllst, kannst du dich bewerben mit der Chance, zum Studium zugelassen zu werden.
"""
# print("G-Eval Correctness")
# print("=== GPT 3.5-turbo")
# eval_correctness_gpt35turbo = EvalLoop(kit_results_gpt35turbo, "correctness", [""])
# asyncio.run(eval_correctness_gpt35turbo.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_correctness_gemini = EvalLoop(kit_results_gemini, "correctness", [""])
# asyncio.run(eval_correctness_gemini.evaluate())
#
# print("Hallucination de")
# print("=== GPT 3.5-turbo")
# eval_hallucination_gpt35turbo = EvalLoop(kit_results_gpt35turbo, "hallucination", context_de)
# asyncio.run(eval_hallucination_gpt35turbo.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_hallucination_gemini = EvalLoop(kit_results_gemini, "hallucination", context_de)
# asyncio.run(eval_hallucination_gemini.evaluate())
#
# print("Hallucination en")
# print("=== GPT 3.5-turbo")
# eval_hallucination_gpt35turbo = EvalLoop(kit_results_gpt35turbo, "hallucination", context_en)
# asyncio.run(eval_hallucination_gpt35turbo.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_hallucination_gemini = EvalLoop(kit_results_gemini, "hallucination", context_en)
# asyncio.run(eval_hallucination_gemini.evaluate())
#
# print("Answer relevancy")
# print("=== GPT 3.5-turbo")
# eval_answer_relevancy_gpt35turbo = EvalLoop(kit_results_gpt35turbo, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_gpt35turbo.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_answer_relevancy_gemini = EvalLoop(kit_results_gemini, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_gemini.evaluate())
#
# print("Grammatical and Spelling Correctness")
# print("=== GPT 3.5-turbo")
# eval_bias_gpt35turbo = EvalLoop(kit_results_gpt35turbo, "grammatical and spelling correctness", [""])
# asyncio.run(eval_bias_gpt35turbo.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_grammatical_and_spelling_correctness_gemini = EvalLoop(kit_results_gemini, "grammatical and spelling correctness", [""])
# asyncio.run(eval_grammatical_and_spelling_correctness_gemini.evaluate())
#
# print("Grice Maxims")
# print("=== GPT 3.5-turbo")
# eval_grice_maxims_gpt35turbo = EvalLoop(kit_results_gpt35turbo, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_gpt35turbo.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_grice_maxims_gemini = EvalLoop(kit_results_gemini, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_gemini.evaluate())
#
# print("Naturalness")
# print("=== GPT 3.5-turbo")
# eval_naturalness_gpt35turbo = EvalLoop(kit_results_gpt35turbo, "naturalness", [""])
# asyncio.run(eval_naturalness_gpt35turbo.evaluate_mauve(reference))
#
# print("=== Gemini 1.5 Pro")
# eval_naturalness_gemini = EvalLoop(kit_results_gemini, "naturalness", [""])
# asyncio.run(eval_naturalness_gemini.evaluate_mauve(reference))
