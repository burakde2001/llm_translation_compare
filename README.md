DE:

Dieses Programm wurde als Teil der Bachelorarbeit "Untersuchung von LLM Antworten auf verschiedenen Sprachen nach messbarer
Qualität" für das Fach Wirtschaftsinformatik von Burak Can Demirtas an der Hochschule Karlsruhe im Wintersemester 2024/2025 geschrieben.

Es ist eine wiederverwendbare und erweiterbare Anwendung für das Testen von LLM Antworten nach ihrer sprachlichen Qualität.

___

Dies ist eine Dokumentation der ausgeführten Schritte.

Schritte:

1. Erstelle in beliebigem Ordner das Verzeichnis "llm_translation_compare"

2. Wechsle in neu erstelltes Verzeichnis

3. Erstelle virtuelle Umgebung mit ``python -m venv .venv``
   1. "python" --> Das Programm Python soll ausgeführt werden (Vorausgesetzt, dass Python schon auf dem Rechner installiert und in die Pfadvariable "Path" in den Systemumgebungsvariablen gesetzt ist)
   2. "-m" --> Ruft ein Modul als Skript auf
   3. "venv" --> Zugriff auf Modul venv, welches normalerweise vorinstalliert mit Python kommt
   4. ".venv" --> Erstellt virtuelle Umgebung in neuem Verzeichnis .venv (Name ist frei wählbar, aber .venv ist konventional)

4. Aktiviere virtuelle Umgebung
   1. Windows PowerShell --> ``.venv\Scripts\Activate.ps1``
   2. Windows Bash --> ``source .venv/Scripts/activate``
   3. macOS, Linux --> ``source .venv/bin/activate``

5. Erstelle .gitignore für .venv mit ``echo "*" > .venv/.gitignore``

6. Installiere Python Web Framework FastAPI mit ``pip install "fastapi[standard]"``

7. Installiere folgende Erweiterungen für FastAPI:
   1. ``pip install "uvicorn[standard]"``
   2. ``pip install python-multipart sqlalchemy jinja2``
   3. ``pip install pydantic``
   4. ``pip install langchain_community``
   5. ``pip install langchain_openai``

8. Öffne neue Shell im Ordner "llm_translation_compare"

9. Installiere React Frontend Framework Vite mit ``npm create vite frontend --template react-ts`` (Vorausgesetzt Node.js und NPM sind schon auf dem Rechner installiert und in die Pfadvariable "Path" in den Systemumgebungsvariablen gesetzt)

10. Führe ``npm install`` aus

11. Installiere folgende Erweiterungen für React:
    1. ``npm install @mui/material @emotion/react @emotion/styled``
    2. ``npm install axios``

12. Starte Frontend Anwendung mit ``npm run dev``

13. Starte Backend Anwendung mit ``uvicorn app:app --reload``
    1. "app" hinter dem Doppelpunkt steht für die Datei "app.py"
    2. "app" nach dem Doppelpunkt steht für die Instanz "app" in der Datei "app.py"

Weiterführung:

-Installiere OllamaSetup\
-gehe in Installationsordner und öffne Terminal bzw. Powershell\
-Lade herunter und starte beliebige LLM auf Ollama:\
    1. ``ollama pull llama3.2``\
    2. ``ollama pull cyberwald/llama-3.1-sauerkrautlm-8b-instruct``\
    3. ``ollama pull hf.co/TheBloke/leo-hessianai-13B-chat-GGUF:latest``\
    4. ``ollama pull hf.co/TheBloke/DiscoLM_German_7b_v1-GGUF``\
    5. ``ollama pull mistral``\
    6. ``ollama run <LLM>`` (für direkte Kommunikation im Terminal)\

-starte Ollama Server: ``ollama serve`` (Beenden mit Task Manager)\
-Installiere Langchain Ollama: ``pip install -U langchain-ollama``\

-Intalliere DeepEval: ``pip install -U deepeval"``

-Installiere Open WebUI mit Docker: ``docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main``

-Installiere Google AI: ``pip install -q -U google-generativeai``\
-Installiere Langchain Google AI: ``pip install -q -U langchain-google-genai``

-Installiere pyperclip: ``pip install pyperclip``

-Installiere Pinecone: ``pip install pinecone``\
-Installiere Langchain Pinecone: ``pip install -qU langchain-pinecone pinecone-notebooks``

-Installiere MAUVE: ``pip install mauve-text``

___

Hier ist eine kurze Erklärung der Branches:

basic_display: Dazu da, um einfache Prompts ohne RAG per REST Request vom Frontend an Backend zu schicken, und Antwort zurückzubekommen, die im Frontend angezeigt wird.

