import React, { useState, useEffect } from 'react';
import { Award, Clock, CheckCircle2, XCircle, ShieldAlert, RotateCcw, ArrowRight } from 'lucide-react';

export default function ExamModeView({ questions }) {
  const [examActive, setExamActive] = useState(false);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [userAnswers, setUserAnswers] = useState({});
  const [timeLeft, setTimeLeft] = useState(600); // 10 min
  const [finished, setFinished] = useState(false);

  useEffect(() => {
    let timer;
    if (examActive && !finished && timeLeft > 0) {
      timer = setInterval(() => {
        setTimeLeft((prev) => {
          if (prev <= 1) {
            setFinished(true);
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    }
    return () => clearInterval(timer);
  }, [examActive, finished, timeLeft]);

  const startExam = () => {
    setExamActive(true);
    setCurrentIndex(0);
    setUserAnswers({});
    setTimeLeft(600);
    setFinished(false);
  };

  const currentQ = questions[currentIndex];

  const handleSelectOption = (optId) => {
    if (finished) return;
    const currentSel = userAnswers[currentQ.id] || [];
    let updated;
    if (currentQ.multipleChoice) {
      updated = currentSel.includes(optId)
        ? currentSel.filter(id => id !== optId)
        : [...currentSel, optId];
    } else {
      updated = [optId];
    }
    setUserAnswers({ ...userAnswers, [currentQ.id]: updated });
  };

  const handleFinish = () => {
    setFinished(true);
  };

  // Calculate score
  let correctCount = 0;
  questions.forEach(q => {
    const sel = userAnswers[q.id] || [];
    const correctIds = q.options.filter(o => o.isCorrect).map(o => o.id);
    const isCorrect = sel.length === correctIds.length && sel.every(id => correctIds.includes(id));
    if (isCorrect) correctCount++;
  });

  const percentage = Math.round((correctCount / questions.length) * 100) || 0;
  const passed = percentage >= 75; // TÜV pass mark is 75%

  const formatTime = (secs) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m}:${s < 10 ? '0' : ''}${s}`;
  };

  if (!examActive) {
    return (
      <div className="glass-panel" style={{ padding: '40px', textAlign: 'center', maxWidth: '640px', margin: '0 auto' }}>
        <div style={{ width: '64px', height: '64px', borderRadius: '16px', background: 'rgba(99, 102, 241, 0.2)', display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 20px auto' }}>
          <Award size={36} color="#a5b4fc" />
        </div>
        <h2 style={{ fontSize: '1.6rem', fontWeight: 800, color: '#ffffff', marginBottom: '12px' }}>
          TÜV QMB Prüfungs-Simulation
        </h2>
        <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem', marginBottom: '24px', lineHeight: '1.6' }}>
          Teste dein Wissen unter realistischen Prüfungsbedingungen! 
          <br />• <strong>{questions.length} Fragen</strong> aus allen ISO 9001 Bereichen
          <br />• Zeitlimit: <strong>10 Minuten</strong>
          <br />• Bestehensgrenze: <strong>75% der Gesamtpunkte</strong>
        </p>
        <button onClick={startExam} className="btn-primary" style={{ fontSize: '1.1rem', padding: '14px 32px' }}>
          Prüfungssimulation jetzt starten
        </button>
      </div>
    );
  }

  if (finished) {
    return (
      <div className="glass-panel" style={{ padding: '32px' }}>
        <div style={{ textAlign: 'center', marginBottom: '32px' }}>
          <div style={{ fontSize: '3.5rem', marginBottom: '8px' }}>
            {passed ? '🎉' : '⚠️'}
          </div>
          <h2 style={{ fontSize: '1.8rem', fontWeight: 800, color: passed ? '#6ee7b7' : '#fca5a5', marginBottom: '8px' }}>
            {passed ? 'TÜV-Prüfung BESTANDEN!' : 'TÜV-Prüfung NICHT BESTANDEN'}
          </h2>
          <div style={{ fontSize: '2.5rem', fontWeight: 900, color: '#ffffff', marginBottom: '8px' }}>
            {percentage}% <span style={{ fontSize: '1.1rem', color: 'var(--text-muted)' }}>({correctCount} von {questions.length} richtig)</span>
          </div>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>
            {passed ? 'Hervorragende Leistung! Du erfüllst die Anforderungen nach DIN EN ISO 9001:2015.' : 'Mindestens 75% erforderlich. Nutze den Stapel-Trainer, um Schwachstellen aufzufrischen.'}
          </p>
          <button onClick={startExam} className="btn-primary" style={{ marginTop: '16px' }}>
            <RotateCcw size={18} /> Prüfung erneut ablegen
          </button>
        </div>

        {/* Detailed Question Breakdown */}
        <h3 style={{ fontSize: '1.1rem', fontWeight: 700, color: '#ffffff', marginBottom: '16px' }}>
          Detaillierte Auswertung & ISO 9001 Begründungen:
        </h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {questions.map((q, idx) => {
            const sel = userAnswers[q.id] || [];
            const correctIds = q.options.filter(o => o.isCorrect).map(o => o.id);
            const isCorrect = sel.length === correctIds.length && sel.every(id => correctIds.includes(id));
            return (
              <div key={q.id} className="glass-card" style={{ padding: '20px', borderLeft: isCorrect ? '4px solid #10b981' : '4px solid #ef4444' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
                  <span style={{ fontWeight: 700, color: '#ffffff' }}>Frage {idx + 1}: {q.question}</span>
                  {isCorrect ? <CheckCircle2 size={20} color="#10b981" /> : <XCircle size={20} color="#ef4444" />}
                </div>
                <div style={{ fontSize: '0.85rem', color: '#c7d2fe', background: 'rgba(99, 102, 241, 0.1)', padding: '8px 12px', borderRadius: '6px' }}>
                  <strong>ISO Begründung:</strong> {q.isoJustification}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    );
  }

  return (
    <div className="glass-panel" style={{ padding: '32px' }}>
      {/* Header bar */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '24px', flexWrap: 'wrap', gap: '12px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <span className="badge badge-purple">Frage {currentIndex + 1} von {questions.length}</span>
          <span className="badge badge-amber">{currentQ.isoClause}</span>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '8px 16px', borderRadius: '10px', background: 'rgba(239, 68, 68, 0.15)', border: '1px solid rgba(239, 68, 68, 0.3)', color: '#fca5a5', fontWeight: 700, fontSize: '1rem' }}>
          <Clock size={18} /> Verbleibende Zeit: {formatTime(timeLeft)}
        </div>
      </div>

      {/* Question */}
      <h2 style={{ fontSize: '1.25rem', fontWeight: 700, color: '#ffffff', marginBottom: '20px' }}>
        {currentQ.question}
      </h2>

      {/* Options */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginBottom: '28px' }}>
        {currentQ.options.map(opt => {
          const isSel = (userAnswers[currentQ.id] || []).includes(opt.id);
          return (
            <div
              key={opt.id}
              onClick={() => handleSelectOption(opt.id)}
              style={{
                padding: '14px 18px',
                borderRadius: '12px',
                border: isSel ? '2px solid #6366f1' : '1px solid rgba(255, 255, 255, 0.1)',
                background: isSel ? 'rgba(99, 102, 241, 0.2)' : 'rgba(30, 41, 59, 0.5)',
                color: '#ffffff',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '12px'
              }}
            >
              <div style={{
                width: '22px',
                height: '22px',
                borderRadius: currentQ.multipleChoice ? '4px' : '50%',
                border: isSel ? '2px solid #6366f1' : '2px solid rgba(255, 255, 255, 0.3)',
                background: isSel ? '#6366f1' : 'transparent',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontWeight: 700,
                fontSize: '0.8rem'
              }}>
                {opt.id}
              </div>
              <span>{opt.text}</span>
            </div>
          );
        })}
      </div>

      {/* Navigation */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <button
          onClick={() => setCurrentIndex(prev => Math.max(0, prev - 1))}
          disabled={currentIndex === 0}
          className="btn-secondary"
          style={{ opacity: currentIndex === 0 ? 0.5 : 1 }}
        >
          Vorherige Frage
        </button>

        {currentIndex < questions.length - 1 ? (
          <button onClick={() => setCurrentIndex(prev => prev + 1)} className="btn-primary">
            Nächste Frage <ArrowRight size={16} />
          </button>
        ) : (
          <button onClick={handleFinish} className="btn-primary" style={{ background: 'linear-gradient(135deg, #10b981 0%, #059669 100%)' }}>
            Prüfung jetzt abgeben & auswerten
          </button>
        )}
      </div>
    </div>
  );
}
