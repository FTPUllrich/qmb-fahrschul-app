#!/usr/bin/env python3
"""Vierte Korrektur-Runde: Fragen 134-200 (Fehlermanagement, Agiles QM)"""
import json
from datetime import datetime

HTML_PATH = '/home/ole/Projects/qmb-fahrschul-app/index.html'

CORRECTIONS_R4 = {
    # Fehlermanagement-Block
    "qmb-all-134": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.2",
        "isoJustification": "Gute Fehlerkultur: Fehler als Lernchance (A), keine Schuldzuweisung (B) und praeventive Ausrichtung (C). Schuldigen-Suche (D) hemmt Fehlerkultur.",
        "infobox": "KORREKTUR: A, B, C beschreiben positive Fehlerkulturelemente. D (Schuldigen-Suche) ist kontraproduktiv.",
    },
    "qmb-all-136": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.2",
        "isoJustification": "Fehleranalyseinstrumente: Brainstorming (A), Ishikawa-Diagramm (B) und 5-Why-Analyse (C). Benchmarking (D) ist ein Vergleichsinstrument.",
        "infobox": "KORREKTUR: Brainstorming (A), Ishikawa (B) und 5-Why (C) sind Fehleranalyseinstrumente. Benchmarking (D) ist strategisch.",
    },
    "qmb-all-139": {
        "options_correct": {"A": True, "B": True, "C": False, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.2 / ISO 9000",
        "isoJustification": "Zweck von Fehleraufzeichnungen: Lernen (A) und Nachweis der Korrekturmassnahmen (B). Schuldige identifizieren (C) ist kein ISO-Ziel.",
        "infobox": "KORREKTUR: Fehleraufzeichnungen dienen dem Lernen (A) und Nachweis (B), nicht der Schuldzuweisung.",
    },
    "qmb-all-140": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.2",
        "isoJustification": "Ursachenanalysemethoden: Brainstorming (A), Ishikawa-Diagramm (B) und 5-Why-Analyse (C). Benchmarking (D) ist kein Ursachenanalysewerkzeug.",
        "infobox": "KORREKTUR: Brainstorming (A), Ishikawa (B) und 5-Why (C) sind Ursachenanalysemethoden.",
    },
    "qmb-all-141": {
        "options_correct": {"A": True, "B": True, "C": False, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.2",
        "isoJustification": "Fehlervermeidung = Fehlerquellen ausschliessen (A). Fehlerkorrektur = Fehler nachtraeglich beheben (B). C und D sind falsche Definitionen.",
        "infobox": "KORREKTUR: A (Fehlervermeidung) und B (Fehlerkorrektur) sind korrekte Definitionen.",
    },
    "qmb-all-142": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.2 + 10.3",
        "isoJustification": "Lessons Learned: Erkenntnisse fuer Zukunft (A), Prozessverbesserung durch Erfahrung (B) und Vermeidung aehnlicher Fehler (C). Strafen (D) gehoeren nicht dazu.",
        "infobox": "KORREKTUR: A, B und C beschreiben Lessons Learned korrekt. D (Strafen) hat keinen Platz im Lernansatz.",
    },
    "qmb-all-143": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.2 / 7.5",
        "isoJustification": "Dokumentation im Fehlermanagement: Lernen (A), Nachvollziehbarkeit (B) und Ueberprüfbarkeit (C). Schuldige identifizieren (D) ist kein Ziel.",
        "infobox": "KORREKTUR: A (Lernen), B (Nachvollziehbarkeit) und C (Ueberprüfbarkeit) sind Zwecke der Fehlerdokumentation.",
    },
    "qmb-all-144": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 5.1 + 10.2",
        "isoJustification": "Management im Fehlermanagement: Ressourcen (A), Massnahmenunterstuetzung (B) und Fehlerkultur foerdern (C). Nur Unterschriften leisten (D) ist unzureichend.",
        "infobox": "KORREKTUR: A (Ressourcen), B (Unterstuetzung) und C (Fehlerkultur) sind Management-Aufgaben im Fehlermanagement.",
    },
    "qmb-all-145": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 10002 / ISO 9001:2015 Abs. 10.2",
        "isoJustification": "Reklamationsmeldung: Problembeschreibung (A), Zeitpunkt/Ort (B) und betroffene Produkte (C). Persoenliche Meinungen (D) gehoeren nicht in Reklamationen.",
        "infobox": "KORREKTUR: A (Problem), B (Zeitpunkt/Ort) und C (Produkte/Chargen) sind Pflichtbestandteile einer Reklamationsmeldung.",
    },
    "qmb-all-146": {
        "options_correct": {"A": True, "B": True, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "8D-Report (VDA 8D)",
        "isoJustification": "Nach der Ursachenanalyse (D4/D5) im 8D: Korrekturmassnahmen einfuehren (A = D5/D6), praeventive Massnahmen ableiten (B = D7) und Abschluss (D = D8).",
        "infobox": "KORREKTUR: 8D nach Ursachenanalyse: A (Korrektionsmassnahmen), B (Praevention), D (Abschluss D8). C (Team bilden = D1) kommt am Anfang.",
    },
    "qmb-all-147": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 10002 / ISO 9001:2015 Abs. 9.1.2",
        "isoJustification": "Kommunikation im Reklamationsprozess: Missverstaendnisse vermeiden (A), Vertrauen aufbauen (B) und Prozess beschleunigen (C). Ursachenanalyse ersetzen (D) kann Kommunikation nicht.",
        "infobox": "KORREKTUR: A, B und C sind valide Gruende fuer gute Kommunikation im Reklamationsprozess.",
    },
    "qmb-all-148": {
        "options_correct": {"A": True, "B": False, "C": False, "D": False},
        "isoClause": "ISO 9001:2015 Abs. 10.2 / ISO 9000:2015",
        "isoJustification": "Korrekturmassnahmen = dauerhafte Beseitigung der Fehlerursache (A). Validierung (B) und Ursachenanalyse (C) sind Voraussetzungen, keine Korrekturmassnahmen.",
        "infobox": "Korrekturmassnahme = Ursache dauerhaft beseitigen (A). Unterschied: Korrektur (Symptom) vs. Korrekturmassnahme (Ursache).",
    },
    "qmb-all-149": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.2 + 9.1",
        "isoJustification": "Fehlermanagement-Controlling: Massnahmenwirksamkeit (A), Fehlerkosten (B) und Verbesserungspotenziale (C). Fehler vertuschen (D) widerspricht ISO.",
        "infobox": "KORREKTUR: A (Wirksamkeit), B (Kosten) und C (Potenziale) sind Controlling-Ziele im Fehlermanagement.",
    },
    "qmb-all-150": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.2",
        "isoJustification": "Systemischer Fehler: Grundlegende Strukturfehler (A), wiederholende Fehler in mehreren Bereichen (B) und organisatorische Maengel (C). Tippfehler (D) sind keine systemischen Fehler.",
        "infobox": "KORREKTUR: A, B und C beschreiben systemische Fehler korrekt. D (Tippfehler) ist ein zuaefaelliger Einzelfehler.",
    },
    "qmb-all-151": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 10.2 / Fehlerkultur",
        "isoJustification": "Offene Fehlerkultur: Anonyme Meldungen (A), keine Bestrafung (B) und offene Kommunikation (C). Fehler vertuschen (D) ist das Gegenteil.",
        "infobox": "KORREKTUR: A (Anonymitaet), B (keine Bestrafung) und C (Offenheit) foerdern Fehlerkultur.",
    },
    "qmb-all-152": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "8D-Report Schritt D8",
        "isoJustification": "8D-Abschluss (D8): Dank (A), Dokumentation/Sicherung (B) und Lessons Learned (C). Schuldensuche (D) gehoert nicht zu D8.",
        "infobox": "KORREKTUR: 8D D8 = Dank (A) + Dokumentation (B) + Lessons Learned (C). Kein Platz fuer Schuldzuweisung.",
    },
    "qmb-all-153": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 9.1.2 / ISO 10002",
        "isoJustification": "Reklamationsausloeser: Qualitaetsmangel (A), Kommunikationsprobleme (B) und Lieferterminverstoesse (C). Urlaubsplaene (D) koennen keine Reklamation ausloesen.",
        "infobox": "KORREKTUR: A, B und C sind typische Reklamationsausloeser.",
    },
    "qmb-all-154": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 9001:2015 Abs. 9.1.2 / ISO 10002",
        "isoJustification": "Reklamationen ernst nehmen: Kundenzufriedenheit (A), Kundenbindung (B) und systemische Schwachstellen erkennen (C). Statistikverbesserung (D) ist kein genuines Ziel.",
        "infobox": "KORREKTUR: A (Zufriedenheit), B (Bindung) und C (Schwachstellen erkennen) sind valide Gruende.",
    },
    "qmb-all-155": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "Lean Management / ISO 9001:2015 Abs. 10.3",
        "isoJustification": "Verschwendungsarten (Muda): Ueberproduktion (A), Wartezeiten (B), ueberflussige Transporte (C). 'Uebermassige Kreativitaet' ist keine Lean-Verschwendungsart.",
        "infobox": "KORREKTUR: A, B, C sind Lean-Verschwendungsarten (Muda). D ('uebermassige Kreativitaet') ist keine.",
    },
    # Agiles QM (158)
    "qmb-all-158": {
        "options_correct": {"A": False, "B": True, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "Agiles Manifest / ISO 9001:2015",
        "isoJustification": "Agiles QM priorisiert: Individuen und Interaktion (ueber Prozesse und Tools, B) und Reagieren auf Veraenderung (ueber Planbefolgung, D).",
        "infobox": "KORREKTUR: Agiles QM = B (Individuen/Interaktion) und D (Reagieren auf Veraenderung). Laut Agilem Manifest.",
    },
    # Risikomanagement 171-200
    "qmb-all-171": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "Agile Methoden",
        "isoJustification": "Agile Alltagsmethoden: Kanban (A), Scrum (B) und Daily Standup (C). 'EFQM-Modell' (D) ist ein Exzellenzrahmen, keine agile Methode.",
        "infobox": "KORREKTUR: Agile Alltagsmethoden sind Kanban (A), Scrum (B) und Daily Standup (C).",
    },
    "qmb-all-172": {
        "options_correct": {"A": True, "B": True, "C": False, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018 / ISO 9001:2015 Abs. 6.1",
        "isoJustification": "Risiko = Unsicherheit mit negativen Konsequenzen (A) und messbar/beurteilbar (B). C (immer vermeidbar) und D (immer beherrschbar) sind unrealistisch.",
        "infobox": "KORREKTUR: Risiken sind unsicher mit negativen Folgen (A) und messbar/beurteilbar (B).",
    },
    "qmb-all-173": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018",
        "isoJustification": "Risikoarten: finanzielle (A), operationelle (B) und strategische (C) Risiken. 'Kreative Risiken' (D) sind kein etablierter Begriff.",
        "infobox": "KORREKTUR: Finanzielle (A), operationelle (B) und strategische (C) Risiken sind klassische Risikoarten.",
    },
    "qmb-all-174": {
        "options_correct": {"A": True, "B": False, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018 / ISO 9001:2015 Abs. 6.1",
        "isoJustification": "Risikoidentifikation: Kontext-/Stakeholderanalyse (A) und Risikoregister (C). SWOT (B) ist eher strategisch; Managementreview (D) ist fuer Leistungsbewertung.",
        "infobox": "KORREKTUR: Risikoidentifikation via Kontextanalyse (A) und Risikoregister (C).",
    },
    "qmb-all-176": {
        "options_correct": {"A": False, "B": True, "C": True, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018",
        "isoJustification": "Risikomanagement-Prozessschritte: Risikoidentifikation (B), -analyse (C) und -bewertung (D). Risikoreporting (A) ist eine separate Aktivitaet.",
        "infobox": "KORREKTUR: B (Identifikation), C (Analyse) und D (Bewertung) sind Kernschritte des Risikomanagementprozesses.",
    },
    "qmb-all-177": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018",
        "isoJustification": "Risikobewältigungsstrategien: Risikovermeidung (A), Risikominderung (B) und Risikouebertragung (C). Risikoversteckung (D) ist keine Strategie.",
        "infobox": "KORREKTUR: Risikobewaeltigungsstrategien: Vermeidung (A), Minderung (B), Uebertragung (C).",
    },
    "qmb-all-181": {
        "options_correct": {"A": True, "B": False, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018 / ISO 9001:2015 Abs. 6.1",
        "isoJustification": "Risikobewertung: Wahrscheinlichkeit x Auswirkung (A) und FMEA-RPZ-Methode (C). Kosten-Nutzen (B) ist nicht direkt Risikobewertung; Zufallsprinzip (D) ist kein Verfahren.",
        "infobox": "KORREKTUR: Risikobewertung durch Wahrsch. x Auswirkung (A) und FMEA-RPZ (C).",
    },
    "qmb-all-182": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018 / ISO 9001:2015 Abs. 6.1",
        "isoJustification": "Risiko praeventive Massnahmen: Schulungen (A), Prozessoptimierungen (B) und praeventive Wartung (C). Risiken ignorieren (D) ist keine Massnahme.",
        "infobox": "KORREKTUR: A, B und C sind praeventive Risikobewaaeltigungsmassnahmen.",
    },
    "qmb-all-183": {
        "options_correct": {"A": True, "B": True, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018",
        "isoJustification": "Risikokommunikation: Transparenz (A), Einbindung aller Stakeholder (B) und korrekte Risikobewertung (D). Risiken verschweigen (C) widerspricht ISO 31000.",
        "infobox": "KORREKTUR: A (Transparenz), B (Stakeholdereinbindung) und D (korrekte Bewertung) sind Risikokommunikationsprinzipien.",
    },
    "qmb-all-186": {
        "options_correct": {"A": True, "B": True, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018 / FMEA",
        "isoJustification": "FMEA-Elemente: Fehlerart (A), moegliche Ursachen (B) und RPZ-Berechnung (D). Mitarbeiterbeurteilung (C) ist kein FMEA-Element.",
        "infobox": "KORREKTUR: FMEA analysiert Fehlerarten (A), Ursachen (B) und berechnet RPZ (D).",
    },
    "qmb-all-188": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018",
        "isoJustification": "Risikoberichterstattung: Klare Kommunikation (A), regelmaessige Berichte (B) und Einbindung der Fuehrung (C). Geheimhaltung (D) widerspricht Risikotransparenz.",
        "infobox": "KORREKTUR: A (Klarheit), B (Regelmaessigkeit) und C (Fuehrungseinbindung) sind Risikoreporting-Prinzipien.",
    },
    "qmb-all-189": {
        "options_correct": {"A": False, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018",
        "isoJustification": "Risikosteuerung: Kontinuierliches Monitoring (B) und Anpassung der Massnahmen (C). Risiken vermeiden ohne Analyse (A) ist falsch; Selbstverwaltung (D) ist ungeeignet.",
        "infobox": "KORREKTUR: Risikosteuerung = kontinuierliches Monitoring (B) und Massnahmenanpassung (C).",
    },
    "qmb-all-190": {
        "options_correct": {"A": False, "B": True, "C": True, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018",
        "isoJustification": "Risikominderungsstrategien: Praevention (B), Versicherung (C) und Outsourcing (D). Nichts tun (A) ist keine Strategie.",
        "infobox": "KORREKTUR: B (Praevention), C (Versicherung/Transfer) und D (Outsourcing) sind Risikominderungsstrategien.",
    },
    "qmb-all-191": {
        "options_correct": {"A": False, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018",
        "isoJustification": "Risikoueberwachung: Regelmaessige Reviews (B) und KPIs (C) als Ueberwachungstools. Einmalige Pruefung (A) und volle Delegierung (D) reichen nicht.",
        "infobox": "KORREKTUR: Regelmaessige Reviews (B) und KPIs (C) sind Risikoueberwachungsinstrumente.",
    },
    "qmb-all-192": {
        "options_correct": {"A": False, "B": True, "C": True, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018",
        "isoJustification": "Risikokultur-Elemente: Bewusstsein (B), Verantwortlichkeit (C) und Foerderung durch Fuehrung (D). Risikovermeidung als alleiniges Ziel (A) ist zu einschraenkend.",
        "infobox": "KORREKTUR: B (Bewusstsein), C (Verantwortlichkeit) und D (Fuehrungsfoerderung) bilden die Risikokultur.",
    },
    "qmb-all-194": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018",
        "isoJustification": "Risikomanagementsystem-Nutzen: Transparenz (A), informierte Entscheidungen (B) und praeventive Massnahmen (C). Risiken verstecken (D) ist kein Nutzen.",
        "infobox": "KORREKTUR: A (Transparenz), B (Entscheidungsqualitaet) und C (Praevention) sind Nutzen des Risikomanagements.",
    },
    "qmb-all-195": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018 / ISO 9001:2015",
        "isoJustification": "Risikomanagementerfolg: Fuehrungsunterstuetzung (A), klare Verantwortlichkeiten (B) und kontinuierliches Monitoring (C). Selbstverwaltung ohne System (D) ist ungenuegend.",
        "infobox": "KORREKTUR: A (Fuehrung), B (Verantwortlichkeiten) und C (Monitoring) = Erfolgsfaktoren RM.",
    },
    "qmb-all-197": {
        "options_correct": {"A": False, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018",
        "isoJustification": "Risikouebertragung: Versicherungen (B) und Outsourcing (C) sind Uebertragungsstrategien. Komplettes Risikovermeiden (A) ist oft nicht moeglich.",
        "infobox": "KORREKTUR: Risikouebertragung via Versicherung (B) und Outsourcing (C).",
    },
    "qmb-all-198": {
        "options_correct": {"A": True, "B": False, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018",
        "isoJustification": "Risikoakzeptanz-Kriterien: Risikobereitschaft (A) und Risikotoleranz (C). Emotionale Entscheidungen (B) und persoenliche Vorlieben (D) sind keine Kriterien.",
        "infobox": "KORREKTUR: Risikoakzeptanz basiert auf Risikobereitschaft (A) und Risikotoleranz (C).",
    },
    "qmb-all-199": {
        "options_correct": {"A": True, "B": True, "C": True, "D": False},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018 / ISO 9001:2015",
        "isoJustification": "Risikobericht-Inhalte: Identifizierte Risiken (A), Bewertungen (B) und Massnahmen (C). Finanzberichterstattung (D) ist kein Standardinhalt.",
        "infobox": "KORREKTUR: Risikobericht = Identifizierte Risiken (A) + Bewertungen (B) + Massnahmen (C).",
    },
    "qmb-all-200": {
        "options_correct": {"A": True, "B": True, "C": False, "D": True},
        "multipleChoice": True,
        "isoClause": "ISO 31000:2018 / ISO 9001:2015 Abs. 6.1",
        "isoJustification": "Risikobewertungsschritte: Identifikation (A), Analyse (B) und Priorisierung (D). Risiken ignorieren (C) ist kein Schritt.",
        "infobox": "KORREKTUR: Risikobewertung = Identifikation (A) + Analyse (B) + Priorisierung (D).",
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

print("=== Korrekturen Runde 4 ===")
questions, n = apply_corrections(questions, CORRECTIONS_R4)
print(f"\nKorrekturen: {n}")

new_json = json.dumps(questions, ensure_ascii=False, indent=2)
new_content = content[:start_idx] + 'const allQuestionsData = ' + new_json + ';' + content[end_idx:]
with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Gespeichert.")