basic_rag: Dazu da, um Pinecone Vektor DB zu initialisieren. Nach der (einmaligen) Initialisierung können per REST Request Prompts mit RAG vom Frontend an Backend geschickt und eine Antwort zurückbekommen werden, die im Frontend angezeigt wird.

with_results_and_tests: Dazu da, um Frage-Antwort Paare von LLMs zu speichern und Tests mit DeepEval und anderen Benchmarks durchzuführen.

main: aktuell auf gleichem Entwicklungsstand wie basic_rag; with_results_and_tests ohne 'results' und 'tests' Verzeichnisse.

___
___

EN:

This program was written as part of the bachelor thesis "Researching the measurable quality of LLM responses in different languages" in the subject of Business Information Systems by Burak Can Demirtas at the Hochschule Karlsruhe im the 2024/2025 winter semester.

It is a reusable and extendable application for testing the linguistic quality of LLM-generated answers.

___

Here is a documentation of every executed step.

Steps:

1. create directory "llm_translation_compare" in any folder

2. change into created directory

3. create virtual environment with ``python -m venv .venv``
   1. "python" --> the program Python shall be executed (On the precondition, that Python is already installed on the computer and written into the path variable "Path" in the system environment variables)
   2. "-m" --> calls a module as a script
   3. "venv" --> Access to module venv, which normally comes preinstalled with Python
   4. ".venv" --> creates virtual environment in new directory .venv (name can be chosen freely, but .venv ist a convention)

4. activate virtual environment
   1. Windows PowerShell --> ``.venv\Scripts\Activate.ps1``
   2. Windows Bash --> ``source .venv/Scripts/activate``
   3. macOS, Linux --> ``source .venv/bin/activate``

5. create .gitignore for .venv with ``echo "*" > .venv/.gitignore``

6. install Python Web Framework FastAPI with ``pip install "fastapi[standard]"``

7. install the following extensions for FastAPI:
   1. ``pip install "uvicorn[standard]"``
   2. ``pip install python-multipart sqlalchemy jinja2``
   3. ``pip install pydantic``
   4. ``pip install langchain_community``
   5. ``pip install langchain_openai``

8. open new shell in folder "llm_translation_compare"

9. install React Frontend Framework Vite with ``npm create vite frontend --template react-ts`` (Vorausgesetzt Node.js und NPM sind schon auf dem Rechner installiert und in die Pfadvariable "Path" in den Systemumgebungsvariablen gesetzt)

10. execute ``npm install``

11. install the following extensions for React:
    1. ``npm install @mui/material @emotion/react @emotion/styled``
    2. ``npm install axios``

12. start frontend application with ``npm run dev``

13. start backend application with ``uvicorn app:app --reload``
    1. "app" hinter dem Doppelpunkt steht für die Datei "app.py"
    2. "app" nach dem Doppelpunkt steht für die Instanz "app" in der Datei "app.py"

Continuation:

-install OllamaSetup\
-go to installation directory and open Terminal or Powershell\
-Download and run any LLM on Ollama:\
    1. ``ollama pull llama3.2``\
    2. ``ollama pull cyberwald/llama-3.1-sauerkrautlm-8b-instruct``\
    3. ``ollama pull hf.co/TheBloke/leo-hessianai-13B-chat-GGUF:latest``\
    4. ``ollama pull hf.co/TheBloke/DiscoLM_German_7b_v1-GGUF``\
    5. ``ollama pull mistral``\
    6. ``ollama run <LLM>`` (for direct communication in Terminal)\

-start Ollama Server: ``ollama serve`` (end with Task Manager)\
-install Langchain Ollama: ``pip install -U langchain-ollama``\

-install DeepEval: ``pip install -U deepeval"``

-install Open WebUI with Docker: ``docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main``

-install Google AI: ``pip install -q -U google-generativeai``\
-install Langchain Google AI: ``pip install -q -U langchain-google-genai``

-install pyperclip: ``pip install pyperclip``

-install Pinecone: ``pip install pinecone``\
-install Langchain Pinecone: ``pip install -qU langchain-pinecone pinecone-notebooks``

-install MAUVE: ``pip install mauve-text``

___

Here is a brief overview of the branches:

basic_display: there to send simple prompts without RAG from frontend to backend per REST request and have an answer returned which will be displayed in the frontend.

basic_rag: there to initialize Pinecone vector DB. After a (singular) initialization, prompts with RAG can be sent from frontend to backend per REST request and have an answer returned which will be displayed in the frontend.

with_results_and_tests: there to save question-answer pairs of LLMs and conduct tests with DeepEval and other benchmarks.

main: currently on the same level of development as basic_rag; with_results_and_tests without 'results' and 'tests' directories.
