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
    2. ``ollama run llama3.2`` (für direkte Kommunikation im Terminal)\
-starte Ollama Server: ``ollama serve`` (Beenden mit Task Manager)\
-Installiere Langchain Ollama: ``pip install -U langchain-ollama``\

-Intalliere DeepEval: ``pip install -U deepeval"``
