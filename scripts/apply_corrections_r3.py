#!/usr/bin/env python3
"""Dritte Korrektur-Runde: Fragen 93-200 (KVP, Fehlermanagement, etc.)"""
import json, shutil
from datetime import datetime

HTML_PATH = '/home/ole/Projects/qmb-fahrschul-app/index.html'

CORRECTIONS_R3 = {
    # PDCA-Fragen mit nur A als richtig (viele haben mehrere richtige Antworten)
    "qmb-all-093": {
        "options_correct": {"A": True, "B": False, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Kap. 9",
        "isoJustification": "Regelmaessige Ueberwachung in der Check-Phase erfolgt durch Interne Audits und Kennzahlenanalyse (A).",
        "infobox": "Check-Phase: Regelmaessige Ueberwachung durch Audits und Kennzahlenanalyse.",
    },
    "qmb-all-094": {
        "options_correct": {"A": True, "B": False, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Kap. 9 / PDCA",
        "isoJustification": "Kontinuierliche Verbesserung in der Check-Phase basiert auf faktenbasierter Datenanalyse.",
        "infobox": "Faktenbasierte Entscheidungen in der Check-Phase ermoeglichen gezielte Verbesserungen.",
    },
    "qmb-all-097": {
        "options_correct": {"A": True, "B": True, "C": False, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 10 (Act-Phase)",
        "isoJustification": "Act-Phase: Nachhaltige Verbesserung durch systematische Massnahmenimplementierung (A) und Standardisierung erfolgreicher Loesungen (B).",
        "infobox": "KORREKTUR: A und B sind Act-Phase-Elemente. C (ohne Analyse) widerspricht dem systematischen Ansatz.",
    },
    "qmb-all-100": {
        "options_correct": {"A": True, "B": True, "C": False, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 5 / PDCA",
        "isoJustification": "Wichtige Voraussetzungen fuer erfolgreiche Umsetzung: Fuehrungsunterstuetzung (A) und Ressourcenbereitstellung (B).",
        "infobox": "KORREKTUR: Fuehrungskommitment (A) und Ressourcen (B) sind Schluessel-Voraussetzungen.",
    },
    "qmb-all-101": {
        "options_correct": {"A": True, "B": False, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 9 / PDCA Check",
        "isoJustification": "Check-Phase Hauptziel: Wirksamkeit der Massnahmen beurteilen (A) und Leistungskennzahlen analysieren (C).",
        "infobox": "KORREKTUR: A (Wirksamkeit beurteilen) und C (Kennzahlen analysieren) sind Check-Phase-Ziele.",
    },
    "qmb-all-102": {
        "options_correct": {"A": True, "B": False, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Kap. 9 / ISO 19011",
        "isoJustification": "Interne Audits und Kennzahlenanalyse sind die Hauptmethoden zur Ueberprüfung in der Check-Phase.",
        "infobox": "Check-Phase-Ueberprüfungsmethoden: Interne Audits, Kennzahlenauswertung, Managementbewertung.",
    },
    "qmb-all-104": {
        "options_correct": {"A": False, "B": True, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Kap. 10 / PDCA Act",
        "isoJustification": "Act-Phase: Ableitung und Umsetzung von Korrekturmassnahmen basierend auf den Pruefergebnissen (B). A (geplante Prozesse) gehoert zur Do-Phase.",
        "infobox": "KORREKTUR: B ist richtig. Act = Korrekturmassnahmen auf Basis von Check-Ergebnissen. A ('geplante Prozesse') = Do-Phase.",
    },
    "qmb-all-105": {
        "options_correct": {"A": True, "B": False, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Abs. 10.3",
        "isoJustification": "KVP ermoeglicht schrittweise Optimierung von Prozessen und Ergebnissen. Dies ist der genuine Mehrwert - nicht nur eine normative Pflicht.",
        "infobox": "KVP = Schrittweise Prozessoptimierung. Der echte Nutzen liegt in kontinuierlicher Leistungssteigerung.",
    },
    "qmb-all-106": {
        "options_correct": {"A": True, "B": False, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Abs. 10.2 + 10.3",
        "isoJustification": "Nachhaltige Verbesserung: Systematische Ursachenanalyse und deren Beseitigung (A). Spontane Aenderungen (B) und Regelueberlastung (D) kontraproduktiv.",
        "infobox": "Nachhaltige QMS-Verbesserung: Systematische Ursachenanalyse + dauerhafte Massnahmen = Kern von ISO 10.2.",
    },
    "qmb-all-107": {
        "options_correct": {"A": True, "B": False, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Kap. 6 (Plan)",
        "isoJustification": "Plan-Phase: Prozesse und Massnahmen zur Zielerreichung definieren (A). B, C, D beschreiben falsche Planungsansaetze.",
        "infobox": "Plan-Phase: Ziele setzen, Prozesse definieren, Ressourcen planen, Risiken bewerten.",
    },
    "qmb-all-108": {
        "options_correct": {"A": True, "B": False, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Abs. 6.1 + 6.2",
        "isoJustification": "Plan-Phase-Dokumentation: Risikobewertungen und Massnnahmenplaene sind normativ gefordert.",
        "infobox": "Plan-Phase Kerndiokumente: Risikobewertungsmatrix, Qualitaetsziele, Massnahmenplaene (Abs. 6.1 + 6.2).",
    },
    "qmb-all-109": {
        "options_correct": {"A": True, "B": False, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Abs. 6.2.2",
        "isoJustification": "Massnahmenplan: Systematische Festlegung von Verantwortlichkeiten, Terminen und Zielen (A).",
        "infobox": "Massnahmenplan nach ISO 9001:2015 Abs. 6.2.2: Was, wer, bis wann, wie gemessen wird.",
    },
    "qmb-all-110": {
        "options_correct": {"A": True, "B": False, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Abs. 7.2 + 7.3",
        "isoJustification": "Schulungen in der Do-Phase: Alle Mitarbeitenden muessen die definierten Prozesse und Qualitaetsanforderungen verstehen und anwenden koennen.",
        "infobox": "Schulung (Abs. 7.2): Kompetenz sicherstellen, nicht nur Pflicht erfuellen - praktisches Verstaendnis ist entscheidend.",
    },
    "qmb-all-111": {
        "options_correct": {"A": True, "B": False, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Abs. 7.2 + 8.5",
        "isoJustification": "Do-Phase QS-Massnahmen: Standardisierte Arbeitsanweisungen und Schulungen (A) sind die Kerninstrumente.",
        "infobox": "Do-Phase: Standardisierte Arbeitsanweisungen (Abs. 8.5) + Schulungen (Abs. 7.2) = Qualitaetssicherung in der Ausfuehrung.",
    },
    "qmb-all-112": {
        "options_correct": {"A": True, "B": False, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Kap. 9 (Check)",
        "isoJustification": "Check-Phase: Regelmaessige Auswertung von Kennzahlen und internen Audits (A) sind die Hauptinstrumente.",
        "infobox": "Check-Phase: Kennzahlenauswertung + Interne Audits = Hauptinstrumente der Leistungsbewertung.",
    },
    "qmb-all-113": {
        "options_correct": {"A": True, "B": False, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Abs. 10.2 + 10.3",
        "isoJustification": "Lernen aus Check-Phase: Ursachenanalyse von Abweichungen und Identifikation von Verbesserungspotenzial (A).",
        "infobox": "Check -> Act: Ursachenanalyse + Verbesserungsidentifikation = Schluessel fuer lernende Organisation.",
    },
    "qmb-all-114": {
        "options_correct": {"A": True, "B": False, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Kap. 10 (Act)",
        "isoJustification": "Act-Phase nachhaltige Verbesserung: Prozessanpassungen basierend auf analysierten Daten (A) sind der korrekte Ansatz.",
        "infobox": "Act = datenbasierte Prozessanpassung, keine blinde Reaktion oder Aktionismus.",
    },
    "qmb-all-115": {
        "options_correct": {"A": True, "B": True, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.3",
        "isoJustification": "KVP-Hauptziele: Prozesse verbessern (A), Fehler abstellen (B) und Wettbewerbsfaehigkeit sichern (D). 'Stillstand erreichen' (C) ist das Gegenteil von KVP.",
        "infobox": "KORREKTUR: KVP-Ziele sind A (Prozessverbesserung), B (Fehlerabstellung) und D (Wettbewerbsfaehigkeit). C (Stillstand) ist kein KVP-Ziel!",
    },
    "qmb-all-116": {
        "options_correct": {"A": True, "B": True, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.3 / Kaizen-Philosophie",
        "isoJustification": "KVP-Kernprinzipien: Kleine Schritte (A), Mitarbeitereinbeziehung (B), Fehlervermeidung statt Vertuschung (D). Staendige Wiederholung (C) ist kein Prinzip.",
        "infobox": "KORREKTUR: KVP-Prinzipien: Kleine Schritte (A), Mitarbeitereinbindung (B) und Fehlervermeidung statt -vertuschung (D).",
    },
    "qmb-all-117": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.3",
        "isoJustification": "KVP-Werkzeuge: PDCA (A), Kaizen-Workshops (B) und 5S (C) sind klassische KVP-Methoden. Benchmarking (D) ist eher ein strategisches Instrument.",
        "infobox": "KORREKTUR: A (PDCA), B (Kaizen-Workshops) und C (5S) sind KVP-Kernwerkzeuge. Benchmarking (D) ist primär strategisch.",
    },
    "qmb-all-118": {
        "options_correct": {"A": True, "B": False, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Abs. 0.4",
        "isoJustification": "PDCA = Plan - Do - Check - Act. Dies ist die korrekte und vollstaendige Bedeutung.",
        "infobox": "PDCA = Plan (Planen) - Do (Ausfuehren) - Check (Ueberpruefen) - Act (Handeln/Verbessern).",
    },
    "qmb-all-119": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 7.3 + Kaizen",
        "isoJustification": "Mitarbeiterbeteiligung im KVP: Detailkenntnisse (A), Ideenvielfalt (B) und hoehere Akzeptanz (C) sind alle valide Gruende. Managementarbeitseinsparung (D) ist kein KVP-Ziel.",
        "infobox": "KORREKTUR: A (Problemkenntnisse), B (Ideen) und C (Akzeptanz) sind Gruende fuer Mitarbeiterbeteiligung im KVP.",
    },
    "qmb-all-120": {
        "options_correct": {"A": True, "B": True, "C": True, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.3",
        "isoJustification": "KVP-Vorteile: Effizienzsteigerung (A), Verschwendungsreduzierung (B), Kundenzufriedenheit (C) und geringere Kosten (D) - alle sind valide Vorteile.",
        "infobox": "KORREKTUR: Alle vier Optionen (A-D) sind legitime KVP-Vorteile.",
    },
    "qmb-all-121": {
        "options_correct": {"A": True, "B": True, "C": False, "D": False},
        "multipleChoice": True,
        "isoClause": "Kaizen-Philosophie / ISO 9001:2015 Abs. 10.3",
        "isoJustification": "Kaizen = 'Veraenderung zum Besseren' (A) und 'kontinuierliche, schrittweise Verbesserung' (B). Beide Bedeutungen erhaenzen sich. Radikale Umstrukturierung (C) = Innovation, nicht Kaizen.",
        "infobox": "KORREKTUR: Kaizen bedeutet sowohl 'Veraenderung zum Besseren' (A) als auch 'kontinuierliche Schrittverbesserung' (B).",
    },
    "qmb-all-122": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 5.1 + 10.3",
        "isoJustification": "Management im KVP: Rahmenbedingungen schaffen (A), Vorbildfunktion (B) und Ressourcen bereitstellen (C). Alleinige Entscheidungen (D) widersprechen dem partizipativen KVP-Ansatz.",
        "infobox": "KORREKTUR: A (Rahmenbedingungen), B (Vorbild) und C (Ressourcen) sind Management-Rollen im KVP.",
    },
    "qmb-all-123": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "Lean-Management / ISO 9001:2015 Abs. 10.3",
        "isoJustification": "7 Verschwendungsarten (Muda): Ueberproduktion (A), Wartezeiten (B), ueberflussige Transporte (C). 'Uebermassige Kreativitaet' (D) ist keine Verschwendungsart.",
        "infobox": "KORREKTUR: Lean-Verschwendungsarten inkl. A (Ueberproduktion), B (Warten) und C (Transport).",
    },
    "qmb-all-124": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "5S-Methode / ISO 9001:2015",
        "isoJustification": "5S: Ordnung/Sauberkeit (A), Standardisierung (B) und Reduzierung von Suchzeiten (C). Prozessdokumentation (D) ist ein eigenes Instrument.",
        "infobox": "KORREKTUR: 5S foerdert Ordnung (A), Standardisierung (B) und reduziert Suchzeiten (C).",
    },
    "qmb-all-125": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 6 (Plan-Phase)",
        "isoJustification": "Plan-Phase: Probleme analysieren (A), Ziele definieren (B) und Masssnahmen planen (C). Kontrolle (D) gehoert zur Check-Phase.",
        "infobox": "KORREKTUR: Plan-Phase beinhaltet A (Problemanalyse), B (Ziele) und C (Massnnahmenplanung). D (Kontrolle) = Check.",
    },
    "qmb-all-126": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 9 (Check-Phase)",
        "isoJustification": "Check prueeft: Ob Massnahmen umgesetzt wurden (A), ob Ergebnisse den Zielen entsprechen (B) und ob Anpassungen noetig sind (C). D (Mitarbeiterurlaub) ist irrelevant.",
        "infobox": "KORREKTUR: A, B und C sind alle korrekten Check-Phase-Pruefkriterien.",
    },
    "qmb-all-127": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 10 (Act-Phase)",
        "isoJustification": "Act-Phase ist entscheidend fuer: Nachhaltigkeit (A), Standardisierung erfolgreicher Loesungen (B) und Uebertragung auf andere Bereiche (C).",
        "infobox": "KORREKTUR: A (Nachhaltigkeit), B (Standardisierung) und C (Transfer) sind Act-Phase-Kernaspekte.",
    },
    "qmb-all-128": {
        "options_correct": {"A": True, "B": True, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.3 / Kaizen vs. Kaikaku",
        "isoJustification": "KVP vs. Projekte: KVP ist dauerhaft (A), lebt von kleinen Schritten (B) und bindet kontinuierlich Mitarbeiter ein (D). C ('endet nach Projektabschluss') ist falsch - das waere ein einmaliges Projekt.",
        "infobox": "KORREKTUR: A (dauerhaft), B (kleine Schritte) und D (kontinuierliche Mitarbeiterbindung) unterscheiden KVP von einmaligen Projekten.",
    },
    "qmb-all-129": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 5.1 + 10.3",
        "isoJustification": "KVP-Erfolgsfaktoren: Management-Unterstuetzung (A), offene Kommunikationskultur (B) und kontinuierliche Schulung (C). Fehlerbestrafung (D) ist kontraproduktiv und widerspricht der KVP-Philosophie.",
        "infobox": "KORREKTUR: A, B, C sind KVP-Erfolgsfaktoren. Strenge Bestrafung (D) zerstoert Verbesserungskultur.",
    },
    "qmb-all-130": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.3 / Kaizen",
        "isoJustification": "KVP-Massnahmen: Arbeitsplatzumgestaltung (A), einheitliche Checklisten (B) und Informationsflussverbesserung (C). Betriebsfeier (D) ist kein KVP.",
        "infobox": "KORREKTUR: A (Wege reduzieren), B (Checklisten), C (Informationsfluss) sind KVP-Massnahmen. D (Betriebsfeier) ist kein KVP.",
    },
    # Fehlermanagement (131-170)
    "qmb-all-131": {
        "options_correct": {"A": True, "B": True, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.2",
        "isoJustification": "Fehlermanagement umfasst: sofortige Reaktion (A), Ursachenanalyse (B) und Korrekturmassnahmen (D). Fehler ignorieren (C) widerspricht ISO 9001.",
        "infobox": "Fehlermanagement = sofortige Reaktion + Ursachenanalyse + nachhaltige Korrekturmassnahmen.",
    },
    "qmb-all-132": {
        "options_correct": {"A": True, "B": True, "C": False, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.2 / ISO 9000:2015",
        "isoJustification": "Nichtkonformitaet = Nichterfuellung einer Anforderung. Korrektur = Symptombehandlung, Korrekturmassnahme = Ursachenbeseitigung.",
        "infobox": "Nichtkonformitaet (A) + Korrektionsmassnahme (B) sind Schluesselkonzepte. Abweichung und Fehler sind synonyme Begriffe.",
    },
    "qmb-all-133": {
        "options_correct": {"A": False, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.2",
        "isoJustification": "Korrekturmassnahme-Schritte: Ursachenanalyse (B) und Massnahmenplanung (C). Direktes Loeschen von Fehlern (A) ist Korrektur, nicht Korrekturmassnahme.",
        "infobox": "Korrekturmassnahmen = Ursache beseitigen (B) + Massnahmen planen (C). Nicht nur Symptome behandeln.",
    },
}

def apply_corrections(questions, corrections):
    count = 0
    for q in questions:
        qid = q['id']
        if qid not in corrections:
            continue
        corr = corrections[qid]
        if 'options_correct' in corr:
            old = [o['id'] for o in q['options'] if o['isCorrect']]
            for o in q['options']:
                if o['id'] in corr['options_correct']:
                    o['isCorrect'] = corr['options_correct'][o['id']]
            new = [o['id'] for o in q['options'] if o['isCorrect']]
            if old != new:
                q['hasDeviation'] = True
                count += 1
                print(f"  {qid}: {old} -> {new}")
        if 'multipleChoice' in corr:
            q['multipleChoice'] = corr['multipleChoice']
        if 'isoClause' in corr:
            q['isoClause'] = corr['isoClause']
        if 'isoJustification' in corr:
            q['isoJustification'] = corr['isoJustification']
        if 'infobox' in corr:
            q['infobox'] = corr['infobox']
    return questions, count

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()
start_idx = content.find('const allQuestionsData = [')
end_idx = content.find('];', start_idx) + 2
json_str = content[start_idx+len('const allQuestionsData = '):end_idx-1]
questions = json.loads(json_str)

print("=== Korrekturen Runde 3 ===")
questions, n = apply_corrections(questions, CORRECTIONS_R3)
print(f"\nKorrekturen: {n}")

new_json = json.dumps(questions, ensure_ascii=False, indent=2)
new_content = content[:start_idx] + 'const allQuestionsData = ' + new_json + ';' + content[end_idx:]
with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Gespeichert.")
