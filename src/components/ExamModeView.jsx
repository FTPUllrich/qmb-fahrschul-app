import React, { useState, useEffect } from 'react';
import { Award, Clock, CheckCircle2, XCircle, ShieldAlert, RotateCcw, ArrowRight, ArrowLeft, Filter, Sparkles, Check, ChevronRight } from 'lucide-react';

export default function ExamModeView({ questions }) {
  const [examActive, setExamActive] = useState(false);
  const [examMode, setExamMode] = useState('standard'); // 'standard' (30 Q), 'compact' (15 Q), 'all' (all Q)
  const [activeQuestions, setActiveQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [userAnswers, setUserAnswers] = useState({});
  const [timeLeft, setTimeLeft] = useState(1800); // in seconds
  const [initialTime, setInitialTime] = useState(1800);
  const [finished, setFinished] = useState(false);
  const [filterReview, setFilterReview] = useState('ALL'); // 'ALL', 'WRONG', 'CORRECT'

  // Timer countdown
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

  // Start exam with randomized, balanced selection
  const startExam = (mode = examMode) => {
    let count = 30;
    let duration = 45 * 60; // 45 min for 30 questions

    if (mode === 'compact') {
      count = 15;
      duration = 20 * 60; // 20 min
    } else if (mode === 'all') {
      count = questions.length;
      duration = Math.max(60 * 60, questions.length * 60); // 1 min per question
    }

    // Shuffle and pick
    const shuffled = [...questions].sort(() => Math.random() - 0.5);
    const selected = shuffled.slice(0, Math.min(count, shuffled.length));

    setActiveQuestions(selected);
    setExamMode(mode);
    setExamActive(true);
    setCurrentIndex(0);
    setUserAnswers({});
    setTimeLeft(duration);
    setInitialTime(duration);
    setFinished(false);
    setFilterReview('ALL');
  };

  const currentQ = activeQuestions[currentIndex];

  const handleSelectOption = (optId) => {
    if (finished || !currentQ) return;
    const currentSel = userAnswers[currentQ.id] || [];
    const updated = currentSel.includes(optId)
      ? currentSel.filter(id => id !== optId)
      : [...currentSel, optId];
    setUserAnswers({ ...userAnswers, [currentQ.id]: updated });
  };

  const handleFinish = () => {
    if (window.confirm('Möchtest du die Prüfung jetzt wirklich abgeben und auswerten lassen?')) {
      setFinished(true);
    }
  };

  // Score calculation
  let correctCount = 0;
  const categoryResults = {};

  activeQuestions.forEach(q => {
    const sel = userAnswers[q.id] || [];
    const correctIds = q.options.filter(o => o.isCorrect).map(o => o.id);
    const isCorrect = sel.length === correctIds.length && sel.every(id => correctIds.includes(id));
    if (isCorrect) correctCount++;

    const cat = q.category || 'Allgemein';
    if (!categoryResults[cat]) {
      categoryResults[cat] = { total: 0, correct: 0 };
    }
    categoryResults[cat].total += 1;
    if (isCorrect) categoryResults[cat].correct += 1;
  });

  const totalExamQuestions = activeQuestions.length || 1;
  const percentage = Math.round((correctCount / totalExamQuestions) * 100) || 0;
  const passed = percentage >= 75; // TÜV pass mark is 75%

  const formatTime = (secs) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m}:${s < 10 ? '0' : ''}${s}`;
  };

  // Intro selection screen
  if (!examActive) {
    return (
      <div className="glass-panel" style={{ padding: '40px', textAlign: 'center', maxWidth: '720px', margin: '0 auto' }}>
        <div style={{ width: '72px', height: '72px', borderRadius: '20px', background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.3) 0%, rgba(168, 85, 247, 0.3) 100%)', display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 24px auto', border: '1px solid rgba(168, 85, 247, 0.4)' }}>
          <Award size={40} color="#a5b4fc" />
        </div>
        
        <h2 style={{ fontSize: '1.75rem', fontWeight: 800, color: '#ffffff', marginBottom: '12px' }}>
          TÜV QMB Prüfungs-Simulation
        </h2>
        
        <p style={{ color: 'var(--text-muted)', fontSize: '0.98rem', marginBottom: '32px', lineHeight: '1.6' }}>
          Teste dein Wissen unter authentischen TÜV-Prüfungsbedingungen. Die Fragen werden zufällig aus dem Pool von <strong>{questions.length} ISO 9001 Fragen</strong> gezogen.
        </p>

        {/* Mode Selector Cards */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '16px', marginBottom: '32px', textAlign: 'left' }}>
          
          <div
            onClick={() => setExamMode('standard')}
            className="glass-card"
            style={{
              padding: '20px',
              cursor: 'pointer',
              border: examMode === 'standard' ? '2px solid #6366f1' : '1px solid var(--glass-border)',
              background: examMode === 'standard' ? 'rgba(99, 102, 241, 0.15)' : 'rgba(30, 41, 59, 0.5)',
              transition: 'all 0.2s ease'
            }}
          >
            <div style={{ fontWeight: 700, color: '#ffffff', fontSize: '1.1rem', marginBottom: '6px' }}>
              🎓 TÜV-Standard
            </div>
            <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginBottom: '8px' }}>
              • <strong>30 Fragen</strong> gemischt<br />
              • Zeit: <strong>45 Minuten</strong><br />
              • Bestehen: <strong>75 %</strong>
            </div>
            <span className="badge badge-purple" style={{ fontSize: '0.72rem' }}>Empfohlen</span>
          </div>

          <div
            onClick={() => setExamMode('compact')}
            className="glass-card"
            style={{
              padding: '20px',
              cursor: 'pointer',
              border: examMode === 'compact' ? '2px solid #6366f1' : '1px solid var(--glass-border)',
              background: examMode === 'compact' ? 'rgba(99, 102, 241, 0.15)' : 'rgba(30, 41, 59, 0.5)',
              transition: 'all 0.2s ease'
            }}
          >
            <div style={{ fontWeight: 700, color: '#ffffff', fontSize: '1.1rem', marginBottom: '6px' }}>
              ⚡ Speed-Check
            </div>
            <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginBottom: '8px' }}>
              • <strong>15 Fragen</strong> Quick-Check<br />
              • Zeit: <strong>20 Minuten</strong><br />
              • Bestehen: <strong>75 %</strong>
            </div>
            <span className="badge badge-amber" style={{ fontSize: '0.72rem' }}>Schnelltest</span>
          </div>

          <div
            onClick={() => setExamMode('all')}
            className="glass-card"
            style={{
              padding: '20px',
              cursor: 'pointer',
              border: examMode === 'all' ? '2px solid #6366f1' : '1px solid var(--glass-border)',
              background: examMode === 'all' ? 'rgba(99, 102, 241, 0.15)' : 'rgba(30, 41, 59, 0.5)',
              transition: 'all 0.2s ease'
            }}
          >
            <div style={{ fontWeight: 700, color: '#ffffff', fontSize: '1.1rem', marginBottom: '6px' }}>
              📚 Marathon-Pool
            </div>
            <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginBottom: '8px' }}>
              • <strong>Alle {questions.length} Fragen</strong><br />
              • Zeit: <strong>60+ Minuten</strong><br />
              • Voller Härtetest
            </div>
            <span className="badge badge-green" style={{ fontSize: '0.72rem' }}>Komplett</span>
          </div>
        </div>

        <button onClick={() => startExam(examMode)} className="btn-primary" style={{ fontSize: '1.1rem', padding: '16px 36px' }}>
          Prüfungssimulation jetzt starten <ArrowRight size={20} />
        </button>
      </div>
    );
  }

  // Result view after completion
  if (finished) {
    const answeredCount = Object.keys(userAnswers).length;
    const filteredQuestions = activeQuestions.filter(q => {
      const sel = userAnswers[q.id] || [];
      const correctIds = q.options.filter(o => o.isCorrect).map(o => o.id);
      const isCorrect = sel.length === correctIds.length && sel.every(id => correctIds.includes(id));
      if (filterReview === 'WRONG') return !isCorrect;
      if (filterReview === 'CORRECT') return isCorrect;
      return true;
    });

    return (
      <div className="glass-panel" style={{ padding: '32px' }}>
        {/* Results Banner */}
        <div style={{ textAlign: 'center', padding: '24px', background: passed ? 'rgba(16, 185, 129, 0.12)' : 'rgba(239, 68, 68, 0.12)', borderRadius: '16px', border: passed ? '1px solid rgba(16, 185, 129, 0.4)' : '1px solid rgba(239, 68, 68, 0.4)', marginBottom: '32px' }}>
          <div style={{ fontSize: '3.5rem', marginBottom: '8px' }}>
            {passed ? '🎉' : '⚠️'}
          </div>
          <h2 style={{ fontSize: '1.9rem', fontWeight: 800, color: passed ? '#6ee7b7' : '#fca5a5', marginBottom: '8px' }}>
            {passed ? 'TÜV-Zertifikatsprüfung BESTANDEN!' : 'TÜV-Zertifikatsprüfung NICHT BESTANDEN'}
          </h2>
          <div style={{ fontSize: '2.8rem', fontWeight: 900, color: '#ffffff', marginBottom: '8px' }}>
            {percentage}% <span style={{ fontSize: '1.15rem', color: 'var(--text-muted)' }}>({correctCount} von {totalExamQuestions} Punkten)</span>
          </div>
          <p style={{ color: '#e5e7eb', fontSize: '0.95rem', maxWidth: '600px', margin: '0 auto 16px auto' }}>
            {passed
              ? 'Ausgezeichnet! Deine Kenntnisse zu DIN EN ISO 9001:2015, ISO 9000 und den Auditmethoden nach ISO 19011 erfüllen die offiziellen TÜV-Kriterien.'
              : 'Zur Zertifizierung sind mindestens 75 % korrekte Antworten erforderlich. Nutze die ISO-Begründungen unten und den Fahrschul-Stapel, um deine Lücken zu schließen.'}
          </p>
          <button onClick={() => startExam(examMode)} className="btn-primary">
            <RotateCcw size={18} /> Neue Prüfungssimulation starten
          </button>
        </div>

        {/* Category Breakdown */}
        <div className="glass-card" style={{ padding: '20px', marginBottom: '28px' }}>
          <h3 style={{ fontSize: '1.1rem', fontWeight: 700, color: '#ffffff', marginBottom: '16px' }}>
            Ergebnis nach ISO-Kapiteln:
          </h3>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '12px' }}>
            {Object.entries(categoryResults).map(([cat, res]) => {
              const catRate = res.total > 0 ? Math.round((res.correct / res.total) * 100) : 0;
              return (
                <div key={cat} style={{ background: 'rgba(15, 23, 42, 0.6)', padding: '12px 16px', borderRadius: '10px', border: '1px solid var(--glass-border)' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', marginBottom: '6px' }}>
                    <span style={{ fontWeight: 600, color: '#ffffff' }}>{cat}</span>
                    <span style={{ color: catRate >= 75 ? '#6ee7b7' : '#fca5a5' }}>{res.correct}/{res.total} ({catRate}%)</span>
                  </div>
                  <div style={{ width: '100%', height: '6px', borderRadius: '3px', background: 'rgba(255, 255, 255, 0.1)', overflow: 'hidden' }}>
                    <div style={{ width: `${catRate}%`, height: '100%', background: catRate >= 75 ? '#10b981' : '#ef4444', borderRadius: '3px' }} />
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Question Review Section with Filter */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', flexWrap: 'wrap', gap: '12px' }}>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 700, color: '#ffffff', margin: 0 }}>
            Detaillierte Auswertung & ISO-Normbegründungen ({filteredQuestions.length} Fragen):
          </h3>
          
          <div style={{ display: 'flex', gap: '8px' }}>
            <button
              onClick={() => setFilterReview('ALL')}
              style={{
                padding: '6px 14px',
                borderRadius: '8px',
                border: '1px solid var(--glass-border)',
                background: filterReview === 'ALL' ? '#6366f1' : 'rgba(30, 41, 59, 0.6)',
                color: '#ffffff',
                fontSize: '0.82rem',
                cursor: 'pointer'
              }}
            >
              Alle ({activeQuestions.length})
            </button>
            <button
              onClick={() => setFilterReview('WRONG')}
              style={{
                padding: '6px 14px',
                borderRadius: '8px',
                border: '1px solid rgba(239, 68, 68, 0.4)',
                background: filterReview === 'WRONG' ? '#ef4444' : 'rgba(30, 41, 59, 0.6)',
                color: filterReview === 'WRONG' ? '#ffffff' : '#fca5a5',
                fontSize: '0.82rem',
                cursor: 'pointer'
              }}
            >
              Falsch ({activeQuestions.length - correctCount})
            </button>
            <button
              onClick={() => setFilterReview('CORRECT')}
              style={{
                padding: '6px 14px',
                borderRadius: '8px',
                border: '1px solid rgba(16, 185, 129, 0.4)',
                background: filterReview === 'CORRECT' ? '#10b981' : 'rgba(30, 41, 59, 0.6)',
                color: filterReview === 'CORRECT' ? '#ffffff' : '#6ee7b7',
                fontSize: '0.82rem',
                cursor: 'pointer'
              }}
            >
              Richtig ({correctCount})
            </button>
          </div>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {filteredQuestions.map((q, idx) => {
            const sel = userAnswers[q.id] || [];
            const correctIds = q.options.filter(o => o.isCorrect).map(o => o.id);
            const isCorrect = sel.length === correctIds.length && sel.every(id => correctIds.includes(id));
            
            return (
              <div key={q.id} className="glass-card" style={{ padding: '20px', borderLeft: isCorrect ? '4px solid #10b981' : '4px solid #ef4444' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '12px', marginBottom: '12px' }}>
                  <div>
                    <div style={{ display: 'flex', gap: '8px', marginBottom: '6px', flexWrap: 'wrap' }}>
                      <span className="badge badge-purple">{q.category}</span>
                      <span className="badge badge-amber">{q.isoClause}</span>
                    </div>
                    <h4 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#ffffff', margin: 0 }}>
                      {q.question}
                    </h4>
                  </div>
                  {isCorrect ? (
                    <div style={{ display: 'flex', alignItems: 'center', gap: '6px', color: '#10b981', fontWeight: 700, fontSize: '0.9rem', flexShrink: 0 }}>
                      <CheckCircle2 size={22} color="#10b981" /> Richtig
                    </div>
                  ) : (
                    <div style={{ display: 'flex', alignItems: 'center', gap: '6px', color: '#ef4444', fontWeight: 700, fontSize: '0.9rem', flexShrink: 0 }}>
                      <XCircle size={22} color="#ef4444" /> Abweichung
                    </div>
                  )}
                </div>

                {/* Options overview */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', marginBottom: '14px' }}>
                  {q.options.map(opt => {
                    const isSelected = sel.includes(opt.id);
                    let bg = 'rgba(255, 255, 255, 0.04)';
                    let border = '1px solid transparent';
                    let textCol = 'var(--text-muted)';

                    if (opt.isCorrect) {
                      bg = 'rgba(16, 185, 129, 0.15)';
                      border = '1px solid rgba(16, 185, 129, 0.4)';
                      textCol = '#6ee7b7';
                    } else if (isSelected && !opt.isCorrect) {
                      bg = 'rgba(239, 68, 68, 0.2)';
                      border = '1px solid rgba(239, 68, 68, 0.5)';
                      textCol = '#fca5a5';
                    }

                    return (
                      <div key={opt.id} style={{ padding: '10px 14px', borderRadius: '8px', background: bg, border: border, color: textCol, fontSize: '0.9rem', display: 'flex', alignItems: 'center', gap: '10px' }}>
                        <span style={{ fontWeight: 700 }}>{opt.id}:</span>
                        <span style={{ flexGrow: 1 }}>{opt.text}</span>
                        {opt.isCorrect && <span style={{ fontSize: '0.78rem', fontWeight: 700, color: '#10b981' }}>[Soll: Richtig]</span>}
                        {isSelected && <span style={{ fontSize: '0.78rem', fontWeight: 700, color: opt.isCorrect ? '#10b981' : '#ef4444' }}>[Deine Wahl]</span>}
                      </div>
                    );
                  })}
                </div>

                {/* ISO Justification */}
                <div style={{ background: 'rgba(99, 102, 241, 0.1)', padding: '12px 16px', borderRadius: '10px', borderLeft: '3px solid #6366f1', fontSize: '0.88rem', color: '#c7d2fe', lineHeight: '1.5' }}>
                  <strong style={{ color: '#a5b4fc', display: 'block', marginBottom: '2px' }}>📜 Begründung nach DIN EN ISO 900x:</strong>
                  {q.isoJustification}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    );
  }

  // Active exam in progress
  if (!currentQ) return null;

  return (
    <div className="glass-panel" style={{ padding: '32px' }}>
      {/* Header bar */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', flexWrap: 'wrap', gap: '12px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
          <span className="badge badge-purple">Frage {currentIndex + 1} von {totalExamQuestions}</span>
          <span className="badge badge-amber">{currentQ.isoClause}</span>
        </div>
        
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '8px 16px', borderRadius: '10px', background: timeLeft < 300 ? 'rgba(239, 68, 68, 0.25)' : 'rgba(30, 41, 59, 0.7)', border: timeLeft < 300 ? '1px solid #ef4444' : '1px solid var(--glass-border)', color: timeLeft < 300 ? '#fca5a5' : '#ffffff', fontWeight: 700, fontSize: '1rem' }}>
          <Clock size={18} color={timeLeft < 300 ? '#ef4444' : '#a5b4fc'} /> 
          Verbleibende Zeit: {formatTime(timeLeft)}
        </div>
      </div>

      {/* Progress mini-bar */}
      <div style={{ width: '100%', height: '4px', background: 'rgba(255, 255, 255, 0.1)', borderRadius: '2px', marginBottom: '24px', overflow: 'hidden' }}>
        <div style={{ width: `${((currentIndex + 1) / totalExamQuestions) * 100}%`, height: '100%', background: 'linear-gradient(90deg, #6366f1, #a855f7)', transition: 'width 0.3s ease' }} />
      </div>

      {/* Question Text */}
      <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#ffffff', marginBottom: '24px', lineHeight: '1.5' }}>
        {currentQ.question}
      </h2>

      {/* Options List */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginBottom: '32px' }}>
        {currentQ.options.map(opt => {
          const isSel = (userAnswers[currentQ.id] || []).includes(opt.id);
          return (
            <div
              key={opt.id}
              onClick={() => handleSelectOption(opt.id)}
              style={{
                padding: '16px 20px',
                borderRadius: '12px',
                border: isSel ? '2px solid #6366f1' : '1px solid rgba(255, 255, 255, 0.1)',
                background: isSel ? 'rgba(99, 102, 241, 0.25)' : 'rgba(30, 41, 59, 0.5)',
                color: '#ffffff',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '14px',
                transition: 'all 0.2s ease',
                fontSize: '1rem'
              }}
            >
              <div style={{
                width: '24px',
                height: '24px',
                borderRadius: '6px',
                border: isSel ? '2px solid #6366f1' : '2px solid rgba(255, 255, 255, 0.3)',
                background: isSel ? '#6366f1' : 'transparent',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontWeight: 700,
                fontSize: '0.85rem',
                flexShrink: 0
              }}>
                {opt.id}
              </div>
              <span style={{ flexGrow: 1 }}>{opt.text}</span>
            </div>
          );
        })}
      </div>

      {/* Question jump matrix */}
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px', marginBottom: '28px', padding: '12px', background: 'rgba(15, 23, 42, 0.4)', borderRadius: '10px' }}>
        {activeQuestions.map((q, idx) => {
          const isAnswered = (userAnswers[q.id] || []).length > 0;
          const isCurrent = idx === currentIndex;
          return (
            <button
              key={q.id}
              onClick={() => setCurrentIndex(idx)}
              style={{
                width: '32px',
                height: '32px',
                borderRadius: '6px',
                border: isCurrent ? '2px solid #ffffff' : '1px solid var(--glass-border)',
                background: isCurrent ? '#6366f1' : isAnswered ? 'rgba(16, 185, 129, 0.3)' : 'rgba(30, 41, 59, 0.6)',
                color: isCurrent ? '#ffffff' : isAnswered ? '#6ee7b7' : 'var(--text-muted)',
                fontWeight: isCurrent ? 700 : 500,
                fontSize: '0.8rem',
                cursor: 'pointer'
              }}
            >
              {idx + 1}
            </button>
          );
        })}
      </div>

      {/* Footer Navigation */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '12px' }}>
        <button
          onClick={() => setCurrentIndex(prev => Math.max(0, prev - 1))}
          disabled={currentIndex === 0}
          className="btn-secondary"
          style={{ opacity: currentIndex === 0 ? 0.5 : 1 }}
        >
          <ArrowLeft size={16} /> Vorherige Frage
        </button>

        <div style={{ display: 'flex', gap: '12px' }}>
          <button
            onClick={handleFinish}
            className="btn-secondary"
            style={{ borderColor: 'rgba(239, 68, 68, 0.4)', color: '#fca5a5' }}
          >
            Prüfung vorzeitig abgeben
          </button>

          {currentIndex < totalExamQuestions - 1 ? (
            <button onClick={() => setCurrentIndex(prev => prev + 1)} className="btn-primary">
              Nächste Frage <ArrowRight size={16} />
            </button>
          ) : (
            <button onClick={handleFinish} className="btn-primary" style={{ background: 'linear-gradient(135deg, #10b981 0%, #059669 100%)' }}>
              Prüfung jetzt auswerten <Check size={18} />
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
