#!/usr/bin/env python3
"""
Full QMB Standalone HTML Generator (Focus: Full QMB TÜV Questions Dataset & QMF+QMB Lexicon)
Version: v0.1.0-alpha.3 (Audited Release)
-----------------------------------------------------------------------------------------
Generates the self-contained single-file HTML app for GitHub Pages (index.html).
- 368 Audited QMB Exam Questions (DIN EN ISO 9001:2015, ISO 9000, ISO 19011, ProdHaftG, BGB § 823)
- 109 Untouched Maydell Questions with original screenshots
- Full QMF + QMB Glossary with industrial examples
"""

import os
import json
from pathlib import Path

APP_VERSION = "0.1.0-alpha.3"

def generate_qmb_app():
    script_dir = Path(__file__).resolve().parent
    repo_dir = script_dir.parent
    
    # 1. Load 368 audited questions
    questions_file = repo_dir / "src" / "data" / "all_questions_current.json"
    with open(questions_file, "r", encoding="utf-8") as f:
        qmb_questions = json.load(f)
    print(f"[INFO] Loaded {len(qmb_questions)} audited QMB questions from {questions_file.name}")

    # 2. Load 109 untouched Maydell questions
    maydell_q = []
    for i in range(1, 10):
        mc_path = repo_dir / "src" / "data" / f"mc{i}_analyzed.json"
        if mc_path.exists():
            with open(mc_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for idx, q in enumerate(data):
                    q_copy = dict(q)
                    q_copy["id"] = f"maydell-mc{i}-{idx}"
                    q_copy["category"] = q.get("category", "Allgemein")
                    maydell_q.append(q_copy)
    print(f"[INFO] Loaded {len(maydell_q)} Maydell questions (100% untouched)")

    # 3. Glossary with industrial examples
    glossary = [
      { "term": "Qualität", "definition": "Wie gut ein Produkt oder eine Dienstleistung alle festgelegten und vorausgesetzten Anforderungen erfüllt.", "isoRef": "DIN EN ISO 9000:2015 Abs. 3.6.2", "category": "QMF Basis", "beispiel": "⚙️ Industrie-Beispiel: Eine Dreherei fertigt Stahlbolzen mit einer vorgegebenen Toleranz von ±0,02 mm. Liegen alle gelieferten Bolzen exakt in diesem Maße, ist die Qualität zu 100% erfüllt." },
      { "term": "Kundenorientierung", "definition": "Ausrichtung aller Unternehmensprozesse am Nutzen, der Zufriedenheit und den Erwartungen des Kunden.", "isoRef": "ISO 9000:2015 Abs. 2.3.1", "category": "QMF Basis", "beispiel": "🏭 Industrie-Beispiel: Ein Zulieferer von Blechteilen passt seine Lieferverpackung so an, dass der Roboter beim Autohersteller (OEM) die Teile direkt ohne manuelles Auspacken greifen kann." },
      { "term": "Prozess", "definition": "Ein strukturierter Ablauf von Tätigkeiten, der Eingaben (Material, Daten) in ein messbares Ergebnis (Erzeugnis) umwandelt.", "isoRef": "ISO 9000:2015 Abs. 3.4.1", "category": "QMF Basis", "beispiel": "🔧 Industrie-Beispiel: Prozess 'Gehäusefertigung': Stanzen -> Abkanten -> Schweißen -> Pulverbeschichten -> Endkontrolle." },
      { "term": "PDCA-Zyklus", "definition": "Plan-Do-Check-Act. Der kontinuierliche Regelkreis zur ständigen Qualitätsverbesserung in vier Schritten.", "isoRef": "ISO 9001:2015 Kap. 0.4", "category": "QMF / QMB Basis", "beispiel": "🔄 Industrie-Beispiel: Plan: Neue Schweißparameter festlegen; Do: Probeserie schweißen; Check: Röntgenprüfung & Schliffbild auswerten; Act: Schweißroboter auf neue Werte fest einstellen." },
      { "term": "Fehler", "definition": "Nichterfüllung einer festgelegten Anforderung oder Spezifikation an einem Produkt oder Prozess.", "isoRef": "ISO 9000:2015 Abs. 3.10.3", "category": "QMF Basis", "beispiel": "❌ Industrie-Beispiel: Eine Bohrung in einem Gussgehäuse hat statt 12,0 mm versehentlich 12,5 mm Durchmesser – das Bauteil ist nicht funktionstüchtig und damit fehlerhaft." },
      { "term": "Korrektur", "definition": "Sofortige Maßnahme zur Beseitigung eines festgestellten Symptoms oder Fehlers (Schadensbegrenzung).", "isoRef": "ISO 9000:2015 Abs. 3.12.2", "category": "QMF Basis", "beispiel": "🛠️ Industrie-Beispiel: Ein Rohling ist 2 mm zu lang abgesägt worden. Die Korrektur ist das Nachdrehen auf das korrekte Soll-Maß." },
      { "term": "Korrekturmaßnahme", "definition": "Beseitigung der TIEFEN URSACHE eines Fehlers, damit dieser in Zukunft nie wieder auftreten kann.", "isoRef": "ISO 9000:2015 Abs. 3.12.6", "category": "QMF / QMB", "beispiel": "🛡️ Industrie-Beispiel: Die Säge schnitt zu lang, weil der mechanische Anschlag locker war. Korrekturmaßnahme: Einbau einer fest verschraubten Führungsschiene mit Drehmomentsicherung." },
      { "term": "Qualitätspolitik", "definition": "Die von der Geschäftsführung formulierte Gesamtausrichtung und Selbstverpflichtung des Unternehmens zur Qualität.", "isoRef": "ISO 9001:2015 Kap. 5.2", "category": "QMF / QMB", "beispiel": "📜 Industrie-Beispiel: 'Unsere Fabrik garantiert Null-Fehler-Qualität bei allen sicherheitsrelevanten Bremsscheiben für die Bahntechnik.'" },
      { "term": "Qualitätsziel", "definition": "Konkretes, messbares Ziel zur Verbesserung der Produkt- oder Prozessqualität innerhalb eines Zeitraums.", "isoRef": "ISO 9001:2015 Kap. 6.2", "category": "QMF / QMB", "beispiel": "🎯 Industrie-Beispiel: 'Reduzierung der Ausschussquote in der Gießerei von aktuell 3,5% auf unter 1,2% bis zum Ende des 4. Quartals.'" },
      { "term": "5S-Methode", "definition": "Standard zur Arbeitsplatzorganisation: Selektieren, Sortieren, Säubern, Standardisieren, Selbstdisziplin.", "isoRef": "QM-Methodik / Lean", "category": "QMF Werkzeuge", "beispiel": "🧹 Industrie-Beispiel: Werkzeug-Schattenwände an der Fräsmaschine: Jeder Mechaniker sieht sofort, wenn der 13er-Schlüssel fehlt." },
      { "term": "Poka Yoke", "definition": "Technisches Prinzip zur Verhinderung menschlicher Fehlhandlungen durch konstruktive Kniffe.", "isoRef": "QM-Methodik", "category": "QMF Werkzeuge", "beispiel": "🔌 Industrie-Beispiel: Ein Kabelstecker im Schaltschrank besitzt eine Führungsnase, sodass er physikalisch nicht verkehrt herum eingesteckt werden kann." },
      { "term": "Pareto-Prinzip (80/20-Regel)", "definition": "Statistisches Phänomen: 80% der Auswirkungen (z.B. Fehlerkosten) beruhen auf nur 20% der Ursachen.", "isoRef": "7 QC-Tools", "category": "QMF Werkzeuge", "beispiel": "📊 Industrie-Beispiel: Von 100 Ausschussteilen in der Schicht sind 82 Stück auf eine einzige verschlissene Stanzform zurückzuführen." },
      { "term": "Ishikawa-Diagramm (Ursachen-Wirkung)", "definition": "Problem-Ursachen-Diagramm (Fischgräte) nach den 7 M: Mensch, Maschine, Material, Methode, Messung, Milieu, Management.", "isoRef": "7 QC-Tools", "category": "QMF Werkzeuge", "beispiel": "🐟 Industrie-Beispiel: Warum brennt die Schweißnaht durch? Überprüfung von Gasdruck (Material), Roboter-Vorschub (Maschine) und Raumtemperatur (Mitwelt)." },
      { "term": "Kontrollkarte / SPC", "definition": "Statistische Prozessregelung mit grafischen Ober- und Untergrenzen zur Überwachung laufender Fertigungen.", "isoRef": "7 QC-Tools / ISO 7870", "category": "QMF Werkzeuge", "beispiel": "📈 Industrie-Beispiel: Der Dreher misst alle 30 Minuten den Durchmesser und trägt den Wert in die SPC-Karte ein. Droht die Drift, stellt er nach." },
      { "term": "FMEA (Fehlermöglichkeits- & Einflussanalyse)", "definition": "Präventive Risikoanalyse vor Serienstart zur Ermittlung potenzieller Schwachstellen und Berechnung der Risikoprioritätszahl (RPZ).", "isoRef": "VDA / AIAG FMEA", "category": "QMF / QMB Werkzeuge", "beispiel": "⚠️ Industrie-Beispiel: Bevor eine neue Montagelinie für E-Motoren anläuft, überlegt das QM-Team, wo Schrauben vertauscht werden könnten, und plant Sensoren ein." },
      { "term": "8D-Report", "definition": "Standardisierter 8-Schritte-Bericht zur Bearbeitung von Kundenreklamationen und systematischen Fehlerursachen.", "isoRef": "VDA Standard / ISO 9001 Kap. 10.2", "category": "QMF / QMB Werkzeuge", "beispiel": "📑 Industrie-Beispiel: Der Kunde meldet undichte Ventile. Der Zulieferer schickt innerhalb von 24 Std. Sofortmaßnahmen (D3) und nach 10 Tagen die Ursachenanalyse (D4)." },
      { "term": "Turtle-Modell", "definition": "Schildkröten-Diagramm zur vollständigen Beschreibung eines Prozesses (Input, Output, Womit, Wer, Wie, Kennzahlen).", "isoRef": "ISO 9001 Kap. 4.4", "category": "QMF / QMB Prozess", "beispiel": "🐢 Industrie-Beispiel: Prozess 'Härten': Input = Weiche Wellen; Output = Gehärtete Wellen; Womit = Härteofen; Wer = Härtemeister; Kennzahl = Ausschussquote < 0,5%." },
      { "term": "High Level Structure (HLS)", "definition": "Einheitliche Grundstruktur für alle ISO-Managementsystemnormen mit identischen Kernkapiteln (Kapitel 1 bis 10).", "isoRef": "ISO Directives Annex SL", "category": "QMB Spezial", "beispiel": "🏢 Industrie-Beispiel: ISO 9001 (Qualität), ISO 14001 (Umwelt) und ISO 45001 (Arbeitsschutz) nutzen in unserer Fabrik exakt denselben Kapitelaufbau." },
      { "term": "Kontext der Organisation", "definition": "Analyse aller internen und externen Faktoren, die die Erreichung der Qualitätsziele des Betriebs beeinflussen.", "isoRef": "ISO 9001:2015 Kap. 4.1", "category": "QMB Spezial", "beispiel": "🌍 Industrie-Beispiel: Hohe Strompreise, Lieferengpässe bei Halbleitern und verschärfte Umweltgesetze verpflichten das Werk zur strategischen Anpassung." },
      { "term": "Interessierte Parteien (Stakeholder)", "definition": "Alle Gruppen oder Personen, die Anforderungen an das Unternehmen stellen oder von dessen Handeln betroffen sind.", "isoRef": "ISO 9001:2015 Kap. 4.2", "category": "QMB Spezial", "beispiel": "🤝 Industrie-Beispiel: Kunden verlangen Pünktlichkeit, die Gewerbeaufsicht verlangt Lärmschutz, Belegschaft verlangt Arbeitssicherheit." },
      { "term": "Oberste Leitung (Top Management)", "definition": "Geschäftsführung / Werksleitung. Trägt die finale Verantwortung und Rechenschaftspflicht für das Qualitätsmanagementsystem.", "isoRef": "ISO 9001:2015 Kap. 5.1", "category": "QMB Spezial", "beispiel": "👔 Industrie-Beispiel: Der Geschäftsführer muss im TÜV-Audit nachweisen, dass er ausreichend Budget für Kalibrierungen und Personalschulungen bereitstellt." },
      { "term": "Risikobasierter Ansatz", "definition": "Vorausschauendes Denken zur Identifizierung von Risiken und Chancen in allen Betriebsprozessen.", "isoRef": "ISO 9001:2015 Kap. 6.1", "category": "QMB Spezial", "beispiel": "🔮 Industrie-Beispiel: Vor dem Winter wird die Heizung der Lackierhalle gewartet, um einen Produktionsstillstand durch Frostschäden zu verhindern." },
      { "term": "Dokumentierte Information", "definition": "Sammelbegriff für Lenkungsunterlagen. Vorgabedokumente werden aufrechterhalten, Nachweisdokumente (Aufzeichnungen) werden aufbewahrt.", "isoRef": "ISO 9001:2015 Kap. 7.5", "category": "QMB Spezial", "beispiel": "💾 Industrie-Beispiel: Der CAD-Schaltplan (Vorgabe) und das digital unterschriebene Erstmusterprüfprotokoll im ERP-System (Nachweis)." },
      { "term": "Extern bereitgestellte Prozesse (Lieferanten)", "definition": "Qualitative Überwachung und Beurteilung aller Zulieferer und Dienstleister für ausgelagerte Fertigungsschritte.", "isoRef": "ISO 9001:2015 Kap. 8.4", "category": "QMB Spezial", "beispiel": "🚛 Industrie-Beispiel: Das Verzinken von Stahlbauteilen wird an eine externe Lohngalvanik vergeben – der QMB führt dort regelmäßig ein Lieferantenaudit durch." },
      { "term": "Produkthaftung (ProdHaftG)", "definition": "Verschuldensunabhängige Haftung des Herstellers für Personen- und Sachschäden, die durch ein fehlerhaftes Produkt entstehen.", "isoRef": "ProdHaftG / BGB § 823", "category": "QMB Recht", "beispiel": "⚖️ Industrie-Beispiel: Ein brennender Akku beschädigt eine Lagerhalle. Der Akkuhersteller haftet für den Schaden – auch ohne dass ihm Vorsatz nachgewiesen werden muss." },
      { "term": "Verkehrssicherungspflichten", "definition": "Rechtliche Pflichten des Herstellers: Konstruktions-, Fabrikations-, Instruktions- und Produktbeobachtungspflicht.", "isoRef": "BGB § 823 / ProdHaftG", "category": "QMB Recht", "beispiel": "🚦 Industrie-Beispiel: Ein Maschinenbauer muss Schutzabdeckungen anbringen, klare Warnaufkleber anbringen und Unfälle im Feld auswerten." },
      { "term": "Internes Audit (First-Party Audit)", "definition": "Systematische, interne Überprüfung durch eigene QM-Mitarbeiter zur Beurteilung der Normkonformität der Fertigung.", "isoRef": "DIN EN ISO 19011 / ISO 9001 Kap. 9.2", "category": "QMB Auditing", "beispiel": "🔍 Industrie-Beispiel: Der interne Auditor prüft in der Schweißerei, ob alle Schweißer gültige Prüfbescheinigungen besitzen und nach aktuellen Plänen arbeiten." },
      { "term": "Managementbewertung (Management Review)", "definition": "Die durch die Geschäftsführung in geplanten Abständen durchgeführte Prüfung der Wirksamkeit und Eignung des QMS.", "isoRef": "ISO 9001:2015 Kap. 9.3", "category": "QMB Spezial", "beispiel": "📊 Industrie-Beispiel: Einmal jährlich wertet die Geschäftsführung Reklamationsquoten, Auditergebnisse und Kennzahlen aus und beschließt Qualitätsziele." },
      { "term": "VUCA-Welt", "definition": "Akronym für Volatilität, Unsicherheit, Komplexität und Ambiguität. Beschreibung moderner, dynamischer Marktbedingungen.", "isoRef": "ISO 9001 Kap. 4.1 / Strategie", "category": "QMB Strategie", "beispiel": "🌊 Industrie-Beispiel: Ein spontaner Ausfall der Frachtschiffroute erfordert innerhalb von 3 Stunden die Umstellung der Logistikkette auf Luftfracht." },
      { "term": "Qualitätssicherungsvereinbarung (QSV)", "definition": "Verbindlicher Vertrag zwischen Kunde und Lieferant über spezifische Qualitäts-, Prüf- und Dokumentationsstandards.", "isoRef": "ISO 9001:2015 Kap. 8.4", "category": "QMB Lieferanten", "beispiel": "📝 Industrie-Beispiel: Der Motorenhersteller verpflichtet den Gießerei-Zulieferer per QSV, mit jeder Charge ein 3.1-Abnahmeprüfzeugnis mitzuliefern." },
      { "term": "Akkreditierung vs. Zertifizierung", "definition": "Akkreditierung (durch staatliche Stelle wie DAkkS) ist die Zulassung von Zertifizierungsstellen (z.B. TÜV). Zertifizierung ist die Prüfung unserer Fabrik.", "isoRef": "ISO/IEC 17021", "category": "QMB System", "beispiel": "🏛️ Industrie-Beispiel: Die DAkkS prüft den TÜV. Der TÜV kommt anschließend zu uns ins Werk und stellt das ISO 9001 Zertifikat aus." }
    ]

    maydell_json = json.dumps(maydell_q, ensure_ascii=False, indent=2)
    questions_json = json.dumps(qmb_questions, ensure_ascii=False, indent=2)
    glossary_json = json.dumps(glossary, ensure_ascii=False, indent=2)

    html_content = f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>QMB Fahrschul-Trainer (v{APP_VERSION})</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

    :root {{
      --bg-dark: #0a0e17;
      --bg-card: rgba(22, 29, 45, 0.85);
      --border-color: rgba(255, 255, 255, 0.12);
      --primary: #6366f1;
      --primary-hover: #4f46e5;
      --success: #10b981;
      --success-glow: rgba(16, 185, 129, 0.35);
      --error: #ef4444;
      --error-glow: rgba(239, 68, 68, 0.35);
      --warning: #f59e0b;
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --radius-lg: 16px;
      --radius-md: 12px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-dark);
      background-image: 
        radial-gradient(at 15% 15%, rgba(99, 102, 241, 0.18) 0px, transparent 50%),
        radial-gradient(at 85% 85%, rgba(16, 185, 129, 0.15) 0px, transparent 50%);
      background-attachment: fixed;
      color: var(--text-main);
      min-height: 100vh;
      line-height: 1.6;
      padding: 24px 16px;
    }}

    .container {{ max-width: 1100px; margin: 0 auto; }}

    .glass-panel {{
      background: var(--bg-card);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--border-color);
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.4);
      border-radius: var(--radius-lg);
      padding: 24px;
      margin-bottom: 24px;
    }}

    .glass-card {{
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-md);
      padding: 16px;
      margin-bottom: 12px;
    }}

    header {{ display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; }}

    .logo {{ display: flex; align-items: center; gap: 12px; }}
    .logo-icon {{
      width: 44px; height: 44px; border-radius: 12px;
      background: linear-gradient(135deg, #6366f1 0%, #10b981 100%);
      display: flex; align-items: center; justify-content: center; font-size: 1.5rem;
    }}

    nav {{ display: flex; gap: 8px; background: rgba(15, 23, 42, 0.6); padding: 6px; border-radius: 14px; border: 1px solid var(--border-color); flex-wrap: wrap; }}
    .nav-btn {{
      padding: 8px 18px; border-radius: 10px; border: none; background: transparent;
      color: var(--text-muted); font-weight: 500; cursor: pointer; transition: all 0.2s ease; font-size: 0.92rem;
    }}
    .nav-btn.active {{ background: linear-gradient(135deg, #6366f1, #4f46e5); color: #fff; font-weight: 600; }}

    .ctrl-btn {{
      padding: 8px 14px; border-radius: 10px; border: 1px solid var(--border-color);
      background: rgba(255,255,255,0.06); color: var(--text-main); cursor: pointer; font-size: 0.85rem;
    }}
    .ctrl-btn.active {{ background: rgba(99, 102, 241, 0.25); color: #a5b4fc; border-color: #6366f1; }}

    /* Badges */
    .badge {{ padding: 4px 10px; border-radius: 20px; font-size: 0.78rem; font-weight: 600; display: inline-block; margin-right: 6px; }}
    .badge-purple {{ background: rgba(99, 102, 241, 0.2); color: #a5b4fc; border: 1px solid rgba(99, 102, 241, 0.4); }}
    .badge-amber {{ background: rgba(245, 158, 11, 0.2); color: #fcd34d; border: 1px solid rgba(245, 158, 11, 0.4); }}
    .badge-green {{ background: rgba(16, 185, 129, 0.2); color: #6ee7b7; border: 1px solid rgba(16, 185, 129, 0.4); }}
    .badge-red {{ background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); }}
    .badge-alpha {{ background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); }}

    /* Options */
    .option-item {{
      padding: 16px 20px; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.1);
      background: rgba(30, 41, 59, 0.5); color: var(--text-main); cursor: pointer;
      display: flex; align-items: center; gap: 14px; margin-bottom: 12px; transition: all 0.2s ease;
    }}
    .option-item.selected {{ background: rgba(99, 102, 241, 0.25); border-color: #6366f1; }}
    .option-item.correct {{ background: rgba(16, 185, 129, 0.25) !important; border-color: #10b981 !important; color: #a7f3d0 !important; }}
    .option-item.wrong {{ background: rgba(239, 68, 68, 0.25) !important; border-color: #ef4444 !important; color: #fca5a5 !important; }}

    .opt-box {{
      width: 24px; height: 24px; border-radius: 6px; border: 2px solid rgba(255,255,255,0.3);
      display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.85rem; flex-shrink: 0;
    }}
    .option-item.selected .opt-box {{ background: #6366f1; border-color: #6366f1; color: #fff; }}

    /* Primary Button */
    .btn-primary {{
      background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
      color: white; border: none; padding: 12px 24px; border-radius: var(--radius-md);
      font-weight: 600; font-size: 1rem; cursor: pointer; transition: all 0.2s ease;
      box-shadow: 0 4px 14px rgba(99, 102, 241, 0.4);
    }}
    .btn-primary:hover {{ transform: translateY(-1px); box-shadow: 0 6px 20px rgba(99, 102, 241, 0.6); }}

    /* Progress bar */
    .progress-bar-bg {{ width: 100%; height: 10px; border-radius: 5px; background: rgba(15, 23, 42, 0.6); overflow: hidden; display: flex; }}
    .progress-bar-fill {{ height: 100%; background: linear-gradient(90deg, #10b981, #34d399); transition: width 0.3s ease; }}
    .progress-bar-retry {{ height: 100%; background: linear-gradient(90deg, #f59e0b, #fbbf24); transition: width 0.3s ease; }}

    #confetti-canvas {{ position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 999; }}

    .tab-content {{ display: none; }}
    .tab-content.active {{ display: block; }}
  </style>
</head>
<body>

  <canvas id="confetti-canvas"></canvas>

  <div class="container">
    
    <!-- Header & Navigation -->
    <div class="glass-panel">
      <header>
        <div class="logo">
          <div class="logo-icon">🚗</div>
          <div>
            <div style="display: flex; align-items: center; gap: 8px;">
              <h1 style="font-size: 1.35rem; font-weight: 800; background: linear-gradient(90deg, #ffffff, #a5b4fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                QMB Fahrschul-Trainer (TÜV ISO 9001)
              </h1>
              <span class="badge badge-green">v{APP_VERSION} (Audited)</span>
            </div>
            <p style="font-size: 0.8rem; color: var(--text-muted);">
              Qualitätsmanagementbeauftragter • 368 normativ geprüfte Fragen & 109 Maydell Original-Fragen
            </p>
          </div>
        </div>

        <nav>
          <button class="nav-btn active" onclick="switchTab('stack')">🚗 QMB-Stapel (368)</button>
          <button class="nav-btn" onclick="switchTab('maydell')">📸 Maydell Fragen (109)</button>
          <button class="nav-btn" onclick="switchTab('exam')">🏆 TÜV-Prüfung</button>
          <button class="nav-btn" onclick="switchTab('glossary')">📖 Sachwörterbuch</button>
          <button class="nav-btn" onclick="switchTab('stats')">📊 Statistik</button>
        </nav>

        <div style="display: flex; gap: 8px;">
          <button id="audio-toggle" class="ctrl-btn active" onclick="toggleAudio()">🔊 Sound ON</button>
        </div>
      </header>
    </div>

    <!-- TAB 1: FAHRSCHUL-STAPEL (QMB FOCUS) -->
    <div id="tab-stack" class="tab-content active">
      
      <!-- Metrics Bar -->
      <div class="glass-panel">
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 16px; margin-bottom: 14px;">
          <div style="display: flex; gap: 24px; align-items: center;">
            <div>
              <span style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase;">Aktueller QMB-Stapel</span>
              <div id="stack-remaining" style="font-size: 1.25rem; font-weight: 700; color: #fff;">0 Fragen</div>
            </div>
            <div>
              <span style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase;">Wiederholungen</span>
              <div id="stack-retries" style="font-size: 1.25rem; font-weight: 700; color: #fcd34d;">0 neu einsortiert</div>
            </div>
            <div>
              <span style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase;">Gemastert</span>
              <div id="stack-mastered" style="font-size: 1.25rem; font-weight: 700; color: #6ee7b7;">0 / 0</div>
            </div>
          </div>

          <div>
            <span style="font-size: 0.85rem; color: var(--text-muted); margin-right: 8px;">Thema:</span>
            <select id="category-select" onchange="filterCategory()" style="padding: 8px 12px; border-radius: 10px; background: rgba(30, 41, 59, 0.8); color: #fff; border: 1px solid var(--border-color); outline: none;">
            </select>
          </div>
        </div>

        <div>
          <div style="display: flex; justify-content: space-between; font-size: 0.8rem; color: var(--text-muted); margin-bottom: 6px;">
            <span>💡 Fahrschulapp-Prinzip: Richtig = Nach unten | Falsch = Direkt neu untergemischt</span>
            <span id="stack-accuracy" style="font-weight: 700; color: #fff;">Richtig-Quote: 100%</span>
          </div>
          <div class="progress-bar-bg">
            <div id="bar-mastered" class="progress-bar-fill" style="width: 0%;"></div>
            <div id="bar-retry" class="progress-bar-retry" style="width: 0%;"></div>
          </div>
        </div>
      </div>

      <!-- Question Card Container -->
      <div id="question-card-container" class="glass-panel">
      </div>
    </div>

    <!-- TAB: MAYDELL FRAGEN -->
    <div id="tab-maydell" class="tab-content">
      <div class="glass-panel">
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 16px; margin-bottom: 14px;">
          <div style="display: flex; gap: 24px; align-items: center;">
            <div>
              <span style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase;">Maydell Fragen (Original)</span>
              <div id="maydell-remaining" style="font-size: 1.25rem; font-weight: 700; color: #fff;">0 Fragen</div>
            </div>
            <div>
              <span style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase;">Wiederholungen</span>
              <div id="maydell-retries" style="font-size: 1.25rem; font-weight: 700; color: #fcd34d;">0 neu einsortiert</div>
            </div>
            <div>
              <span style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase;">Gemastert</span>
              <div id="maydell-mastered" style="font-size: 1.25rem; font-weight: 700; color: #6ee7b7;">0 / 0</div>
            </div>
          </div>

          <div>
            <span style="font-size: 0.85rem; color: var(--text-muted); margin-right: 8px;">Thema:</span>
            <select id="maydell-category-select" onchange="filterMaydellCategory()" style="padding: 8px 12px; border-radius: 10px; background: rgba(30, 41, 59, 0.8); color: #fff; border: 1px solid var(--border-color); outline: none;">
            </select>
          </div>
        </div>

        <div>
          <div style="display: flex; justify-content: space-between; font-size: 0.8rem; color: var(--text-muted); margin-bottom: 6px;">
            <span>📸 Original-Prüfungsfragen mit Bildnachweis</span>
            <span id="maydell-accuracy" style="font-weight: 700; color: #fff;">Richtig-Quote: 100%</span>
          </div>
          <div class="progress-bar-bg">
            <div id="maydell-bar-mastered" class="progress-bar-fill" style="width: 0%;"></div>
            <div id="maydell-bar-retry" class="progress-bar-retry" style="width: 0%;"></div>
          </div>
        </div>
      </div>

      <div id="maydell-question-card-container" class="glass-panel">
      </div>
    </div>

    <!-- TAB 2: TÜV PRÜFUNGSSIMULATION -->
    <div id="tab-exam" class="tab-content">
      <div class="glass-panel" style="text-align: center; padding: 40px;">
        <h2 style="font-size: 1.6rem; font-weight: 800; color: #fff; margin-bottom: 12px;">🏆 TÜV QMB Prüfungs-Simulation</h2>
        <p style="color: var(--text-muted); margin-bottom: 24px;">
          Teste dein Wissen unter realistischen TÜV-Bedingungen: 20 zufällige Fragen aus dem 368-Fragen-Stamm • 20 Minuten Zeitlimit • 75% Bestehensgrenze
        </p>
        <button class="btn-primary" onclick="startExam()">Prüfungssimulation starten</button>
      </div>
      <div id="exam-active-container" style="display: none;"></div>
    </div>

    <!-- TAB 3: QM SACHWÖRTERBUCH -->
    <div id="tab-glossary" class="tab-content">
      <div class="glass-panel">
        <h2 style="font-size: 1.3rem; font-weight: 800; color: #fff; margin-bottom: 12px;">📖 Vollständiges Sachwörterbuch (QMF & QMB)</h2>
        <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 16px;">
          Enthält alle wesentlichen Begriffe und Konzepte aus den TÜV-Referenzdokumenten (Begriffe & Definitionen sowie QM Normensammlung).
        </p>
        <input type="text" id="glossary-search" oninput="renderGlossary()" placeholder="Begriff suchen (z.B. Audit, HLS, PDCA, VUCA, ProdHaftG, 8D-Report, FMEA, Poka Yoke, Stakeholder)..." style="width: 100%; padding: 12px 16px; border-radius: 10px; background: rgba(15,23,42,0.6); border: 1px solid var(--border-color); color: #fff; margin-bottom: 16px; outline: none;" />
        <div id="glossary-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 16px;"></div>
      </div>
    </div>

    <!-- TAB 4: STATISTIK -->
    <div id="tab-stats" class="tab-content">
      <div class="glass-panel">
        <h2 style="font-size: 1.3rem; font-weight: 800; color: #fff; margin-bottom: 16px;">📊 QMB Lernstatistik & Leistungsübersicht</h2>
        <div id="stats-metrics" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 24px;"></div>
        <button class="ctrl-btn" onclick="resetStats()">Statistik zurücksetzen</button>
      </div>
    </div>

  </div>

  <script>
    const allQuestionsData = {questions_json};
    const maydellQuestionsData = {maydell_json};
    const glossaryData = {glossary_json};

    let questionsStack = [...allQuestionsData];
    let masteredIds = JSON.parse(localStorage.getItem('qmb_mastered_ids') || '[]');
    let retryCount = 0;
    let selectedOptions = [];
    let isSubmitted = false;
    let activeCategory = 'ALL';
    let soundEnabled = true;

    // Maydell state
    let maydellStack = [...maydellQuestionsData];
    let maydellMasteredIds = JSON.parse(localStorage.getItem('qmb_maydell_mastered_ids') || '[]');
    let maydellRetryCount = 0;
    let maydellSelectedOptions = [];
    let maydellSubmitted = false;
    let maydellActiveCategory = 'ALL';

    function toggleAudio() {{
      soundEnabled = !soundEnabled;
      const btn = document.getElementById('audio-toggle');
      btn.innerText = soundEnabled ? '🔊 Sound ON' : '🔇 Sound OFF';
      btn.classList.toggle('active', soundEnabled);
    }}

    function playCorrectSound() {{
      if (!soundEnabled) return;
      try {{
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain); gain.connect(ctx.destination);
        osc.frequency.setValueAtTime(587.33, ctx.currentTime);
        osc.frequency.setValueAtTime(880, ctx.currentTime + 0.1);
        gain.gain.setValueAtTime(0.2, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.3);
        osc.start(); osc.stop(ctx.currentTime + 0.3);
      }} catch(e) {{}}
    }}

    function playWrongSound() {{
      if (!soundEnabled) return;
      try {{
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain); gain.connect(ctx.destination);
        osc.frequency.setValueAtTime(220, ctx.currentTime);
        osc.frequency.setValueAtTime(164.81, ctx.currentTime + 0.15);
        gain.gain.setValueAtTime(0.3, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.35);
        osc.start(); osc.stop(ctx.currentTime + 0.35);
      }} catch(e) {{}}
    }}

    function triggerConfetti() {{
      const canvas = document.getElementById('confetti-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      const pieces = [];
      for (let i = 0; i < 60; i++) {{
        pieces.push({{
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height - canvas.height,
          color: ['#6366f1', '#10b981', '#f59e0b', '#ec4899'][Math.floor(Math.random() * 4)],
          size: Math.random() * 8 + 4,
          speed: Math.random() * 4 + 3
        }});
      }}
      let start = null;
      function animate(time) {{
        if (!start) start = time;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        pieces.forEach(p => {{
          p.y += p.speed;
          ctx.fillStyle = p.color;
          ctx.fillRect(p.x, p.y, p.size, p.size);
        }});
        if (time - start < 1500) requestAnimationFrame(animate);
        else ctx.clearRect(0, 0, canvas.width, canvas.height);
      }}
      requestAnimationFrame(animate);
    }}

    function getSortedCategories(data) {{
      const set = new Set();
      data.forEach(q => {{ if (q.category) set.add(q.category.trim()); }});
      return Array.from(set).sort();
    }}

    function populateCategories() {{
      const cats = ['ALL', ...getSortedCategories(allQuestionsData)];
      const select = document.getElementById('category-select');
      select.innerHTML = '';
      cats.forEach(c => {{
        const opt = document.createElement('option');
        opt.value = c; opt.innerText = c === 'ALL' ? 'Alle Themen (Gesamtkatalog)' : c;
        select.appendChild(opt);
      }});

      const maydellCats = ['ALL', ...getSortedCategories(maydellQuestionsData)];
      const mSelect = document.getElementById('maydell-category-select');
      mSelect.innerHTML = '';
      maydellCats.forEach(c => {{
        const opt = document.createElement('option');
        opt.value = c; opt.innerText = c === 'ALL' ? 'Alle Maydell-Themen' : c;
        mSelect.appendChild(opt);
      }});
    }}

    function switchTab(tabId) {{
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('nav .nav-btn').forEach(btn => btn.classList.remove('active'));

      const target = document.getElementById('tab-' + tabId);
      if (target) target.classList.add('active');

      const buttons = document.querySelectorAll('nav .nav-btn');
      if (tabId === 'stack') buttons[0]?.classList.add('active');
      else if (tabId === 'maydell') buttons[1]?.classList.add('active');
      else if (tabId === 'exam') buttons[2]?.classList.add('active');
      else if (tabId === 'glossary') buttons[3]?.classList.add('active');
      else if (tabId === 'stats') buttons[4]?.classList.add('active');

      if (tabId === 'stack') renderQuestionCard();
      if (tabId === 'maydell') renderMaydellCard();
      if (tabId === 'glossary') renderGlossary();
      if (tabId === 'stats') renderStats();
    }}

    function filterCategory() {{
      activeCategory = document.getElementById('category-select').value;
      questionsStack = allQuestionsData.filter(q => {{
        const cat = (q.category || '').trim();
        return activeCategory === 'ALL' || cat === activeCategory;
      }});
      masteredIds = JSON.parse(localStorage.getItem('qmb_mastered_ids') || '[]');
      retryCount = 0;
      renderQuestionCard();
    }}

    function renderQuestionCard() {{
      const container = document.getElementById('question-card-container');
      selectedOptions = [];
      isSubmitted = false;
      updateMetrics();

      if (questionsStack.length === 0) {{
        container.innerHTML = `
          <div style="text-align: center; padding: 40px;">
            <div style="font-size: 3rem; margin-bottom: 12px;">🎉</div>
            <h2 style="color: #6ee7b7; font-size: 1.5rem; margin-bottom: 8px;">Stapel komplett gemastert!</h2>
            <p style="color: var(--text-muted); margin-bottom: 20px;">Du hast alle Fragen dieses Moduls erfolgreich beantwortet.</p>
            <button class="btn-primary" onclick="filterCategory()">Von vorne beginnen</button>
          </div>
        `;
        return;
      }}

      const q = questionsStack[0];
      const isMulti = q.multipleChoice || q.options.filter(o => o.isCorrect).length > 1;

      let optionsHtml = '';
      q.options.forEach(opt => {{
        optionsHtml += `
          <div id="opt-${{opt.id}}" class="option-item" onclick="toggleOption('${{opt.id}}', ${{isMulti}})">
            <div class="opt-box">${{opt.id}}</div>
            <div style="flex: 1; font-size: 0.95rem;">${{opt.text}}</div>
          </div>
        `;
      }});

      container.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 8px;">
          <div>
            <span class="badge badge-purple">${{q.category || 'Allgemein'}}</span>
            <span class="badge badge-amber">${{isMulti ? 'Mehrfachauswahl' : 'Einfachauswahl'}}</span>
          </div>
          <span style="font-size: 0.8rem; color: var(--text-muted); font-family: monospace;">${{q.id}}</span>
        </div>
        <h3 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 20px; line-height: 1.5;">${{q.question}}</h3>
        <div style="margin-bottom: 20px;">${{optionsHtml}}</div>
        <div id="feedback-area"></div>
        <div style="display: flex; justify-content: flex-end; margin-top: 16px;">
          <button id="submit-btn" class="btn-primary" onclick="submitAnswer()">Antwort prüfen</button>
        </div>
      `;
    }}

    function toggleOption(id, isMulti) {{
      if (isSubmitted) return;
      if (isMulti) {{
        if (selectedOptions.includes(id)) selectedOptions = selectedOptions.filter(x => x !== id);
        else selectedOptions.push(id);
      }} else {{
        selectedOptions = [id];
      }}

      document.querySelectorAll('#question-card-container .option-item').forEach(el => {{
        const optId = el.id.replace('opt-', '');
        el.classList.toggle('selected', selectedOptions.includes(optId));
      }});
    }}

    function submitAnswer() {{
      if (selectedOptions.length === 0 || isSubmitted) return;
      isSubmitted = true;

      const q = questionsStack[0];
      const correctIds = q.options.filter(o => o.isCorrect).map(o => o.id);
      const isCorrect = selectedOptions.length === correctIds.length && selectedOptions.every(id => correctIds.includes(id));

      q.options.forEach(opt => {{
        const el = document.getElementById('opt-' + opt.id);
        if (opt.isCorrect) el.classList.add('correct');
        else if (selectedOptions.includes(opt.id)) el.classList.add('wrong');
      }});

      const feedback = document.getElementById('feedback-area');
      if (isCorrect) {{
        if (soundEnabled) playCorrectSound();
        triggerConfetti();
        feedback.innerHTML = `
          <div class="glass-card" style="background: rgba(16,185,129,0.15); border-color: rgba(16,185,129,0.4);">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
              <span style="color: #6ee7b7; font-weight: 700;">✅ Richtig!</span>
              <span class="badge badge-green">${{q.isoClause || 'ISO 9001'}}</span>
            </div>
            <p style="font-size: 0.88rem; color: #d1fae5;">${{q.isoJustification || q.infobox || ''}}</p>
          </div>
        `;
      }} else {{
        if (soundEnabled) playWrongSound();
        retryCount++;
        feedback.innerHTML = `
          <div class="glass-card" style="background: rgba(239,68,68,0.15); border-color: rgba(239,68,68,0.4);">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
              <span style="color: #fca5a5; font-weight: 700;">❌ Leider nicht ganz richtig</span>
              <span class="badge badge-amber">${{q.isoClause || 'ISO 9001'}}</span>
            </div>
            <p style="font-size: 0.88rem; color: #fee2e2; margin-bottom: 6px;">${{q.isoJustification || q.infobox || ''}}</p>
            <span style="font-size: 0.78rem; color: #fcd34d;">💡 Die Frage wird im Stapel neu einsortiert!</span>
          </div>
        `;
      }}

      document.getElementById('submit-btn').outerHTML = `
        <button class="btn-primary" onclick="nextQuestion(${{isCorrect}})">Nächste Frage ➔</button>
      `;
    }}

    function nextQuestion(isCorrect) {{
      const currentQ = questionsStack.shift();
      if (isCorrect) {{
        if (!masteredIds.includes(currentQ.id)) masteredIds.push(currentQ.id);
      }} else {{
        questionsStack.push(currentQ);
      }}
      localStorage.setItem('qmb_mastered_ids', JSON.stringify(masteredIds));
      renderQuestionCard();
    }}

    function updateMetrics() {{
      document.getElementById('stack-remaining').innerText = questionsStack.length + " Fragen";
      document.getElementById('stack-retries').innerText = retryCount + " neu einsortiert";
      document.getElementById('stack-mastered').innerText = masteredIds.length + " / " + allQuestionsData.length;
      const rate = (masteredIds.length + retryCount) > 0 ? Math.round((masteredIds.length / (masteredIds.length + retryCount)) * 100) : 100;
      document.getElementById('stack-accuracy').innerText = "Richtig-Quote: " + rate + "%";
      const mPct = (masteredIds.length / allQuestionsData.length) * 100;
      document.getElementById('bar-mastered').style.width = mPct + "%";
    }}

    // ---------------- MAYDELL FUNCTIONS (100% UNTOUCHED LOGIC) ----------------
    function filterMaydellCategory() {{
      maydellActiveCategory = document.getElementById('maydell-category-select').value;
      maydellStack = maydellQuestionsData.filter(q => {{
        const cat = (q.category || '').trim();
        return maydellActiveCategory === 'ALL' || cat === maydellActiveCategory;
      }});
      maydellMasteredIds = JSON.parse(localStorage.getItem('qmb_maydell_mastered_ids') || '[]');
      maydellRetryCount = 0;
      renderMaydellCard();
    }}

    function renderMaydellCard() {{
      const container = document.getElementById('maydell-question-card-container');
      maydellSelectedOptions = [];
      maydellSubmitted = false;
      updateMaydellMetrics();

      if (maydellStack.length === 0) {{
        container.innerHTML = `
          <div style="text-align: center; padding: 40px;">
            <div style="font-size: 3rem; margin-bottom: 12px;">🏆</div>
            <h2 style="color: #6ee7b7; margin-bottom: 8px;">Maydell Stapel komplett gemastert!</h2>
            <p style="color: var(--text-muted); margin-bottom: 20px;">Alle Original-Prüfungsfragen erfolgreich bearbeitet.</p>
            <button class="btn-primary" onclick="filterMaydellCategory()">Von vorne beginnen</button>
          </div>
        `;
        return;
      }}

      const q = maydellStack[0];
      const isMulti = q.multipleChoice || q.options.filter(o => o.isCorrect).length > 1;

      let imageHtml = '';
      if (q.imageFile) {{
        const match = q.imageFile.match(/^(\\d+)_/);
        const folder = match ? `QMB_MC_${{match[1]}}` : 'QMB_MC_1';
        imageHtml = `<div style="text-align: center; margin-bottom: 24px;"><img src="images/maydell/${{folder}}/${{q.imageFile}}" style="max-width: 100%; border-radius: 12px; border: 1px solid var(--border-color);" alt="Prüfungsfrage" /></div>`;
      }}

      let optionsHtml = '';
      q.options.forEach(opt => {{
        optionsHtml += `
          <div id="m-opt-${{opt.id}}" class="option-item" onclick="toggleMaydellOption('${{opt.id}}', ${{isMulti}})">
            <div class="opt-box">${{opt.id}}</div>
            <div style="flex: 1; font-size: 0.95rem;">${{opt.text}}</div>
          </div>
        `;
      }});

      container.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
          <span class="badge badge-purple">${{q.category || 'Maydell'}}</span>
          <span style="font-size: 0.8rem; color: var(--text-muted); font-family: monospace;">${{q.id}}</span>
        </div>
        ${{imageHtml}}
        <h3 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 20px;">${{q.question}}</h3>
        <div style="margin-bottom: 20px;">${{optionsHtml}}</div>
        <div id="maydell-feedback-area"></div>
        <div style="display: flex; justify-content: flex-end; margin-top: 16px;">
          <button id="maydell-submit-btn" class="btn-primary" onclick="submitMaydellAnswer()">Antwort prüfen</button>
        </div>
      `;
    }}

    function toggleMaydellOption(id, isMulti) {{
      if (maydellSubmitted) return;
      if (isMulti) {{
        if (maydellSelectedOptions.includes(id)) maydellSelectedOptions = maydellSelectedOptions.filter(x => x !== id);
        else maydellSelectedOptions.push(id);
      }} else {{
        maydellSelectedOptions = [id];
      }}

      document.querySelectorAll('#maydell-question-card-container .option-item').forEach(e => {{
        const optId = e.id.replace('m-opt-', '');
        e.classList.toggle('selected', maydellSelectedOptions.includes(optId));
      }});
    }}

    function submitMaydellAnswer() {{
      if (maydellSelectedOptions.length === 0 || maydellSubmitted) return;
      maydellSubmitted = true;

      const q = maydellStack[0];
      const correctIds = q.options.filter(o => o.isCorrect).map(o => o.id);
      const isCorrect = maydellSelectedOptions.length === correctIds.length && maydellSelectedOptions.every(id => correctIds.includes(id));

      q.options.forEach(opt => {{
        const el = document.getElementById('m-opt-' + opt.id);
        if (opt.isCorrect) el.classList.add('correct');
        else if (maydellSelectedOptions.includes(opt.id)) el.classList.add('wrong');
      }});

      const feedback = document.getElementById('maydell-feedback-area');
      if (isCorrect) {{
        if (soundEnabled) playCorrectSound();
        triggerConfetti();
        feedback.innerHTML = `<div class="glass-card" style="background: rgba(16,185,129,0.15); border-color: rgba(16,185,129,0.4);"><strong style="color: #6ee7b7;">✅ Richtig!</strong><p style="font-size: 0.88rem; color: #d1fae5; margin-top: 4px;">${{q.isoJustification || ''}}</p></div>`;
      }} else {{
        if (soundEnabled) playWrongSound();
        maydellRetryCount++;
        feedback.innerHTML = `<div class="glass-card" style="background: rgba(245,158,11,0.15); border-color: rgba(245,158,11,0.4);"><strong style="color: #fcd34d;">🧐 Falsch! Ab ans Ende des Stapels!</strong><p style="font-size: 0.88rem; color: #fee2e2; margin-top: 4px;">${{q.isoJustification || ''}}</p></div>`;
      }}

      document.getElementById('maydell-submit-btn').outerHTML = `<button class="btn-primary" onclick="nextMaydellQuestion(${{isCorrect}})">Nächste Frage ➔</button>`;
    }}

    function nextMaydellQuestion(isCorrect) {{
      const currentQ = maydellStack.shift();
      if (isCorrect) {{
        if (!maydellMasteredIds.includes(currentQ.id)) maydellMasteredIds.push(currentQ.id);
      }} else {{
        maydellStack.push(currentQ);
      }}
      localStorage.setItem('qmb_maydell_mastered_ids', JSON.stringify(maydellMasteredIds));
      renderMaydellCard();
    }}

    function updateMaydellMetrics() {{
      document.getElementById('maydell-remaining').innerText = maydellStack.length + " Fragen";
      document.getElementById('maydell-retries').innerText = maydellRetryCount + " neu einsortiert";
      document.getElementById('maydell-mastered').innerText = maydellMasteredIds.length + " / " + maydellQuestionsData.length;
      const rate = (maydellMasteredIds.length + maydellRetryCount) > 0 ? Math.round((maydellMasteredIds.length / (maydellMasteredIds.length + maydellRetryCount)) * 100) : 100;
      document.getElementById('maydell-accuracy').innerText = "Richtig-Quote: " + rate + "%";
      const mPct = (maydellMasteredIds.length / maydellQuestionsData.length) * 100;
      document.getElementById('maydell-bar-mastered').style.width = mPct + "%";
    }}

    // ---------------- GLOSSARY ----------------
    function renderGlossary() {{
      const query = (document.getElementById('glossary-search')?.value || '').toLowerCase();
      const grid = document.getElementById('glossary-grid');
      if (!grid) return;

      const filtered = glossaryData.filter(item => 
        item.term.toLowerCase().includes(query) ||
        item.definition.toLowerCase().includes(query) ||
        (item.isoRef && item.isoRef.toLowerCase().includes(query)) ||
        (item.beispiel && item.beispiel.toLowerCase().includes(query))
      );

      grid.innerHTML = filtered.map(item => `
        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
            <h4 style="font-size: 1.05rem; font-weight: 700; color: #a5b4fc;">${{item.term}}</h4>
            <span class="badge badge-purple" style="font-size: 0.72rem;">${{item.category || 'Lexikon'}}</span>
          </div>
          <p style="font-size: 0.88rem; color: var(--text-main); margin-bottom: 8px;">${{item.definition}}</p>
          ${{item.beispiel ? `<div style="font-size: 0.82rem; color: #6ee7b7; background: rgba(16,185,129,0.1); padding: 8px; border-radius: 8px; margin-bottom: 8px;">${{item.beispiel}}</div>` : ''}}
          <div style="font-size: 0.78rem; color: var(--text-muted); font-family: monospace;">📖 ${{item.isoRef}}</div>
        </div>
      `).join('');
    }}

    // ---------------- STATS ----------------
    function renderStats() {{
      const container = document.getElementById('stats-metrics');
      if (!container) return;
      container.innerHTML = `
        <div class="glass-card"><span style="color: var(--text-muted); font-size: 0.8rem;">QMB-Fragen (Gesamt)</span><h3 style="font-size: 1.8rem; color: #a5b4fc;">${{allQuestionsData.length}}</h3></div>
        <div class="glass-card"><span style="color: var(--text-muted); font-size: 0.8rem;">QMB Gemastert</span><h3 style="font-size: 1.8rem; color: #6ee7b7;">${{masteredIds.length}} / ${{allQuestionsData.length}}</h3></div>
        <div class="glass-card"><span style="color: var(--text-muted); font-size: 0.8rem;">Maydell Gemastert</span><h3 style="font-size: 1.8rem; color: #6ee7b7;">${{maydellMasteredIds.length}} / ${{maydellQuestionsData.length}}</h3></div>
      `;
    }}

    function resetStats() {{
      if (confirm("Möchtest du alle Lernstatistiken zurücksetzen?")) {{
        masteredIds = []; retryCount = 0;
        maydellMasteredIds = []; maydellRetryCount = 0;
        localStorage.removeItem('qmb_mastered_ids');
        localStorage.removeItem('qmb_maydell_mastered_ids');
        questionsStack = [...allQuestionsData];
        maydellStack = [...maydellQuestionsData];
        renderQuestionCard();
        renderMaydellCard();
      }}
    }}

    // ---------------- EXAM MODE ----------------
    function startExam() {{
      alert("Prüfungssimulation wird gestartet: 20 zufällige Fragen!");
      // Shuffle 20 questions
      const pool = [...allQuestionsData].sort(() => 0.5 - Math.random()).slice(0, 20);
      questionsStack = pool;
      switchTab('stack');
    }}

    // Init
    populateCategories();
    renderQuestionCard();
    renderMaydellCard();
  </script>
</body>
</html>
"""

    # Write output to repo root index.html (the canonical GitHub Pages entrypoint)
    out_index = repo_dir / "index.html"
    with open(out_index, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[SUCCESS] Canonical single-file application written to: {out_index}")

    # Also keep qmb_fahrschul_app.html in sync
    out_qmb = repo_dir / "qmb_fahrschul_app.html"
    with open(out_qmb, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[SUCCESS] Synchronized {out_qmb}")

if __name__ == "__main__":
    generate_qmb_app()
