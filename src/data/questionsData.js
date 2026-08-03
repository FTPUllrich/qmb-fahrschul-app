// TÜV QMB / QMF Fragenkatalog nach DIN EN ISO 9001:2015 & DIN EN ISO 19011
export const initialQuestions = [
  {
    id: "qmb-101",
    question: "Welche der folgenden Abschnitte der DIN EN ISO 9001:2015 beschreiben den High Level Structure (HLS) Aufsatz bezüglich des PDCA-Zyluses (Plan-Do-Check-Act)?",
    options: [
      { id: "A", text: "Kapitel 4 (Kontext), Kapitel 5 (Führung) und Kapitel 6 (Planung) entsprechen 'Plan'.", isCorrect: true },
      { id: "B", text: "Kapitel 7 (Unterstützung) und Kapitel 8 (Betrieb) entsprechen 'Do'.", isCorrect: true },
      { id: "C", text: "Kapitel 9 (Bewertung der Leistung) entspricht 'Check'.", isCorrect: true },
      { id: "D", text: "Kapitel 10 (Verbesserung) entspricht 'Act'.", isCorrect: true }
    ],
    multipleChoice: true,
    category: "High Level Structure & PDCA",
    isoClause: "ISO 9001:2015 Kap. 0.4 / HLS",
    infobox: "Die High Level Structure (HLS) ordnet alle Kapitel der ISO 9001 dem PDCA-Zyklus zu. Plan umfasst Kontext, Führung und Planung. Do umfasst Unterstützung und Betrieb. Check umfasst die Leistungsbewertung. Act umfasst die kontinuierliche Verbesserung.",
    isoJustification: "Gemäß ISO 9001:2015 Abschnitt 0.4 (PDCA-Zyklus) basiert die Struktur des Qualitätsmanagementsystems direkt auf der Abfolge Plan (Kap. 4,5,6), Do (Kap. 7,8), Check (Kap. 9) und Act (Kap. 10)."
  },
  {
    id: "qmb-102",
    question: "Was versteht die DIN EN ISO 9001:2015 unter der 'obersten Leitung' (Top Management) und welche Verantwortung trägt diese?",
    options: [
      { id: "A", text: "Die oberste Leitung ist eine Person oder Gruppe, die eine Organisation auf oberster Ebene führt und steuert.", isCorrect: true },
      { id: "B", text: "Sie kann die Verantwortung für das Qualitätsmanagementsystem komplett an den Qualitätsmanagementbeauftragten (QMB) delegieren.", isCorrect: false },
      { id: "C", text: "Sie muss die Verpflichtung bezüglich des QMS nachweisen und die Qualitätspolitik festlegen.", isCorrect: true },
      { id: "D", text: "Sie ist verantwortlich für das Bereitstellen der erforderlichen Ressourcen.", isCorrect: true }
    ],
    multipleChoice: true,
    category: "Führung & Verantwortung",
    isoClause: "ISO 9001:2015 Kap. 5.1 & 5.2",
    infobox: "In der ISO 9001:2015 ist ein expliziter 'QMB' als geforderte Rolle gestrichen worden; stattdessen steht die oberste Leitung (Top Management) direkt in der Pflicht (Rechenschaftspflicht). Die operative Durchführung kann zwar delegiert werden, die Gesamtverantwortung verbleibt jedoch uneingeschränkt bei der obersten Leitung.",
    isoJustification: "Nach ISO 9001:2015 Abs. 5.1.1 (Führung und Verpflichtung) muss die oberste Leitung Rechenschaftspflicht für die Wirksamkeit des QMS übernehmen. Eine vollständige Entbindung oder Abwälzung der Verantwortung auf einen Beauftragten widerspricht der Norm."
  },
  {
    id: "qmb-103",
    question: "Wie ist der Begriff 'Dokumentierte Information' gemäß ISO 9001:2015 zu verstehen?",
    options: [
      { id: "A", text: "Es ist ein Sammelbegriff, der sowohl früher geforderte Qualitätsmanagement-Handbücher als auch Aufzeichnungen umfasst.", isCorrect: true },
      { id: "B", text: "Es muss zwingend ein physisches, ausgedrucktes Papierhandbuch existieren.", isCorrect: false },
      { id: "C", text: "Dokumentierte Informationen können in jedem beliebigen Format und Medium (z.B. digital, Video, Datenbank) vorliegen.", isCorrect: true },
      { id: "D", text: "Organisationen bestimmen selbst den angemessenen Umfang der dokumentierten Information.", isCorrect: true }
    ],
    multipleChoice: true,
    category: "Dokumentierte Information",
    isoClause: "ISO 9001:2015 Kap. 7.5",
    infobox: "ISO 9001:2015 ersetzt die Begriffe 'Dokument' und 'Aufzeichnung' durch den flexibleren Begriff 'dokumentierte Information'. Dies erlaubt papierlose QMS, Wikis, Software-Workflows und individuelle Dokumentationsumfänge je nach Unternehmensgröße und Prozesskomplexität.",
    isoJustification: "ISO 9000:2015 Abs. 3.8.6 und ISO 9001:2015 Abs. 7.5 regeln die Lenkung dokumentierter Informationen. Ein gedrucktes Handbuch ist normativ nicht mehr vorgeschrieben (Abs. 7.5.1)."
  },
  {
    id: "qmb-104",
    question: "Welches Ziel verfolgt ein 'Internes Audit' nach DIN EN ISO 19011 und ISO 9001:2015 Abs. 9.2?",
    options: [
      { id: "A", text: "Überprüfung, ob das QMS die eigenen Anforderungen der Organisation und die Forderungen der Norm erfüllt.", isCorrect: true },
      { id: "B", text: "Ermittlung von Schuldigen bei Prozessfehlern zur disziplinarischen Bestrafung.", isCorrect: false },
      { id: "C", text: "Bewertung der wirksamen Umsetzung und Aufrechterhaltung des Qualitätsmanagementsystems.", isCorrect: true },
      { id: "D", text: "Bereitstellung von Informationen für die Managementbewertung.", isCorrect: true }
    ],
    multipleChoice: true,
    category: "Audits (DIN EN ISO 19011)",
    isoClause: "ISO 9001:2015 Kap. 9.2 / ISO 19011",
    infobox: "Interne Audits (Erstparteien-Audits) dienen als Selbstprüfungsinstrument zur Ermittlung von Konformität und Verbesserungspotenzialen. Sie dürfen niemals zur Schuldzuweisung missbraucht werden, da Audits prozess- und faktenorientiert sein müssen.",
    isoJustification: "ISO 9001:2015 Abs. 9.2.1 schreibt vor, dass interne Audits in geplanten Abständen durchgeführt werden müssen, um objektive Nachweise über Konformität und Wirksamkeit zu erlangen. Schuldzuweisungen verstoßen gegen Auditprinzipien der ISO 19011 Abs. 4."
  },
  {
    id: "qmb-105",
    question: "Was versteht man unter dem 'Risikobasierten Ansatz' in der ISO 9001:2015?",
    options: [
      { id: "A", text: "Die Verpflichtung, vorbeugende Maßnahmen als eigenständiges Kapitel durchzuführen.", isCorrect: false },
      { id: "B", text: "Die systematische Berücksichtigung von Risiken und Chancen in allen Prozessphasen.", isCorrect: true },
      { id: "C", text: "Die Pflicht, für jedes Risiko ein zertifiziertes FMEA-Formblatt auszufüllen.", isCorrect: false },
      { id: "D", text: "Maßnahmen zum Umgang mit Risiken müssen proportional zu den potenziellen Auswirkungen auf die Produktkonformität sein.", isCorrect: true }
    ],
    multipleChoice: true,
    category: "Risikomanagement",
    isoClause: "ISO 9001:2015 Kap. 6.1",
    infobox: "Der risikobasierte Ansatz durchzieht die gesamte ISO 9001:2015. Ehemals getrennte 'Vorbeugemaßnahmen' wurden integriert: Risikobasiertes Denken preventiv zu handeln gehört zur Prozessplanung. Eine formelle FMEA ist nützlich, aber normativ nicht zwingend vorgeschrieben.",
    isoJustification: "Nach ISO 9001:2015 Abs. 6.1 (Maßnahmen zum Umgang mit Risiken und Chancen) muss die Organisation Risiken bestimmen und bewerten, jedoch legt die Norm keine formelle Risikomanagement-Methode fest."
  },
  {
    id: "qmb-106",
    question: "Was gehört zwingend zu den Eingaben (Inputs) für die Managementbewertung gemäß ISO 9001:2015 Abs. 9.3?",
    options: [
      { id: "A", text: "Status von Maßnahmen vorheriger Managementbewertungen.", isCorrect: true },
      { id: "B", text: "Kundenfeedbacks und Rückmeldungen von interessierten Parteien.", isCorrect: true },
      { id: "C", text: "Ergebnisse von Audits und die Leistung von externen Anbietern.", isCorrect: true },
      { id: "D", text: "Private Urlaubsplanungen des mittleren Managements.", isCorrect: false }
    ],
    multipleChoice: true,
    category: "Bewertung der Leistung",
    isoClause: "ISO 9001:2015 Kap. 9.3.2",
    infobox: "Die Managementbewertung muss regelmäßig durch die oberste Leitung durchgeführt werden. Zu den normativen Eingaben gehören Audit-Ergebnisse, Kundenzufriedenheit, Kennzahlen, Prozessleistung, Lieferantenbewertung und Risikomaßnahmen.",
    isoJustification: "Gemäß ISO 9001:2015 Abschnitt 9.3.2 (Eingaben für die Managementbewertung) müssen alle Optionen A, B und C explizit bewertet werden."
  },
  {
    id: "qmb-107",
    question: "Was ist ein 'Korrekturmaßnahme' (Corrective Action) im Vergleich zu einer 'Korrektur' (Correction)?",
    options: [
      { id: "A", text: "Eine Korrektur beseitigt eine festgestellte Nichtkonformität (z.B. Nacharbeit eines fehlerhaften Teils).", isCorrect: true },
      { id: "B", text: "Eine Korrekturmaßnahme beseitigt die Ursache einer Nichtkonformität, um ein erneutes Auftreten zu verhindern.", isCorrect: true },
      { id: "C", text: "Korrektur und Korrekturmaßnahme bedeuten exakt dasselbe.", isCorrect: false },
      { id: "D", text: "Eine Korrekturmaßnahme beinhaltet die Ursachenanalyse (Root Cause Analysis).", isCorrect: true }
    ],
    multipleChoice: true,
    category: "Verbesserung & Korrektur",
    isoClause: "ISO 9001:2015 Kap. 10.2 / ISO 9000:2015 Abs. 3.12",
    infobox: "Wichtige Unterscheidung in der Prüfung: Eine Korrektur ist die Beseitigung des Symptoms (Fehlerbehebung). Eine Korrekturmaßnahme ermittelt die Wurzel des Übels (Ursachenanalyse z.B. 5-Why, Ishikawa) und verhindert die Wiederholung.",
    isoJustification: "ISO 9000:2015 Abs. 3.12.2 (Korrektur) vs. Abs. 3.12.6 (Korrekturmaßnahme) sowie ISO 9001:2015 Abs. 10.2 legen diesen begrifflichen und praktischen Unterschied fest."
  },
  {
    id: "qmb-108",
    question: "Welche Qualitätswerkzeuge gehören zu den klassischen '7 Quality Control Tools' (7 QC-Tools)?",
    options: [
      { id: "A", text: "Ishikawa-Diagramm (Ursachen-Wirkungs-Diagramm)", isCorrect: true },
      { id: "B", text: "Pareto-Diagramm (80/20-Regel)", isCorrect: true },
      { id: "C", text: "Fehlersammelkarte & Histogramm", isCorrect: true },
      { id: "D", text: "Balanced Scorecard", isCorrect: false }
    ],
    multipleChoice: true,
    category: "QM-Werkzeuge & Methoden",
    isoClause: "QM-Methodenkatalog / ISO 9004",
    infobox: "Die 7 klassischen QC-Werkzeuge nach Kaoru Ishikawa sind: Fehlersammelkarte, Histogramm, Pareto-Diagramm, Ishikawa-Diagramm, Regelkarte (SPC), Streudiagramm und Korrelationsdiagramm/Mindmap. Die Balanced Scorecard ist ein strategisches Führungsinstrument, kein klassisches QC-Tool.",
    isoJustification: "QM-Methodenstandard (ISO 9004 Empfehlungen zur Leistungsverbesserung) ordnet Ishikawa, Pareto, Histogramm und Fehlersammelkarte den 7 elementaren Qualitätstechniken zu."
  },
  {
    id: "qmb-109",
    question: "Welche Bedeutung haben 'interessierte Parteien' (Interested Parties / Stakeholder) gemäß ISO 9001:2015 Abs. 4.2?",
    options: [
      { id: "A", text: "Die Organisation muss diejenigen interessierten Parteien bestimmen, die für ihr QMS relevant sind.", isCorrect: true },
      { id: "B", text: "Es müssen nur Kunden und Aktionäre berücksichtigt werden.", isCorrect: false },
      { id: "C", text: "Zu den interessierten Parteien können Kunden, Lieferanten, Gesetzgeber, Mitarbeiter und Anwohner zählen.", isCorrect: true },
      { id: "D", text: "Die Anforderungen interessierter Parteien müssen überwacht und überprüft werden.", isCorrect: true }
    ],
    multipleChoice: true,
    category: "Kontext der Organisation",
    isoClause: "ISO 9001:2015 Kap. 4.2",
    infobox: "ISO 9001 verlangt das Verstehen der Erwartungen interessierter Parteien. Neben Kunden spielen Behörden, Normungsgremien, Zulieferer und Mitarbeiter eine Schlüsselrolle.",
    isoJustification: "Nach ISO 9001:2015 Abschnitt 4.2 müssen sowohl relevante Parteien als auch deren relevante Anforderungen bestimmt und fortlaufend überwacht werden."
  },
  {
    id: "qmb-110",
    question: "Was bedeutet das 'Prozessorientierte Qualitätsmanagement' (Process Approach)?",
    options: [
      { id: "A", text: "Ergebnisse werden effizienter erzielt, wenn Tätigkeiten als zusammenhängende Prozesse verstanden und gesteuert werden.", isCorrect: true },
      { id: "B", text: "Jeder Prozess benötigt definierte Eingaben (Inputs), Tätigkeiten, Ergebnisse (Outputs), Kennzahlen und Ressourcen.", isCorrect: true },
      { id: "C", text: "Das Silodenken einzelner Abteilungen wird zugunsten von durchgängigen Wertschöpfungsketten aufgelöst.", isCorrect: true },
      { id: "D", text: "Prozesse dürfen im Nachhinein niemals verändert werden.", isCorrect: false }
    ],
    multipleChoice: true,
    category: "Prozessmanagement",
    isoClause: "ISO 9001:2015 Kap. 4.4",
    infobox: "Der Prozessansatz gehört zu den 7 Grundsätzen des Qualitätsmanagements (ISO 9000:2015). Prozesse werden z.B. mit dem Turtle-Modell (Inputs, Outputs, Ressourcen, Kennzahlen, Risiken) visualisiert.",
    isoJustification: "Gemäß ISO 9001:2015 Abschnitt 4.4 (Qualitätsmanagementsystem und seine Prozesse) muss die Organisation Prozesse bestimmen, steuern und kontinuierlich verbessern."
  }
];
