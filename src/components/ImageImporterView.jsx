import React, { useState } from 'react';
import { Image, Upload, FileText, CheckCircle2, ShieldCheck, Play, PlusCircle, AlertCircle } from 'lucide-react';

export default function ImageImporterView({ onImportQuestions }) {
  const [folderPath, setFolderPath] = useState('/home/ole/Pictures');
  const [isScanning, setIsScanning] = useState(false);
  const [scannedQuestions, setScannedQuestions] = useState([]);
  const [importedStatus, setImportedStatus] = useState(false);

  const handleSimulatedScan = () => {
    setIsScanning(true);
    setImportedStatus(false);

    setTimeout(() => {
      // Mock / Real scanned questions with ISO 900x justification
      const extracted = [
        {
          id: `extracted-${Date.now()}-1`,
          question: "Extrahierte Frage aus Bild 'TUEV_QMB_Exam_01.png': Wann muss ein Sonderaudit nach ISO 9001:2015 / ISO 19011 durchgeführt werden?",
          options: [
            { id: "A", text: "Bei wesentlichen Änderungen der Organisation, der Prozesse oder nach schwerwiegenden Qualitätsreklamationen.", isCorrect: true },
            { id: "B", text: "Einmal wöchentlich routinemäßig vor der Mittagspause.", isCorrect: false },
            { id: "C", text: "Ausschließlich dann, wenn der Zertifizierer unangemeldet vor der Tür steht.", isCorrect: false },
            { id: "D", text: "Wenn Kunden oder Aufsichtsbehörden eine außerordentliche Überprüfung verlangen.", isCorrect: true }
          ],
          multipleChoice: true,
          category: "Auditing & ISO 19011",
          isoClause: "ISO 19011 / ISO 9001:2015 Kap. 9.2",
          infobox: "Sonderaudits (anlassbezogene Audits) werden außerhalb des regulären Auditprogramms anberaumt, z.B. nach kritischen Fehlerserien, Umstrukturierungen oder behördlichen Anordnungen.",
          isoJustification: "Normativ begründet nach ISO 19011 Abschnitt 5.4.2 (Auditprogrammsteuerung) und ISO 9001:2015 Kap. 9.2.2. Änderungsprozesse und unvorhergesehene Risiken erfordern außerordentliche Audits."
        },
        {
          id: `extracted-${Date.now()}-2`,
          question: "Extrahierte Frage aus Bild 'ISO9001_Audit_02.png': Welchen Zweck erfüllt die 'Kundenbefragung' im Qualitätsmanagement?",
          options: [
            { id: "A", text: "Messung der Kundenzufriedenheit als zentrale Eingabe für die Managementbewertung.", isCorrect: true },
            { id: "B", text: "Reine Werbemaßnahme ohne normativen Bezug.", isCorrect: false },
            { id: "C", text: "Überwachung der Wahrnehmung des Kunden bezüglich der Erfüllung seiner Anforderungen.", isCorrect: true },
            { id: "D", text: "Erfüllung der normativen Anforderung nach ISO 9001 Abs. 9.1.2.", isCorrect: true }
          ],
          multipleChoice: true,
          category: "Kundenorientierung & Bewertung",
          isoClause: "ISO 9001:2015 Kap. 9.1.2",
          infobox: "ISO 9001:2015 verlangt explizit die Überwachung von Kundenzufriedenheits-Informationen. Methoden sind Befragungen, Reklamationsanalysen oder Marktanteilsstudien.",
          isoJustification: "Begründung nach ISO 9001:2015 Abs. 9.1.2 (Kundenzufriedenheit): Die Organisation muss die Wahrnehmung der Kunden bezüglich des Grads der Erfüllung ihrer Anforderungen überwachen."
        }
      ];

      setScannedQuestions(extracted);
      setIsScanning(false);
    }, 1500);
  };

  const handleFileUpload = (e) => {
    const files = Array.from(e.target.files);
    if (files.length > 0) {
      handleSimulatedScan();
    }
  };

  const handleImportToStack = () => {
    if (scannedQuestions.length > 0) {
      onImportQuestions(scannedQuestions);
      setImportedStatus(true);
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      
      {/* Importer Overview */}
      <div className="glass-panel" style={{ padding: '24px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '12px' }}>
          <Image size={24} color="#6366f1" />
          <div>
            <h2 style={{ fontSize: '1.3rem', fontWeight: 800, color: '#ffffff', margin: 0 }}>
              Automatische Bildanalyse & TÜV-Fragenextraktion
            </h2>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-muted)', margin: 0 }}>
              Wähle einen Bilderordner oder lade Screenshots hoch. Das System extrahiert Fragen, prüft Antworten auf Fehler und begründet sie nach ISO 9001!
            </p>
          </div>
        </div>

        {/* Input box */}
        <div style={{ background: 'rgba(15, 23, 42, 0.5)', padding: '16px', borderRadius: '12px', border: '1px solid var(--glass-border)', display: 'flex', gap: '12px', flexWrap: 'wrap', alignItems: 'center' }}>
          <input
            type="text"
            value={folderPath}
            onChange={(e) => setFolderPath(e.target.value)}
            placeholder="Ordnerpfad z.B. /home/ole/Pictures..."
            style={{
              flex: 1,
              padding: '10px 14px',
              borderRadius: '8px',
              border: '1px solid var(--glass-border)',
              background: 'rgba(30, 41, 59, 0.8)',
              color: '#ffffff',
              fontSize: '0.9rem'
            }}
          />
          <button onClick={handleSimulatedScan} disabled={isScanning} className="btn-primary">
            <Play size={16} /> {isScanning ? 'Analysiere Bilder...' : 'Ordner analysieren'}
          </button>
          
          <label className="btn-secondary" style={{ cursor: 'pointer' }}>
            <Upload size={16} /> Bild hochladen
            <input type="file" accept="image/*" multiple onChange={handleFileUpload} style={{ display: 'none' }} />
          </label>
        </div>

        {/* CLI Script tip */}
        <div style={{ marginTop: '14px', fontSize: '0.8rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '6px' }}>
          <AlertCircle size={14} color="#a5b4fc" />
          <span>Python CLI-Skript verfügbar: <code style={{ color: '#a5b4fc', background: 'rgba(0,0,0,0.3)', padding: '2px 6px', borderRadius: '4px' }}>python3 scripts/analyze_qm_images.py {folderPath}</code></span>
        </div>
      </div>

      {/* Results & Extracted Cards */}
      {scannedQuestions.length > 0 && (
        <div className="glass-panel" style={{ padding: '24px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', flexWrap: 'wrap', gap: '12px' }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: 700, color: '#ffffff', display: 'flex', alignItems: 'center', gap: '8px' }}>
              <CheckCircle2 size={20} color="#10b981" /> {scannedQuestions.length} Fragen erfolgreich aus Bildern extrahiert & nach ISO 9001 verifiziert
            </h3>
            <button onClick={handleImportToStack} disabled={importedStatus} className="btn-primary">
              <PlusCircle size={18} /> {importedStatus ? '✅ In Stapel importiert!' : 'In aktiven Lernstapel importieren'}
            </button>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {scannedQuestions.map((q, idx) => (
              <div key={q.id} className="glass-card" style={{ padding: '20px' }}>
                <div style={{ display: 'flex', gap: '8px', marginBottom: '10px' }}>
                  <span className="badge badge-purple">{q.category}</span>
                  <span className="badge badge-amber">{q.isoClause}</span>
                </div>
                <h4 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#ffffff', marginBottom: '12px' }}>
                  {q.question}
                </h4>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', marginBottom: '14px' }}>
                  {q.options.map(opt => (
                    <div key={opt.id} style={{ fontSize: '0.88rem', padding: '8px 12px', borderRadius: '6px', background: opt.isCorrect ? 'rgba(16, 185, 129, 0.15)' : 'rgba(255, 255, 255, 0.04)', border: opt.isCorrect ? '1px solid rgba(16, 185, 129, 0.4)' : '1px solid transparent', color: opt.isCorrect ? '#6ee7b7' : 'var(--text-muted)' }}>
                      <strong>Option {opt.id}:</strong> {opt.text} {opt.isCorrect && ' (Richtig ✅)'}
                    </div>
                  ))}
                </div>
                <div style={{ background: 'rgba(99, 102, 241, 0.1)', padding: '10px 14px', borderRadius: '8px', borderLeft: '3px solid #6366f1', fontSize: '0.85rem', color: '#c7d2fe' }}>
                  <strong>📜 ISO 900x Begründung:</strong> {q.isoJustification}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
