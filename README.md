# 🚗 QMB Fahrschul-Trainer (DIN EN ISO 9001:2015 & ISO 19011)

> **Interaktive, serverlose Werkzeug-Sammlung im Fahrschulapp-Prinzip exklusiv für den Qualitätsmanagementbeauftragten (QMB - TÜV-Standard).**  
> *Ziel dieser Tools ist es, ein Gefühl für die Fragen des TÜVs zu bekommen und Release-Feedback zu verwalten. 100% Standalone Single-File HTML!*

---

![Version](https://img.shields.io/badge/Version-0.1.0--alpha.1-red.svg)
![Release Stage](https://img.shields.io/badge/Stage-Alpha_Pre--Release-orange.svg)
![Level](https://img.shields.io/badge/Level-QMB_T%C3%9CV-blue.svg)
![Standard](https://img.shields.io/badge/ISO-9001%3A2015-green.svg)
![Auditing](https://img.shields.io/badge/DIN_EN_ISO-19011-purple.svg)
![Offline](https://img.shields.io/badge/Offline-100%25-brightgreen.svg)

---

> 🎵 **Wichtiger ISO 9001 Leitsatz (RickRoll Edition)**:
> *"Never gonna give you up, never gonna let you down... never gonna run around and fail your TÜV audit!"* 🕺✨  
> [Geheimer TÜV-Zertifizierungs-Link 📜](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

---

## 🛠️ Standalone HTML-Werkzeuge im Projekt

Dieses Repository enthält zwei vollkommen eigenständige, doppelklickbare HTML-Dateien:

1. 🚗 **`qmb_fahrschul_app.html`** *(oder `index.html`)*:
   - Der interaktive QMB Spaced-Repetition Lern-Trainer (Fahrschulapp-Prinzip).
   - TÜV-Prüfungssimulation (10 Fragen / 10 Min).
   - Kombiniertes Sachwörterbuch (QMF & QMB) mit Industrie-Beispielen.
   - Farblicher Abweichungs-Indikator & kondensiertes ISO-Debatten-Modal.

2. 🐛 **`qmb_issue_tracker.html`**:
   - Eigenständiger **Fehlerberichte- & Release-Feedback-Manager**.
   - Formular zur Erfassung von Bugs, Tippfehlern & unklaren ISO-Klauseln.
   - Liste aller eingereichten Berichte mit Status (`🔴 Offen` / `🟢 Behoben`).
   - JSON-Export & Import-Funktion zum Zusammenführen von Feedback aus der Schulklasse.

---

## 📌 Versionshinweis (`v0.1.0-alpha.1`)

Dies ist eine **Alpha-Entwicklungsversion (Pre-Release)**. Vor dem finalen v1.0.0-Release folgen kleinere Ergänzungen (*Minor Changes*) und Feinschliff anhand des Feedbacks aus der Schulklasse.

---

## 🎨 Interaktiver Abweichungs-Indikator & ISO-Debatte

Auf jeder Fragenkarte befindet sich ein **farblich codierter Abweichungs-Indikator**:

- 🟢 **`🟢 Bild & Norm konform (100% Übereinstimmung)`**: 100% Übereinstimmung zwischen Aufgabenbild/Rohentwurf und ISO-Norm.
- 🔴 **`⚠️ Norm-Abweichung im Bild-Entwurf (Klicken für Debatte 💬)`**: Hebt Fragen hervor, bei denen Rohentwürfe aus den Unterlagen von der ISO 9001:2015 abweichen.

### 💬 Die kondensierte ISO-Debatte (Gegenüberstellung auf Klick)
Bei Klick auf das rote Abweichungsfeld öffnet sich ein hochmodernes **Debatten-Modal**, das die beiden Sichtweisen auf den Punkt genau gegenüberstellt:

```
┌──────────────────────────────────────────────┬──────────────────────────────────────────────┐
│ 📝 Bild / Rohentwurf (Ursprung):             │ 📜 ISO 9001 Norm-Schlussfolgerung:           │
├──────────────────────────────────────────────┼──────────────────────────────────────────────┤
│ Entwurf behauptete: CE-Kennzeichen befreit   │ BGB § 823 & ISO Abs. 8.5.5 Klarstellung:     │
│ den Hersteller vollständig von der Haftung.  │ CE-Zeichen ist nur Konformitätserklärung,    │
│                                              │ befreit aber keinesfalls von Haftung.        │
└──────────────────────────────────────────────┴──────────────────────────────────────────────┘
```

---

## ⚡ Das Fahrschulapp-Lernprinzip (Spaced Repetition)

Das System nutzt einen intelligenten Stapel-Algorithmus zur optimalen Prüfungsvorbereitung:

```
                  ┌────────────────────────┐
                  │   Aktueller QMB-Stapel │
                  └───────────┬────────────┘
                              │
                    Beantworte Frage
                              │
             ┌────────────────┴────────────────┐
             ▼                                 ▼
    [ Richtig beantwortet ]           [ Falsch beantwortet ]
             │                                 │
             ▼                                 ▼
   Wandert NACH UNTEN in             Wird 2 Plätze weiter VORNE
   den gemasterten Stapel!           wieder NEU NEUGEMISCHT!
```

---

## 📖 Sachwörterbuch (QMF & QMB Begriffssammlung + Industrie-Beispiele)

Das integrierte Sachwörterbuch umfasst beide Ausbildungsstufen – jeweils mit anschaulichen Beispielen aus der Fertigung:

- **⚙️ Qualität**: *Beispiel*: Drehen eines Stahlbolzens mit Toleranz ±0,02 mm.
- **🔌 Poka Yoke**: *Beispiel*: Führungsnase am Schaltschrank-Stecker (physikalisch unmöglich falsch einzustecken).
- **🛠️ Korrektur vs. Korrekturmaßnahme**: *Beispiel*: Rohr nachdrehen (Korrektur) vs. Führungsschiene mit Drehmomentsicherung verbauen (Korrekturmaßnahme).
- **🚛 Extern bereitgestellte Prozesse**: *Beispiel*: Lohngalvanik für Verzinken auditieren.
- **⚖️ Produkthaftung**: *Beispiel*: Akkubrand beschädigt Lagerhalle – Gefährdungshaftung nach ProdHaftG.

---

## 🚀 Schnellstart

1. Öffne **`qmb_fahrschul_app.html`** per Doppelklick zum Lernen.
2. Öffne **`qmb_issue_tracker.html`** per Doppelklick zum Melden & Verwalten von Release-Feedback.

> [!WARNING]
> Verlasst euch nicht zu sehr auf das Sachwörterbuch (dies ist auch eher etwas für die mit mutiertem DAT-Protein), da in der Prüfung das Wissen über die Lokation der Textpassagen von essentieller Wichtigkeit sind!



Quotes:

„Arguing that you don't care about the right to privacy because you have nothing to hide is no different than saying you don't care about free speech because you have nothing to say.“

„Be curious. Read widely. Try new things. What people call intelligence just boils down to curiosity.“

„Privacy is a necessity. Freedom of speech is a necessity. The ability to speak without being watched is a necessity.“


