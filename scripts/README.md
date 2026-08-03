# 🔄 Sync Issues to Folder (`sync_issues_to_folder.py`)

> **Automatischer Synchronisations-Helper (v0.1.0-alpha.1), um alle von Mitschülern auf GitHub eingereichten Fehlerberichte & Issues direkt als lokale Markdown-Dateien in den Ordner `reports/` herunterzuladen.**

---

![Version](https://img.shields.io/badge/Version-0.1.0--alpha.1-red.svg)

---

## 🛠️ Funktionsweise

Der Standalone Issue Tracker (`qmb_issue_tracker.html`) ermöglicht es Mitschülern über ihre eindeutige Client-ID, Fehlerberichte mit 1 Klick ins GitHub-Projekt einzureichen. 

Das Skript `sync_issues_to_folder.py` rufst du als Projektleiter lokal auf. Es fragt die GitHub-API deines Repositories (`FTPUllrich/qmb-fahrschul-app`) ab und speichert jeden Bericht als einzelne, übersichtliche Markdown-Datei im Ordner `reports/` ab.

---

## 🚀 Verwendung / Befehl ausführen

Öffne dein Terminal im Hauptverzeichnis des Projekts und führe folgenden Befehl aus:

```bash
python3 scripts/sync_issues_to_folder.py
```

### 📤 Beispiel-Ausgabe im Terminal:
```
[SYNC] Found 3 issues on GitHub.
  [SAVED] /home/ole/Projects/qmb-fahrschul-app/reports/issue_1.md
  [SAVED] /home/ole/Projects/qmb-fahrschul-app/reports/issue_2.md
  [SAVED] /home/ole/Projects/qmb-fahrschul-app/reports/issue_3.md
```

---

## 📁 Zielordner & Dateistruktur

Die heruntergeladenen Berichte landen automatisch im Ordner `reports/`:

```
qmb-fahrschul-app/
├── reports/
│   ├── issue_1.md   <-- Fehlerbericht von Mitschüler A
│   ├── issue_2.md   <-- Fehlerbericht von Mitschüler B
│   └── ...
└── scripts/
    ├── build_standalone_app.py
    ├── build_issue_tracker.py
    ├── sync_issues_to_folder.py
    └── README.md
```

---

## 📄 Aufbau einer generierten Markdown-Datei (`issue_X.md`)

```markdown
# Issue #1: [🐛 Bug / Darstellungsfehler] QMB-Stapel (von Stephan)

- **State**: OPEN
- **Created**: 2026-08-03T16:25:00Z
- **URL**: https://github.com/FTPUllrich/qmb-fahrschul-app/issues/1

## Details
### 🐛 QMB Release Fehlerbericht
* **Client-ID**: `client-8f3a9b2c`
* **Autor**: Stephan
* **Typ**: 🐛 Bug / Darstellungsfehler
* **Bereich**: QMB-Stapel (Fragenkatalog)

### 📝 Problembeschreibung
Bei Frage qmb-102 wird der Hunde-Modus Hinweis doppelt gerendert.
```
