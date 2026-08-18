#!/usr/bin/env python3
"""Zweite Korrektur-Runde: Fragen 61-200"""
import json, shutil
from datetime import datetime

HTML_PATH = '/home/ole/Projects/qmb-fahrschul-app/index.html'

CORRECTIONS_R2 = {
    "qmb-all-062": {
        "options_correct": {"A": False, "B": False, "C": False, "D": True},
        "isoClause": "ISO 9001:2015 Kap. 4",
        "isoJustification": "Die Frage fragt nach NICHT-Anforderungen. Option D enthaelt 'Quantitaetsmanagementsystem' - diesen Begriff gibt es nicht. ISO 9001 regelt 'Qualitaetsmanagementsysteme'.",
        "infobox": "KORREKTUR: D ist richtig. 'Quantitaetsmanagementsystem und keine Prozesse' (D) ist keine normative Anforderung - es enthält inhaltliche Fehler.",
    },
    "qmb-all-063": {
        "options_correct": {"A": False, "B": False, "C": True, "D": False},
        "isoClause": "ISO/IEC Direktive Annex SL / HLS",
        "isoJustification": "Die HLS (Harmonized Structure) ist eine einheitliche Struktur fuer alle ISO-Managementsystemnormen, kein spezielles QM-Tool.",
        "infobox": "KORREKTUR: C ist richtig. HLS = einheitliche Struktur fuer alle ISO-MSN (ISO 9001, 14001, 45001 etc.), erleichtert Integration.",
    },
    "qmb-all-064": {
        "options_correct": {"A": False, "B": False, "C": True, "D": False},
        "isoClause": "ISO 9001:2015 Abs. 4.1",
        "isoJustification": "Der Kontext umfasst das Verstaendnis interner UND externer Faktoren sowie die Anforderungen interessierter Parteien.",
        "infobox": "KORREKTUR: C ist richtig. Kontext = interne + externe Einflussfaktoren auf das QMS (nicht nur Finanzlage).",
    },
    "qmb-all-066": {
        "options_correct": {"A": True, "B": False, "C": True, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 4.2",
        "isoJustification": "Interessierte Parteien koennen Mitarbeiter (A), Regulierungsbehoerden (C) und Gesellschaft (D) sein. 'Eltern' sind keine typische Stakeholder-Gruppe.",
        "infobox": "KORREKTUR: A (Mitarbeiter), C (Regulierungsbehoerden) und D (Gesellschaft) sind interessierte Parteien nach ISO 9001:2015 Abs. 4.2.",
    },
    "qmb-all-067": {
        "options_correct": {"A": False, "B": False, "C": False, "D": True},
        "isoClause": "ISO 9001:2015 Kap. 4 / Kap. 9.2",
        "isoJustification": "Interne Audits (D) gehoeren zu Kapitel 9 (Bewertung der Leistung), NICHT zu Kapitel 4 (Kontext der Organisation).",
        "infobox": "KORREKTUR: D ist richtig. Interne Audits sind in Kap. 9.2, nicht in Kap. 4 geregelt.",
    },
    "qmb-all-068": {
        "options_correct": {"A": False, "B": False, "C": True, "D": False},
        "isoClause": "ISO 9001:2015 Abs. 4.2",
        "isoJustification": "ISO 9001 fordert, relevante interessierte Parteien zu ermitteln und deren Anforderungen zu bestimmen - nicht alle moeglichen, nicht nur Kunden.",
        "infobox": "KORREKTUR: C ist richtig. Relevante interessierte Parteien ermitteln und Anforderungen bestimmen (Abs. 4.2).",
    },
    "qmb-all-069": {
        "options_correct": {"A": False, "B": False, "C": True, "D": False},
        "isoClause": "ISO 9001:2015 Abs. 4.1",
        "isoJustification": "Kontext = Identifizierung interner UND externer Faktoren sowie relevanter interessierter Parteien.",
        "infobox": "KORREKTUR: C ist richtig. Kontext = intern + extern + interessierte Parteien (Abs. 4.1 + 4.2).",
    },
    "qmb-all-071": {
        "options_correct": {"A": False, "B": False, "C": False, "D": True},
        "isoClause": "ISO 9001:2015 Abs. 5.3",
        "isoJustification": "Abs. 5.3 fordert Verantwortlichkeiten fuer QMS-Konformitaet, Prozessleistung und Kundenorientierung - NICHT fuer Gehaltsfestlegungen.",
        "infobox": "KORREKTUR: D ist richtig (Nicht-Anforderung). Gehaltsfestlegung (D) ist keine normative Anforderung nach Abs. 5.3.",
    },
    "qmb-all-072": {
        "options_correct": {"A": False, "B": False, "C": False, "D": True},
        "isoClause": "ISO 9001:2015 Abs. 4.2",
        "isoJustification": "Haustiere sind keine interessierten Parteien. Alle anderen (Kunden, Lieferanten, Mitarbeiter) sind klassische Stakeholder.",
        "infobox": "KORREKTUR: D ist richtig. Haustiere der Mitarbeiter sind offensichtlich keine interessierten Parteien.",
    },
    "qmb-all-073": {
        "options_correct": {"A": True, "B": False, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Abs. 4.1",
        "isoJustification": "Kontext = Verstaendnis interner und externer Faktoren, die das QMS beeinflussen (Abs. 4.1).",
        "infobox": "Kontext der Organisation: interne Faktoren (Kultur, Ressourcen, Strategie) + externe Faktoren (Markt, Gesetzgebung, Technologie).",
    },
    "qmb-all-074": {
        "options_correct": {"A": False, "B": True, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Abs. 5.3",
        "isoJustification": "ISO 9001:2015 fordert KEINEN expliziten QMB mehr (A ist falsch!). Die oberste Leitung muss Verantwortlichkeiten zuweisen (B ist richtig).",
        "infobox": "KRITISCHER FEHLER KORRIGIERT: A ist FALSCH - ISO 9001:2015 schreibt keinen QMB mehr vor! B ist richtig: Verantwortlichkeiten durch oberste Leitung.",
    },
    "qmb-all-075": {
        "options_correct": {"A": False, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 6 (Planung) / PDCA",
        "isoJustification": "Plan-Phase = Kap. 6: Qualitaetsziele (B) und Risiko-/Chancenbewertung (C). Interne Audits (A) = Check, Korrekturmassnahmen (D) = Act.",
        "infobox": "KORREKTUR: B (Qualitaetsziele) und C (Risikobewertung) gehoeren zur Plan-Phase. Audits = Check, Korrekturen = Act.",
    },
    "qmb-all-076": {
        "options_correct": {"A": True, "B": False, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 9 (Check) / PDCA",
        "isoJustification": "Check-Phase: Wirksamkeit bewerten (A) und Kennzahlen analysieren (C). Planung (B) = Plan, Lieferantenkommunikation (D) = Do.",
        "infobox": "KORREKTUR: A (Wirksamkeitsbewertung) und C (Kennzahlenanalyse) sind Check-Phase-Ziele.",
    },
    "qmb-all-077": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 6.2.2",
        "isoJustification": "Ein Massnnahmenplan muss Zustaendigkeiten (A), Terminvorgaben (B) und Ressourcen/Budget (C) enthalten. D (ohne konkrete Daten) ist unvollstaendig.",
        "infobox": "KORREKTUR: A, B, C sind Bestandteile eines vollstaendigen Massnahmenplans nach ISO 9001:2015 Abs. 6.2.2.",
    },
    "qmb-all-078": {
        "options_correct": {"A": True, "B": True, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 9 / ISO 19011",
        "isoJustification": "Check-Phase-Methoden: Interne Audits (A), Kundenbefragungen (B) und Prozessbeobachtungen (D). Schulungszertifikate (C) unterstuetzen die Do-Phase.",
        "infobox": "KORREKTUR: A (Audits), B (Kundenbefragungen) und D (Prozessbeobachtungen) sind Check-Phase-Methoden.",
    },
    "qmb-all-079": {
        "options_correct": {"A": False, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 7+8 (Do) / PDCA",
        "isoJustification": "Do-Phase: Arbeitsanweisungen einhalten (B) und Mitarbeiter schulen (C). Freie Interpretation (A) widerspricht dem PDCA, Risikobewertung (D) = Plan.",
        "infobox": "KORREKTUR: B (Arbeitsanweisungen) und C (Schulung) sind entscheidend in der Do-Phase.",
    },
    "qmb-all-080": {
        "options_correct": {"A": False, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 6.1",
        "isoJustification": "Risiko-/Chancenbewertung identifiziert Verbesserungsbereiche (B) und priorisiert Masssnahmen (C). Interne Audits ersetzen (A) ist falsch; nur fuer ISO-Zertiifizierung (D) ist falsch.",
        "infobox": "KORREKTUR: B (Verbesserungsbereiche) und C (Massnahmenpriorisierung) sind Zwecke der Risikobewertung.",
    },
    "qmb-all-082": {
        "options_correct": {"A": True, "B": False, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 10 (Act) / PDCA",
        "isoJustification": "Act-Phase: Praeventive Massnahmen (A) und Reaktion auf Auditfeststellungen (D). Produktfreigabe (B) = Do, Schulung allein (C) = eher Do.",
        "infobox": "KORREKTUR: A (praeventive Massnahmen) und D (Auditfeststellungen umsetzen) = Act-Phase.",
    },
    "qmb-all-083": {
        "options_correct": {"A": True, "B": False, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 9 / PDCA",
        "isoJustification": "Kennzahlen dienen als Grundlage fuer Entscheidungen in Check und Act (A) und zur Erfassung der Zielerreichung (C).",
        "infobox": "KORREKTUR: A (Entscheidungsgrundlage) und C (Zielerreichungserfassung) sind Rollen von Kennzahlen im PDCA.",
    },
    "qmb-all-084": {
        "options_correct": {"A": False, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 6.1 + 6.2 (Planung)",
        "isoJustification": "Plan-Phase-Dokumente: Risikobewertungen (B) und Massnnahmenlisten (C). Auditplaene (A) gehoeren eher zur Check-Phase; Lieferantenerklaerungen (D) sind operational.",
        "infobox": "KORREKTUR: B (Risikobewertung) und C (Massnnahmenliste) sind typische Plan-Phase-Dokumente.",
    },
    "qmb-all-085": {
        "options_correct": {"A": True, "B": False, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 7+8 (Do) / PDCA",
        "isoJustification": "Do-Phase operationalisiert Prozesse aus der Planung (A) und Kundenanforderungen (D). Neue Geschaeftszweige (B) = strategisch, Personalentwicklung (C) = Plan.",
        "infobox": "KORREKTUR: A (Geplante Prozesse ausfuehren) und D (Kundenanforderungen erfullen) = Do-Phase.",
    },
    "qmb-all-086": {
        "options_correct": {"A": True, "B": True, "C": False, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 7+8 (Do)",
        "isoJustification": "Ineffektive Do-Phase: Fehlende Schulung (A) und unklare Prozesse (B) sind Hauptursachen. Ueberdokumentation (C) kann hinderlich sein, ist aber kein typisches Do-Problem.",
        "infobox": "KORREKTUR: A (fehlende Schulung) und B (unklare Prozesse) fuehren zu ineffektiver Do-Phase.",
    },
    "qmb-all-087": {
        "options_correct": {"A": False, "B": True, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 PDCA",
        "isoJustification": "Check = analysieren und bewerten. Act = implementieren von Verbesserungen und Massnahmen. B beschreibt den Unterschied korrekt.",
        "infobox": "KORREKTUR: B ist richtig. Check analysiert Ergebnisse, Act implementiert Verbesserungen auf Basis der Analyse.",
    },
    "qmb-all-088": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 6 (Planung)",
        "isoJustification": "Fehler in der Plan-Phase: Fehlende Stakeholdereinbindung (A), uebermassige Planung ohne Umsetzung (B) und mangelhafte Risikobewertung (C). Zu fruehe Prozesskontrolle (D) ist kein Plan-Fehler.",
        "infobox": "KORREKTUR: A, B, C sind typische Plan-Phase-Fehler.",
    },
    "qmb-all-089": {
        "options_correct": {"A": True, "B": False, "C": True, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 10.3 (KVP)",
        "isoJustification": "KVP im Act: Massnahmen auf Basis von Ergebnissen (A), Feedbackintegration (C) und Fehlervermeidung (D). Prozesse ohne Analyse einfuehren (B) widerspricht KVP.",
        "infobox": "KORREKTUR: A (ergebnisbasierte Massnahmen), C (Feedbackintegration) und D (Fehlervermeidung) = KVP im Act.",
    },
    "qmb-all-090": {
        "options_correct": {"A": True, "B": True, "C": False, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Kap. 9 (Check-Phase)",
        "isoJustification": "Check-Phase: Managementbewertung (A, Kap. 9.3) und Interne Audits (B, Kap. 9.2) finden regelmaessig statt. Prozessaenderungen (C) = Act, Ursachenanalyse (D) = Reaktion auf Abweichungen.",
        "infobox": "KORREKTUR: A (Managementbewertung) und B (Interne Audits) sind regelmaessige Check-Phasen-Aktivitaeten.",
    },
    # Fragen 91-110 mit Kaestchen-Symbolen
    "qmb-all-091": {
        "options_correct": {"A": False, "B": True, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Kap. 9 / PDCA",
        "isoJustification": "Regelmaessige Ueberwachung in der Check-Phase: Kennzahlen-Monitoring ist die zentrale Methode.",
        "infobox": "Check-Phase: Regelmaessige Ueberwachung durch Kennzahlen, Audits und Kundenfeedback.",
    },
    "qmb-all-092": {
        "options_correct": {"A": False, "B": False, "C": True, "D": False},
        "isoClause": "ISO 9001:2015 Kap. 4.1",
        "isoJustification": "PESTLE-Analyse umfasst Political, Economic, Social, Technological, Legal, Environmental Faktoren fuer die Kontextanalyse.",
        "infobox": "PESTLE = Werkzeug fuer externe Kontextanalyse nach ISO 9001:2015 Abs. 4.1.",
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

print("=== Korrekturen Runde 2 ===")
questions, n = apply_corrections(questions, CORRECTIONS_R2)
print(f"\nKorrekturen: {n}")

new_json = json.dumps(questions, ensure_ascii=False, indent=2)
new_content = content[:start_idx] + 'const allQuestionsData = ' + new_json + ';' + content[end_idx:]
with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)
print(f"Gespeichert.")
