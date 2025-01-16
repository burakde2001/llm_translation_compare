import asyncio

from dotenv import load_dotenv

from EvalLoop import EvalLoop
from results.results_discolm import karlsruhe_results_discolm
from results.results_gemini import karlsruhe_results_gemini
from results.results_gpt import karlsruhe_results_gpt35turbo
from results.results_leo import karlsruhe_results_leo
from results.results_llama import karlsruhe_results_llama32
from results.results_mistral import karlsruhe_results_mistral
from results.results_sauerkrautlm import karlsruhe_results_sauerkrautlm

load_dotenv()

context_1 = """Museen und Galerien

In Karlsruhe gibt es eine Vielzahl an staatlichen, städtischen und privaten Museen und Einrichtungen. Zahlreiche Ausstellungen mit unterschiedlichen Schwerpunkten präsentieren naturwissenschaftliche Themen, Medienkunst sowie zeitgenössische und klassische künstlerische Positionen.
__

Eine weltweit einzigartige Kulturinstitution ist das ZKM | Zentrum für Kunst und Medien. Als „Mekka der Medienkunst“ erforscht und präsentiert es die neuesten Medienentwicklungen sowie die Auswirkungen der Digitalisierung auf Kunst und Gesellschaft. Es vereint Ausstellungen und Veranstaltungen, Produktion und Forschung, Vermittlung und Dokumentation im Bereich der Kunst mit neuen Medien. Neben interaktiven Umgebungen, in denen sich die Besucherinnen und Besucher wie in der realen Welt bewegen können, versetzen überwältigende Installationen auf einer gigantischen Ausstellungsfläche von 15.000 Meter in Staunen.
__

Das Badische Landesmuseum präsentiert im ehemaligen Residenzschloss der Großherzöge Badens Zeugnisse aus mehr als 50.000 Jahre Kulturgeschichte von der Ur- und Frühgeschichte bis in die jüngste Gegenwart. Hervorzuheben ist eine der schönsten Antikensammlungen Deutschlands, zu der Objekte der Kykladenkultur, der frühen Hochkulturen und des klassischen Griechenlands zählen. Zu den besonderen Höhepunkten gehört die fürstliche Kunst- und Wunderkammer sowie die sogenannte „Türkenbeute“, eine historisch einzigartige Trophäensammlung aus den Türkenkriegen des 17. Jahrhunderts. Die Sammlungs- und Sonderausstellungen laden zum Schauen, Entdecken und Experimentieren ein. 

Das Museum beim Markt ist eine Außenstelle des Badischen Landesmuseums und rückt die Sammlungen zur Kunst des 20. Jahrhunderts in den Fokus. Mit seiner Dauerausstellung in der ersten Etage und seinen Wechselausstellungen im Erdgeschoss schlägt das Museum beim Markt die Brücke zu den historischen Sammlungen im Karlsruher Schloss. Mit Werken des 1919 gegründeten Bauhauses bietet die Sammlung einen repräsentativen Überblick über das Design-Geschehen vom Funktionalismus bis hin zu aktuellen Erzeugnissen.

Das Museum in der Majolika, ein Zweigmuseum des Badischen Landesmuseums, gibt einen Überblick über die Produktion der Manufaktur von ihren Anfängen bis in die Gegenwart. Gezeigt wird der künstlerische Wandel im 19. und 20. Jahrhundert anhand zahlreicher Exponate – vom Jugendstil über den Expressionismus, von der Kunst des Nationalsozialismus über die Tendenzen der 1950er- und 1960er-Jahre bis hin zu den gegenwärtigen Kunstströmungen.
__

Die Staatliche Kunsthalle gehört nicht nur zu den ältesten Museumsbauten Deutschlands, sondern verfügt mit Werken von Dürer, Rubens, Rembrandt, Cézanne und Degas bis hin zu Ernst und Richter auch über eine der bedeutendsten Kunstsammlungen. Seit dem 1. November 2021 ist die Kunsthalle für mehrere Jahre geschlossen, in denen das Museum saniert und erweitert wird. Einem digitalen Besuch steht in dieser Zeit jedoch nichts im Wege: Die zahlreichen Online-Angebote verbinden Wissenswertes und Unterhaltsames zu den Werken der Kunsthalle mit zahlreichen Blicken hinter die Kulissen. Ab September 2022 sind die Highlights der Sammlung dann wieder live und in Farbe zu sehen – zu Gast im ZKM | Zentrum für Kunst und Medien.
__

Die Städtische Galerie ist das Kunstmuseum für moderne und zeitgenössische Kunst der Stadt Karlsruhe. In einem der größten Industriedenkmäler Deutschlands mit einer einzigartigen Architektur zeigt sie Wechselausstellungen zur internationalen Kunst des 20. und 21. Jahrhunderts begleitet von Präsentationen aus der eigenen Sammlung. In diesem Dialog gibt sie einen breit gefächerten Überblick über die Kunst von der Moderne bis in die Gegenwart.
__

Der 1818 gegründete Badische Kunst­ver­ein, der seit 1900 das für seine Zwecke erbaute Haus in der Waldstraße im Zentrum der Stadt bespielt, ist der zweitälteste Kunstverein Deutschlands. Auf 1.000 Quadratmeter Ausstellungsfläche wird in wechselnden Gruppen- und Einzelausstellungen ein lokal wie global ausgerichtetes Programm gezeigt. Dabei werden oftmals künstlerische Positionen präsentiert, die bislang wenig Beachtung fanden. Die Ausstellungen werden von einem Rahmenprogramm sowie von öffentlichen Führungen begleitet. Der Badische Kunstverein ist Preisträger des ADKV-Art Cologne Preis (Arbeitsgemeinschaft Deutscher Kunstvereine) für Kunstvereine 2012.
__

Im Rahmen von wechselnden Ausstellungen und unterschiedlichen Veranstaltungen erleben die Besucherinnen und Besucher die Entwicklung der Fächerstadt von der Gründung bis zur Gegenwart. Meilensteine der Stadtgeschichte, aber auch weniger Bekanntes stehen dabei im Fokus der Präsentationen im Stadtmuseum.

Eindrucksvolle Exponate, attraktive Inszenierungen und interaktive Medienstationen laden zum Eintauchen in die Vergangenheit Karlsruhes ein. Politik und Gesellschaft, Industrie und Gewerbe, Stadtentwicklung und Verkehr werden dabei ebenso beleuchtet wie Sport, Freizeit und künstlerisches Schaffen in Karlsruhe. Unterschiedliche Blickwinkel und thematische Bögen zur Gegenwart regen zur Auseinandersetzung mit der Stadtgeschichte an.
"""
context_2 = """Das Wasser- und Brunnenmuseum der Stadtwerke Karlsruhe befindet sich im geschichtsträchtigen Wasserwerk Durlacher Wald. Exponate aus Technik, Kunst und Geschichte laden zu einer Zeitreise durch die Karlsruher Trink­was­ser­ver­sor­gung ein. Wechselnde Ausstellungen zeigen ausgewählte Kunstwerke vieler namhafter Künstler über die 204 öffentlich zugänglichen Karlsruher Brunnen."""
context_3 = """Soziokultur und Stadtgesellschaft

Eine lebenswerte Stadt verlangt kulturelle Vielfalt und Teilhabe. Wie bunt und bereichernd ein kultureller Austausch sein kann, zeigen Orte der Soziokultur und die Themen der Stadtgesellschaft in Karlsruhe.
__

Das Tollhaus ist ein freies Kulturzentrum mit weitreichender Ausstrahlung. Es steht für ein anspruchsvolles, zeitgenössisches Programm aus sämtlichen Kultursparten: Neuer Zirkus, Tanztheater, Kleinkunst und Kabarett, Weltmusik, Jazz finden hier ebenso einen Ort wie Pop und Rock. Im Sommer veranstaltet das Tollhaus als einen seiner Jahreshöhepunkte das Zeltival und im Herbst das ATOLL Festival für zeitgenössischen Zirkus.
__

Der Tempel auf dem Gelände der ehemaligen Selden­eck´­schen Brauerei in Mühlburg ist seit 1984 unabhän­gi­ges sozio­kul­tu­rel­les Zentrum und lebendiger Kreativ­pool aller Sparten. Das Kultur­zen­trum bietet nicht nur Veran­stal­tun­gen  in den Bereichen Musik, Tanz, Kunst, sondern auch ein lebendiges Netzwerk für Kunst- und Kultur­schaf­fende der freien Szene. Für überre­gio­nale Strahl­kraft sorgt das alljähr­li­che Tanzfes­ti­val TANZ Karlsruhe.
__

Der deutsch-franzö­si­schen Begegnung widmet sich die Stiftung Centre Culturel Franco-Allemand mit einem abwechs­lungs­rei­chen und anspruchs­vol­len Kultu­r­an­ge­bot, das Ausstel­lun­gen, Lesungen, Film und Theater ebenso umfasst wie Konzerte, Vorträge und Sprachkurse. In der Mediathek des französischen Kulturzentrums findet sich darüber hinaus eine große Auswahl an franzö­si­schen Medien."""
context_4 =  """Kulturinteressierte aufgepasst: Das Zentrum für Kunst und Medien - kurz ZKM - ist eine der weltweit wichtigsten Kunstinstitutionen. Gemeinsam mit der Städtischen Galerie und der Staatlichen Hochschule für Gestaltung ist das ZKM in einer ehemaligen Munitionsfabrik am Platz der Menschenrechte beheimatet. Neben Produktion und Forschung könnt Ihr hier wechselnde Ausstellungen und Veranstaltungen besuchen, bei denen Interaktivität nie zu kurz kommt! Besonders lohnenswert ist die Dauerausstellung "zkm_gameplay. the next level"."""
reference="""
Um in Karlsruhe Kunst zu sehen, ist es empfehlenswert, folgende Orte zu besichtigen:
1. das ZKM: ZKM - Zentrum für Kunst und Medien - ist eine weltweit anerkannte Kunst- und Kulturinstitution. Als "Mekka der Medienkunst" bezeichnet, werden Ausstellungen und Veranstaltungen mit Fokus auf Digitalisierung und neuen Medien, ihrer Produktion und Forschung, sowie ihren Auswirkungen auf Kunst und Gesellschaft abgehalten. Besonders bemerkenswert ist der hohe Grad an Interaktivität mit der Umgebung und den Ausstellungsobjekten. Das ZKM befindet sich in einer ehemaligen Munitionsfabrik am Platz der Menschenrechte.
2. die Staatliche Kunsthalle: Als eines der ältesten Museumsbauten Deutschlands beheimatet die Staatliche Kunsthalle eine bedeutende Kunstsammlung mit Werken von Dürer, Rubens, Rembrandt, Cézanne und Degas bis hin zu Ernst und Richter.
3. die Städtische Galerie: Moderne und zeitgenössische Kunst der Stadt Karlsruhe finden sich in diesem Kunstmuseum wieder. Zusätzlich zur eigenen Sammlung werden internationale Kunstwerke aus dem 20. und 21. Jahrhundert in abwechselnden Ausstellungen gezeigt.
4. das Badische Landesmuseum: Dieses Museum, welches sich im ehemaligen Residenzschloss der Großherzöge Badens befindet, ist ein Geschichtsmuseum mit zahlreichen Antiken und historischen Artefakten von der Urgeschichte bis zur Gegenwart. Dieses Museum hat zwei Nebenmuseen, das Museum beim Markt und das Museum an der Majolika, welche in Dauer- und Wechselausstellungen Kunst des 19. und 20. Jahrhunderts zur Schau stellen.
5. das Wasser- und Brunnenmuseum: Die Stadtwerke Karlsruhe stellen in ihrem geschichtlichen Museum im Wasserwerk Durlacher Wald nicht nur Exponate aus Technik dar, sondern zeigen in wechselnden Ausstellungen auch Kunstwerke verschiedener namhafter Künstler über die 204 öffentlich zugänglichen Karlsruher Brunnen.
Dies sind fünf Beispiele von Orten, die man besuchen kann, um Kunst zu sehen.  
"""
# print("G-Eval Correctness")
# print("=== GPT 3.5-turbo")
# eval_correctness_gpt35turbo = EvalLoop(karlsruhe_results_gpt35turbo, "correctness", [""])
# asyncio.run(eval_correctness_gpt35turbo.evaluate())
#
# print("=== Llama 3.2")
# eval_correctness_llama32 = EvalLoop(karlsruhe_results_llama32, "correctness", [""])
# asyncio.run(eval_correctness_llama32.evaluate())
#
# print("=== Leo")
# eval_correctness_leo = EvalLoop(karlsruhe_results_leo, "correctness", [""])
# asyncio.run(eval_correctness_leo.evaluate())
#
# print("=== DiscoLM")
# eval_correctness_discolm = EvalLoop(karlsruhe_results_discolm, "correctness", [""])
# asyncio.run(eval_correctness_discolm.evaluate())
#
# print("=== Sauerkraut")
# eval_correctness_sauerkrautlm = EvalLoop(karlsruhe_results_sauerkrautlm, "correctness", [""])
# asyncio.run(eval_correctness_sauerkrautlm.evaluate())
#
# print("=== Mistral")
# eval_correctness_mistral = EvalLoop(karlsruhe_results_mistral, "correctness", [""])
# asyncio.run(eval_correctness_mistral.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_correctness_gemini = EvalLoop(karlsruhe_results_gemini, "correctness", [""])
# asyncio.run(eval_correctness_gemini.evaluate())
#
# print("Hallucination")
# print("=== GPT 3.5-turbo")
# eval_hallucination_gpt35turbo = EvalLoop(karlsruhe_results_gpt35turbo, "hallucination", [context_1, context_2, context_3, context_4])
# asyncio.run(eval_hallucination_gpt35turbo.evaluate())
#
# print("=== Llama 3.2")
# eval_hallucination_llama32 = EvalLoop(karlsruhe_results_llama32, "hallucination", [context_1, context_2, context_3, context_4])
# asyncio.run(eval_hallucination_llama32.evaluate())
#
# print("=== Leo")
# eval_hallucination_leo = EvalLoop(karlsruhe_results_leo, "hallucination", [context_1, context_2, context_3, context_4])
# asyncio.run(eval_hallucination_leo.evaluate())
#
# print("=== DiscoLM")
# eval_hallucination_discolm = EvalLoop(karlsruhe_results_discolm, "hallucination", [context_1, context_2, context_3, context_4])
# asyncio.run(eval_hallucination_discolm.evaluate())
#
# print("=== Sauerkraut")
# eval_hallucination_sauerkrautlm = EvalLoop(karlsruhe_results_sauerkrautlm, "hallucination", [context_1, context_2, context_3, context_4])
# asyncio.run(eval_hallucination_sauerkrautlm.evaluate())
#
# print("=== Mistral")
# eval_hallucination_mistral = EvalLoop(karlsruhe_results_mistral, "hallucination", [context_1, context_2, context_3, context_4])
# asyncio.run(eval_hallucination_mistral.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_hallucination_gemini = EvalLoop(karlsruhe_results_gemini, "hallucination", [context_1, context_2, context_3, context_4])
# asyncio.run(eval_hallucination_gemini.evaluate())
#
# print("Answer relevancy")
# print("=== GPT 3.5-turbo")
# eval_answer_relevancy_gpt35turbo = EvalLoop(karlsruhe_results_gpt35turbo, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_gpt35turbo.evaluate())
#
# print("=== Llama 3.2")
# eval_answer_relevancy_llama32 = EvalLoop(karlsruhe_results_llama32, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_llama32.evaluate())
#
# print("=== Leo")
# eval_answer_relevancy_leo = EvalLoop(karlsruhe_results_leo, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_leo.evaluate())
#
# print("=== DiscoLM")
# eval_answer_relevancy_discolm = EvalLoop(karlsruhe_results_discolm, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_discolm.evaluate())
#
# print("=== Sauerkraut")
# eval_answer_relevancy_sauerkrautlm = EvalLoop(karlsruhe_results_sauerkrautlm, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_sauerkrautlm.evaluate())
#
# print("=== Mistral")
# eval_answer_relevancy_mistral = EvalLoop(karlsruhe_results_mistral, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_mistral.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_answer_relevancy_gemini = EvalLoop(karlsruhe_results_gemini, "answer relevancy", [""])
# asyncio.run(eval_answer_relevancy_gemini.evaluate())
#
# print("Grammatical and Spelling Correctness")
# print("=== GPT 3.5-turbo")
# eval_bias_gpt35turbo = EvalLoop(karlsruhe_results_gpt35turbo, "grammatical and spelling correctness", [""])
# asyncio.run(eval_bias_gpt35turbo.evaluate())
#
# print("=== Llama 3.2")
# eval_grammatical_and_spelling_correctness_llama32 = EvalLoop(karlsruhe_results_llama32, "grammatical and spelling correctness", [""])
# asyncio.run(eval_grammatical_and_spelling_correctness_llama32.evaluate())
#
# print("=== Leo")
# eval_grammatical_and_spelling_correctness_leo = EvalLoop(karlsruhe_results_leo, "grammatical and spelling correctness", [""])
# asyncio.run(eval_grammatical_and_spelling_correctness_leo.evaluate())
#
# print("=== DiscoLM")
# eval_grammatical_and_spelling_correctness_discolm = EvalLoop(karlsruhe_results_discolm, "grammatical and spelling correctness", [""])
# asyncio.run(eval_grammatical_and_spelling_correctness_discolm.evaluate())
#
# print("=== Sauerkraut")
# eval_grammatical_and_spelling_correctness_sauerkrautlm = EvalLoop(karlsruhe_results_sauerkrautlm, "grammatical and spelling correctness", [""])
# asyncio.run(eval_grammatical_and_spelling_correctness_sauerkrautlm.evaluate())
#
# print("=== Mistral")
# eval_grammatical_and_spelling_correctness_mistral = EvalLoop(karlsruhe_results_mistral, "grammatical and spelling correctness", [""])
# asyncio.run(eval_grammatical_and_spelling_correctness_mistral.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_grammatical_and_spelling_correctness_gemini = EvalLoop(karlsruhe_results_gemini, "grammatical and spelling correctness", [""])
# asyncio.run(eval_grammatical_and_spelling_correctness_gemini.evaluate())
#
# print("Grice Maxims")
# print("=== GPT 3.5-turbo")
# eval_grice_maxims_gpt35turbo = EvalLoop(karlsruhe_results_gpt35turbo, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_gpt35turbo.evaluate())
#
# print("=== Llama 3.2")
# eval_grice_maxims_llama32 = EvalLoop(karlsruhe_results_llama32, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_llama32.evaluate())
#
# print("=== Leo")
# eval_grice_maxims_leo = EvalLoop(karlsruhe_results_leo, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_leo.evaluate())
#
# print("=== DiscoLM")
# eval_grice_maxims_discolm = EvalLoop(karlsruhe_results_discolm, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_discolm.evaluate())
#
# print("=== Sauerkraut")
# eval_grice_maxims_sauerkrautlm = EvalLoop(karlsruhe_results_sauerkrautlm, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_sauerkrautlm.evaluate())
#
# print("=== Mistral")
# eval_grice_maxims_mistral = EvalLoop(karlsruhe_results_mistral, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_mistral.evaluate())
#
# print("=== Gemini 1.5 Pro")
# eval_grice_maxims_gemini = EvalLoop(karlsruhe_results_gemini, "grice maxims", [""])
# asyncio.run(eval_grice_maxims_gemini.evaluate())
#
# print("Naturalness")
# print("=== GPT 3.5-turbo")
# eval_naturalness_gpt35turbo = EvalLoop(karlsruhe_results_gpt35turbo, "naturalness", [""])
# asyncio.run(eval_naturalness_gpt35turbo.evaluate_mauve(reference))
#
# print("=== Llama 3.2")
# eval_naturalness_llama32 = EvalLoop(karlsruhe_results_llama32, "naturalness", [""])
# asyncio.run(eval_naturalness_llama32.evaluate_mauve(reference))
#
# print("=== Leo")
# eval_naturalness_leo = EvalLoop(karlsruhe_results_leo, "naturalness", [""])
# asyncio.run(eval_naturalness_leo.evaluate_mauve(reference))
#
# print("=== DiscoLM")
# eval_naturalness_discolm = EvalLoop(karlsruhe_results_discolm, "naturalness", [""])
# asyncio.run(eval_naturalness_discolm.evaluate_mauve(reference))
#
# print("=== Sauerkraut")
# eval_naturalness_sauerkrautlm = EvalLoop(karlsruhe_results_sauerkrautlm, "naturalness", [""])
# asyncio.run(eval_naturalness_sauerkrautlm.evaluate_mauve(reference))
#
# print("=== Mistral")
# eval_naturalness_mistral = EvalLoop(karlsruhe_results_mistral, "naturalness", [""])
# asyncio.run(eval_naturalness_mistral.evaluate_mauve(reference))
#
# print("=== Gemini 1.5 Pro")
# eval_naturalness_gemini = EvalLoop(karlsruhe_results_gemini, "naturalness", [""])
# asyncio.run(eval_naturalness_gemini.evaluate_mauve(reference))
