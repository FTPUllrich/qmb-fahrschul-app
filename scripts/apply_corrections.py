#!/usr/bin/env python3
import json, shutil
from datetime import datetime

HTML_PATH = '/home/ole/Projects/qmb-fahrschul-app/index.html'
BACKUP_PATH = f'/home/ole/Projects/qmb-fahrschul-app/index_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'

# Korrekturdatenbank: qid -> {options_correct: {A: bool, B: bool, C: bool, D: bool}, ...}
CORRECTIONS = {
    "qmb-all-007": {
        "options_correct": {"A": False, "B": False, "C": True, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 9.1.2",
        "isoJustification": "VoC (Voice of Customer) ist ein Sammelbegriff fuer alle Methoden zur Erfassung von Kundenwuenschen und -erwartungen. VoC fuehrt zu passgenauen Produkten/DL.",
        "infobox": "KORREKTUR: VoC = Sammelbegriff (C) und fuehrt zu besseren Produkten (D). Nicht nur auf Beschwerden beschraenkt.",
    },
    "qmb-all-022": {
        "options_correct": {"A": True, "B": True, "C": False, "D": False},
        "multipleChoice": True,
        "isoClause": "MueG / EU-MUeV / VO (EU) 2019/1020",
        "isoJustification": "Marktüberwachung wird durch das Marktüberwachungsgesetz (MüG) und die EU-Marktüberwachungsverordnung geregelt. Das AGG regelt Diskriminierungsschutz, keine Produktüberwachung.",
        "infobox": "KORREKTUR: A (MüG) und B (EU-MÜV) korrekt. C (AGG) ist kein Produktüberwachungsgesetz.",
    },
    "qmb-all-025": {
        "options_correct": {"A": True, "B": True, "C": True, "D": True},
        "multipleChoice": True,
        "isoClause": "ProdSG / ISO 9001:2015",
        "isoJustification": "Produktsicherheit erfordert alle genannten Maßnahmen: Wareneingangsprüfung, FMEA, Prozesskontrollen und Dokumentation.",
        "infobox": "KORREKTUR: Alle vier Optionen (A, B, C, D) sind korrekte Maßnahmen zur Produktsicherheit.",
    },
    "qmb-all-027": {
        "options_correct": {"A": True, "B": True, "C": False, "D": False},
        "multipleChoice": True,
        "isoClause": "ProdHaftG §1 / BGB §823",
        "isoJustification": "Nach ProdHaftG müssen nachgewiesen werden: ein Schaden (A) und Kausalzusammenhang zwischen Fehler und Schaden (B).",
        "infobox": "KORREKTUR: A (Schadensnachweis) und B (Kausalitaet) sind die Haftungskriterien nach ProdHaftG.",
    },
    "qmb-all-041": {
        "options_correct": {"A": True, "B": False, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 4.4",
        "isoJustification": "Klassische Prozesslandkarte: Kernprozesse (A, wertschoepfend), Fuehrungsprozesse (C, steuernd) und Unterstuetzungsprozesse (ressourcebereitstellend).",
        "infobox": "KORREKTUR: Kernprozesse (A) UND Fuehrungsprozesse (C) sind korrekte Prozessarten in der Prozesslandkarte.",
    },
    "qmb-all-042": {
        "options_correct": {"A": True, "B": False, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 4.4.1",
        "isoJustification": "ISO 9001:2015 Abs. 4.4.1 fordert Festlegung von Schnittstellen (A) und Kommunikation zwischen Prozessbeteiligten (C).",
        "infobox": "KORREKTUR: Schnittstellenbewertung (A) UND Abstimmung (C) sind normativ gefordert.",
    },
    "qmb-all-044": {
        "options_correct": {"A": True, "B": False, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 4.4",
        "isoJustification": "Eine Prozesslandkarte zeigt Kernprozesse (A) und Management-/Hilfsprozesse (C) sowie deren Zusammenwirken.",
        "infobox": "KORREKTUR: Kernprozesse (A) UND Management-/Hilfsprozesse (C) sind Hauptbestandteile der Prozesslandkarte.",
    },
    "qmb-all-047": {
        "options_correct": {"A": False, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 4.4",
        "isoJustification": "Schluesselprozesse umfassen Kernprozesse (wertschoepfend, B) und Fuehrungsprozesse (steuernd, C). Ueberflüssige Prozesse existieren per Definition nicht.",
        "infobox": "Schluesselprozesse: Kernprozesse (B) + Fuehrungsprozesse (C) - die wesentlichen Treiber des Unternehmenserfolgs.",
    },
    "qmb-all-049": {
        "options_correct": {"A": True, "B": True, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 9.1",
        "isoJustification": "Prozesscontrolling-Ansaetze: Finanzsicht (A), Prozesssicht (B) und Datensicht (D). Mitarbeiterbewertung ist kein klassischer Controlling-Ansatz.",
        "infobox": "KORREKTUR: Finanzsicht (A), Prozesssicht (B) UND Datensicht (D) sind alle gueltigen Prozesscontrolling-Perspektiven.",
    },
    "qmb-all-050": {
        "options_correct": {"A": True, "B": False, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 9.1",
        "isoJustification": "Wertstromanalyse (A) und Spaghettidiagramm (C) sind klassische Prozessanalysemethoden. SWOT und Brainstorming sind andere Methodenkategorien.",
        "infobox": "KORREKTUR: Wertstromanalyse (A) und Spaghettidiagramm (C) sind Prozessanalysewerkzeuge.",
    },
    "qmb-all-051": {
        "options_correct": {"A": True, "B": False, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 9.1",
        "isoJustification": "Kennzahlen haben Informationscharakter (A) und eine spezifische Form/Messbarkeit (C). Sie sind objektiv, nicht meinungsbasiert.",
        "infobox": "KORREKTUR: Kennzahlen = Informationscharakter (A) + spezifische Form (C). Immer objektiv und messbar.",
    },
    "qmb-all-052": {
        "options_correct": {"A": False, "B": True, "C": True, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 9.1",
        "isoJustification": "Handlungsfelder fuer Kennzahlensysteme: Kunden (B), Mitarbeitermotivation (C) und Kosten (D). Soziale Medien sind kein klassisches QM-Handlungsfeld.",
        "infobox": "KORREKTUR: Kunden (B), Mitarbeitermotivation (C) und Kosten (D) sind die Handlungsfelder. Nicht 'Soziale Medien' (A).",
    },
    "qmb-all-053": {
        "options_correct": {"A": True, "B": True, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 7.1.6 / DSGVO",
        "isoJustification": "Big-Data-Strategie erfordert Datenschutz (A), Sicherheitsmaßnahmen (B) und Dateninfrastruktur (D). Unkontrollierte Datenweitergabe (C) widerspricht DSGVO.",
        "infobox": "KORREKTUR: Datenschutz (A), Sicherheit (B) und Infrastruktur (D) sind erforderlich. Automatische Datenweitergabe (C) ist unzulaessig.",
    },
    "qmb-all-054": {
        "options_correct": {"A": False, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 4.4",
        "isoJustification": "Schluesselprozesse befinden sich auf Kernprozessebene (B) und Fuehrungsprozessebene (C).",
        "infobox": "Schluesselprozesse: Kernprozesse (B) und Fuehrungsprozesse (C).",
    },
    "qmb-all-055": {
        "options_correct": {"A": False, "B": False, "C": True, "D": False},
        "multipleChoice": False,
        "isoClause": "ISO 9001:2015 Abs. 5.3",
        "isoJustification": "ISO 9001:2015 Abs. 5.3 fordert klare Definition, Dokumentation und Kommunikation von Rollen und Verantwortlichkeiten.",
        "infobox": "KRITISCHER FEHLER KORRIGIERT: A (Vermeidung von Dokumentation) widerspricht ISO 9001 fundamental! C (klare Dokumentation + Kommunikation) ist korrekt.",
    },
    "qmb-all-056": {
        "options_correct": {"A": True, "B": True, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 4",
        "isoJustification": "Kapitel 4: 4.1 Kontext (A), 4.2 Interessierte Parteien (B), 4.4 QMS-Prozesse (D). C enthaelt 'Quantitaetsmanagementsystem' - inhaltlicher Fehler.",
        "infobox": "KORREKTUR: A (4.1), B (4.2) und D (4.4) korrekt. C falsch ('Quantitaets-' statt 'Qualitaetsmanagementsystem').",
    },
    "qmb-all-058": {
        "options_correct": {"A": True, "B": True, "C": False, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO/IEC Direktive Annex SL",
        "isoJustification": "Die HLS erleichtert die Integration mehrerer Managementsysteme (A) und bietet einen gemeinsamen Rahmen (B).",
        "infobox": "KORREKTUR: A (Integration) UND B (gemeinsamer Rahmen) sind Vorteile der HLS.",
    },
    "qmb-all-059": {
        "options_correct": {"A": False, "B": False, "C": False, "D": True},
        "multipleChoice": False,
        "isoClause": "ISO 9001:2015 Abs. 0.4 (PDCA)",
        "isoJustification": "Plan = Kapitel 4, 5, 6. Kontext der Organisation (Kap. 4, D) gehoert zur Plan-Phase. Kap. 1-3 sind Einleitungskapitel ohne PDCA-Zuordnung.",
        "infobox": "KORREKTUR: PDCA-Plan = Kap. 4+5+6. 'Kontext der Organisation' (D, Kap. 4) ist Plan. Kap. 1-3 (Einleitung) gehoeren nicht zum PDCA.",
    },
    "qmb-all-060": {
        "options_correct": {"A": True, "B": True, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 5.3",
        "isoJustification": "ISO 9001:2015 Abs. 5.3 fordert Verantwortlichkeiten fuer: QMS-Konformitaet (A), Prozessleistung (B) und Kundenorientierung (D). Kosten-/Gewinnberichte (C) nicht normativ gefordert.",
        "infobox": "KORREKTUR: A, B und D sind normativ geforderte Verantwortlichkeiten nach Abs. 5.3.",
    },
    "qmb-all-178": {
        "options_correct": {"A": True, "B": False, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018 / ISO 9001:2015 Abs. 6.1",
        "isoJustification": "SWOT-Analyse (A) und FMEA (C) sind klassische Risikobewertungsmethoden.",
        "infobox": "Risikobewertungsmethoden: SWOT (A) fuer strategische Risiken, FMEA (C) fuer Produkt-/Prozessrisiken.",
    },
    "qmb-all-179": {
        "options_correct": {"A": True, "B": True, "C": True, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018 / ISO 9001:2015 Abs. 6.1",
        "isoJustification": "Risiken haben Folgen auf monetaerer, umweltbezogener, Kundenzufriedenheits- und persoenlicher Ebene - alle vier Aspekte (A, B, C, D).",
        "infobox": "KORREKTUR: Alle vier Risikofolgen-Kategorien (A-D) sind korrekt: Monetaer, Umwelt, Kundenzufriedenheit, Mensch.",
    },
    "qmb-all-180": {
        "options_correct": {"A": True, "B": False, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018 / FMEA",
        "isoJustification": "RPZ (Risikoprioritaetszahl, A) und Risikobewertungsmatrix (C) sind Standardinstrumente der Risikobewertung.",
        "infobox": "Risikobewertung: RPZ = Auftreten x Bedeutung x Entdeckung (FMEA). Risikomatrix = Eintrittswahrsch. x Auswirkung.",
    },
    "qmb-all-184": {
        "options_correct": {"A": False, "B": True, "C": True, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018",
        "isoJustification": "Drei Rollen im Risikomanagementsystem: Risikosystembeauftragte (B), Risikoeignerinnen (C) und Risikomanagerinnen (D).",
        "infobox": "Rollen im Risikomanagement: Risikosystembeauftragte (B), Risikoeignerinnen (C), Risikomanagerinnen (D).",
    },
    "qmb-all-185": {
        "options_correct": {"A": True, "B": False, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018",
        "isoJustification": "Risikopolitik legt Verantwortungen/Befugnisse (A) und Ressourcenplanung (C) fest.",
        "infobox": "Risikopolitik enthaelt: Verantwortungen (A) und Ressourcenplanung (C).",
    },
    "qmb-all-187": {
        "options_correct": {"A": True, "B": True, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 6.1 / ISO 31000",
        "isoJustification": "Risikobewältigungsmaßnahmen: Kontrollen (A), Schulungen (B) und Prozessoptimierung (D).",
        "infobox": "KORREKTUR: A, B und D sind Risikobewältigungsmaßnahmen.",
    },
    "qmb-all-193": {
        "options_correct": {"A": False, "B": False, "C": False, "D": True},
        "multipleChoice": False,
        "isoClause": "ISO 31000:2018 Abs. 6.5.3",
        "isoJustification": "Ein akzeptables Restrisiko kann bewusst eingegangen werden, wenn die Kosten der Risikobehandlung den Nutzen uebersteigen.",
        "infobox": "KORREKTUR: D ist korrekt. Restrisiko = verbleibendes Risiko nach Behandlung. Ein akzeptables Restrisiko wird bewusst akzeptiert.",
    },
    "qmb-all-196": {
        "options_correct": {"A": True, "B": True, "C": False, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018 / FMEA",
        "isoJustification": "RPZ in der FMEA: Auftrittswahrscheinlichkeit (A) und Konsequenz/Bedeutung (B) sind zwei der drei RPZ-Faktoren.",
        "infobox": "RPZ = Auftrittswahrsch. (A) x Bedeutung/Konsequenz (B) x Entdeckungswahrsch. - zwei der drei Faktoren sind A und B.",
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

print(f"Fragen geladen: {len(questions)}")
shutil.copy(HTML_PATH, BACKUP_PATH)
print(f"Backup: {BACKUP_PATH}")

print("\n=== Korrekturen ===")
questions, n = apply_corrections(questions, CORRECTIONS)
print(f"\nKorrekturen: {n}")

new_json = json.dumps(questions, ensure_ascii=False, indent=2)
new_content = content[:start_idx] + 'const allQuestionsData = ' + new_json + ';' + content[end_idx:]

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)
print(f"Gespeichert: {HTML_PATH}")
