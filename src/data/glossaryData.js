// QMF & QMB Sachbegriffe-Sammlung (Lexikon) nach DIN EN ISO 9000:2015 & ISO 9001:2015
export const initialGlossary = [
  {
    id: "term-1",
    term: "Audit",
    definition: "Systematischer, unabhängiger und dokumentierter Prozess zur Erlangung von objektiven Nachweisen und zu deren objektiver Auswertung, um zu beurteilen, inwieweit Auditkriterien erfüllt sind.",
    category: "Auditing & Bewertung",
    isoRef: "DIN EN ISO 19011 / ISO 9000:2015 Abs. 3.13.1",
    keywords: ["Audit", "Nachweis", "Auditor", "Erstpartei", "Zweitpartei", "Drittpartei"]
  },
  {
    id: "term-2",
    term: "High Level Structure (HLS) / Harmonized Structure",
    definition: "Eine von ISO entwickelte einheitliche Grundstruktur (10 Kapitel) für alle modernen Managementsystemnormen (z.B. ISO 9001, ISO 14001, ISO 45001) mit identischen Kerntexten und Begriffen.",
    category: "Normung & Struktur",
    isoRef: "ISO Directives Annex SL",
    keywords: ["HLS", "High Level Structure", "Harmonisierung", "Normstruktur", "Annex SL"]
  },
  {
    id: "term-3",
    term: "PDCA-Zyklus (Deming-Kreis)",
    definition: "Plan-Do-Check-Act. Der kontinuierliche Regelkreis zur Qualitätsverbesserung: Planen (Plan: Kap. 4, 5, 6), Umsetzen (Do: Kap. 7, 8), Überprüfen (Check: Kap. 9) und Anpassen/Verbessern (Act: Kap. 10).",
    category: "QM-Grundlagen",
    isoRef: "ISO 9001:2015 Kap. 0.4",
    keywords: ["PDCA", "Plan Do Check Act", "Deming-Kreis", "Verbesserung", "Regelkreis"]
  },
  {
    id: "term-4",
    term: "Dokumentierte Information",
    definition: "Information, die von einer Organisation gelenkt und aufrechterhalten (Vorgabedokumente) oder aufbewahrt (Aufzeichnungen/Nachweise) werden muss, unabhängig vom gewählten Medium.",
    category: "Dokumentation",
    isoRef: "ISO 9000:2015 Abs. 3.8.6 / ISO 9001 Kap. 7.5",
    keywords: ["Dokumentierte Information", "Aufzeichnung", "Vorgabedokument", "Lenkung", "Aufbewahren"]
  },
  {
    id: "term-5",
    term: "Risikobasierter Ansatz (Risk-based Thinking)",
    definition: "Systematische Berücksichtigung von Risiken und Chancen bereits in der Planungsphase von Prozessen und des gesamten QMS, um unerwünschte Auswirkungen präventiv zu minimieren.",
    category: "Risikomanagement",
    isoRef: "ISO 9001:2015 Kap. 6.1 / ISO 31000",
    keywords: ["Risiko", "Chance", "Risikobasiertes Denken", "Prävention", "FMEA"]
  },
  {
    id: "term-6",
    term: "KVP (Kontinuierlicher Verbesserungsprozess)",
    definition: "Die stetige, schrittweise Perfektionierung von Produkten, Prozessen und Systemen durch Einbeziehung aller Mitarbeiter (auch als Kaizen bekannt).",
    category: "Verbesserung & KVP",
    isoRef: "ISO 9001:2015 Kap. 10.3",
    keywords: ["KVP", "Kaizen", "Verbesserung", "Stetige Erhöhung", "Kaikaku"]
  },
  {
    id: "term-7",
    term: "Managementbewertung (Management Review)",
    definition: "Die durch die oberste Leitung in geplanten Abständen durchgeführte Eignungs-, Angemessenheits- und Wirksamkeitsprüfung des Qualitätsmanagementsystems.",
    category: "Führung & Bewertung",
    isoRef: "ISO 9001:2015 Kap. 9.3",
    keywords: ["Managementbewertung", "Management Review", "Oberste Leitung", "Eingaben", "Ergebnisse"]
  },
  {
    id: "term-8",
    term: "Ishikawa-Diagramm (Ursachen-Wirkungs-Diagramm)",
    definition: "Qualitätswerkzeug zur Identifizierung aller potenziellen Ursachen eines Problems anhand der 6 Ms (Mensch, Maschine, Material, Methode, Messung, Mitwelt / Milieu).",
    category: "QM-Werkzeuge & Methoden",
    isoRef: "QM-Methodik / 7 QC-Tools",
    keywords: ["Ishikawa", "Fischgrätendiagramm", "Ursache-Wirkung", "6M", "Fehlerursachen"]
  },
  {
    id: "term-9",
    term: "Turtle-Modell",
    definition: "Eine visuelle Methode zur ganzheitlichen Prozessbeschreibung anhand von 6 W-Fragen: Womit? (Betriebsmittel), Wer? (Personal/Kompetenz), Wie? (Verfahren/Methoden), Womit messen? (KPIs), Was geht hinein? (Input), Was kommt heraus? (Output).",
    category: "Prozessmanagement",
    isoRef: "ISO 9001:2015 Kap. 4.4",
    keywords: ["Turtle", "Prozessdiagramm", "Input", "Output", "Schildkrötenmodell", "Prozessanalyse"]
  },
  {
    id: "term-10",
    term: "Interessierte Parteien (Stakeholder)",
    definition: "Personen oder Organisationen, die eine Entscheidung oder Tätigkeit beeinflussen können, von ihr beeinflusst werden können oder sich davon beeinflusst fühlen (z.B. Kunden, Behörden, Mitarbeiter, Lieferanten).",
    category: "Kontext & Organisation",
    isoRef: "ISO 9000:2015 Abs. 3.2.3 / ISO 9001 Kap. 4.2",
    keywords: ["Stakeholder", "Interessierte Parteien", "Kunden", "Lieferanten", "Anforderungen"]
  },
  {
    id: "term-11",
    term: "Korrektur vs. Korrekturmaßnahme",
    definition: "Korrektur behebt das akute Symptom (z.B. Nacharbeit am fehlerhaften Teil). Korrekturmaßnahme (CAPA) beseitigt die Grundursache, damit der Fehler nicht wiederkehrt.",
    category: "Verbesserung & KVP",
    isoRef: "ISO 9000:2015 Abs. 3.12.9 & 3.12.10 / ISO 9001 Kap. 10.2",
    keywords: ["Korrektur", "Korrekturmaßnahme", "CAPA", "Ursachenbeseitigung", "Fehlerbehebung"]
  },
  {
    id: "term-12",
    term: "Verifizierung vs. Validierung",
    definition: "Verifizierung: Bestätigung durch Bereitstellung objektiver Nachweise, dass festgelegte Anforderungen erfüllt wurden ('Wurde das Produkt richtig gebaut?'). Validierung: Bestätigung, dass die Anforderungen für einen spezifischen beabsichtigten Gebrauch erfüllt sind ('Wurde das richtige Produkt gebaut?').",
    category: "Produktrealisierung",
    isoRef: "ISO 9000:2015 Abs. 3.8.12 & 3.8.13 / ISO 9001 Kap. 8.3.4",
    keywords: ["Verifizierung", "Validierung", "Produktprüfung", "Konformitätsnachweis"]
  },
  {
    id: "term-13",
    term: "7 Qualitätsmanagement-Grundsätze (QMP)",
    definition: "1. Kundenorientierung, 2. Führung, 3. Engagement von Personen, 4. Prozessorientierter Ansatz, 5. Verbesserung, 6. Faktengestützte Entscheidungsfindung, 7. Beziehungsmanagement.",
    category: "QM-Grundlagen",
    isoRef: "DIN EN ISO 9000:2015 Kap. 2.3",
    keywords: ["Grundsätze", "Kundenorientierung", "Führung", "Faktengestützt", "Beziehungsmanagement"]
  },
  {
    id: "term-14",
    term: "8D-Report (8 Disziplinen)",
    definition: "Standardisierter Problemlösungsprozess: D1 Team bilden, D2 Problem beschreiben, D3 Sofortmaßnahmen, D4 Ursachenanalyse, D5 Abstellmaßnahmen auswählen, D6 Maßnahmen einführen, D7 Wiederauftreten verhindern, D8 Teamerfolg würdigen.",
    category: "QM-Werkzeuge & Methoden",
    isoRef: "VDA Band 4 / ISO 9001 Kap. 10.2",
    keywords: ["8D", "8D-Report", "Reklamation", "Ursachenanalyse", "VDA"]
  },
  {
    id: "term-15",
    term: "FMEA (Fehlermöglichkeits- und Einflussanalyse)",
    definition: "Präventive analytische Methode zur Ermittlung potenzieller Fehlerursachen, Fehlerfolgen und deren Risikobewertung mittels Risikoprioritätszahl (RPZ = Auftretenswahrscheinlichkeit x Bedeutung x Entdeckungswahrscheinlichkeit).",
    category: "Risikomanagement",
    isoRef: "DIN EN IEC 60812 / ISO 9001 Kap. 6.1",
    keywords: ["FMEA", "RPZ", "Design-FMEA", "Prozess-FMEA", "Risikobewertung"]
  },
  {
    id: "term-16",
    term: "Akkreditierung vs. Zertifizierung",
    definition: "Zertifizierung: Bestätigung durch eine unabhängige Zertifizierungsstelle, dass ein Managementsystem einer Norm entspricht. Akkreditierung: Staatliche Bestätigung (in DE: DAkkS), dass eine Zertifizierungsstelle fachlich kompetent ist.",
    category: "Normung & Struktur",
    isoRef: "ISO/IEC 17011 & ISO/IEC 17021 / DAkkS",
    keywords: ["Akkreditierung", "Zertifizierung", "DAkkS", "Zertifizierer", "Audit"]
  },
  {
    id: "term-17",
    term: "5S-Methode",
    definition: "Arbeitsplatzorganisation in 5 Schritten: 1. Seiri (Aussortieren), 2. Seiton (Aufräumen/Ordnung), 3. Seiso (Saubermachen), 4. Seiketsu (Standardisieren), 5. Shitsuke (Selbstdisziplin).",
    category: "QM-Werkzeuge & Methoden",
    isoRef: "Lean Management / ISO 9001 Kap. 7.1.4",
    keywords: ["5S", "Arbeitsplatzorganisation", "Lean", "Ordnung", "Sauberkeit"]
  },
  {
    id: "term-18",
    term: "7 Verschwendungsarten (Muda)",
    definition: "Lean-Konzept zur Beseitigung nicht-wertschöpfender Aktivitäten: 1. Überproduktion, 2. Bestände, 3. Transport, 4. Wartezeiten, 5. Aufwendige Prozesse/Überbearbeitung, 6. Bewegung, 7. Ausschuss/Nacharbeit.",
    category: "Verbesserung & KVP",
    isoRef: "Toyota Production System (TPS) / Lean",
    keywords: ["Muda", "Verschwendung", "Lean", "Überproduktion", "Nacharbeit"]
  },
  {
    id: "term-19",
    term: "Oberste Leitung (Top Management)",
    definition: "Person oder Personengruppe, die eine Organisation auf oberster Ebene führt und steuert. Trägt die uneingeschränkte Gesamt- und Rechenschaftspflicht für die Wirksamkeit des QMS nach ISO 9001:2015.",
    category: "Führung & Bewertung",
    isoRef: "ISO 9000:2015 Abs. 3.1.1 / ISO 9001 Kap. 5.1",
    keywords: ["Oberste Leitung", "Top Management", "Führung", "Rechenschaftspflicht", "Verantwortung"]
  },
  {
    id: "term-20",
    term: "Qualitätspolitik & Qualitätsziele",
    definition: "Qualitätspolitik: Gesamtabsichten und Ausrichtung der Organisation zur Qualität, formell durch die oberste Leitung ausgedrückt. Qualitätsziele: Messbare, aus der Politik abgeleitete Ziele auf relevanten Funktionsebenen.",
    category: "Führung & Bewertung",
    isoRef: "ISO 9001:2015 Kap. 5.2 & 6.2",
    keywords: ["Qualitätspolitik", "Qualitätsziele", "Messbarkeit", "Zielvereinbarung"]
  }
];
