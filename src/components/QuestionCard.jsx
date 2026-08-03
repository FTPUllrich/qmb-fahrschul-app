import React, { useState, useEffect } from 'react';
import confetti from 'canvas-confetti';
import { soundFx } from '../services/soundEffects';
import { dogRewards } from '../data/dogData';
import { humorReactions } from '../data/humorData';
import { CheckCircle2, XCircle, Info, ShieldCheck, Sparkles, Dog, HelpCircle, ArrowRight, RotateCcw } from 'lucide-react';

export default function QuestionCard({
  question,
  onAnswer,
  dogMode,
  humorMode,
  activeStackIndex,
  totalStackSize
}) {
  const [selectedOptions, setSelectedOptions] = useState([]);
  const [submitted, setSubmitted] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);
  const [showInfobox, setShowInfobox] = useState(false);
  const [currentDog, setCurrentDog] = useState(null);
  const [currentHumor, setCurrentHumor] = useState(null);

  // Reset state when question changes
  useEffect(() => {
    setSelectedOptions([]);
    setSubmitted(false);
    setIsCorrect(false);
    setShowInfobox(false);
    
    // Pick random dog & humor reward
    const randomDog = dogRewards[Math.floor(Math.random() * dogRewards.length)];
    const randomHumor = humorReactions[Math.floor(Math.random() * humorReactions.length)];
    setCurrentDog(randomDog);
    setCurrentHumor(randomHumor);
  }, [question?.id]);

  if (!question) {
    return (
      <div className="glass-panel" style={{ padding: '48px', textAlign: 'center' }}>
        <div style={{ fontSize: '3rem', marginBottom: '16px' }}>🎉</div>
        <h2 style={{ fontSize: '1.5rem', fontWeight: 700, color: '#6ee7b7', marginBottom: '8px' }}>
          Herzlichen Glückwunsch! Stapel komplett gemastert!
        </h2>
        <p style={{ color: 'var(--text-muted)', marginBottom: '24px' }}>
          Du hast alle Fragen des ausgewählten ISO 9001 Themas erfolgreich nach unten einsortiert.
        </p>
        <button onClick={() => window.location.reload()} className="btn-primary">
          <RotateCcw size={18} /> Stapel zurücksetzen & erneut lernen
        </button>
      </div>
    );
  }

  const handleOptionToggle = (optionId) => {
    if (submitted) return;
    if (question.multipleChoice) {
      if (selectedOptions.includes(optionId)) {
        setSelectedOptions(selectedOptions.filter(id => id !== optionId));
      } else {
        setSelectedOptions([...selectedOptions, optionId]);
      }
    } else {
      setSelectedOptions([optionId]);
    }
  };

  const handleSubmit = () => {
    if (selectedOptions.length === 0 || submitted) return;

    // Check correctness
    const correctOptionIds = question.options.filter(o => o.isCorrect).map(o => o.id);
    const optionsMatch = 
      selectedOptions.length === correctOptionIds.length &&
      selectedOptions.every(id => correctOptionIds.includes(id));

    setSubmitted(true);
    setIsCorrect(optionsMatch);
    setShowInfobox(true); // Automatically expand infobox with ISO justification

    if (optionsMatch) {
      soundFx.playCorrectSound();
      confetti({
        particleCount: 70,
        spread: 60,
        origin: { y: 0.7 }
      });
    } else {
      soundFx.playWrongSound();
    }
  };

  const handleNext = () => {
    onAnswer(question.id, isCorrect);
  };

  return (
    <div
      className={`glass-panel ${submitted ? (isCorrect ? 'animate-success-pulse' : 'animate-error-pulse') : ''}`}
      style={{
        padding: '32px',
        position: 'relative',
        borderColor: submitted ? (isCorrect ? 'rgba(16, 185, 129, 0.6)' : 'rgba(239, 68, 68, 0.6)') : 'var(--glass-border)',
        transition: 'all 0.3s ease'
      }}
    >
      {/* Category & Badge header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '12px', marginBottom: '20px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span className="badge badge-purple">{question.category}</span>
          <span className="badge badge-amber">{question.isoClause}</span>
          {question.multipleChoice ? (
            <span className="badge" style={{ background: 'rgba(59, 130, 246, 0.2)', color: '#93c5fd', border: '1px solid rgba(59, 130, 246, 0.4)' }}>
              Mehrfachauswahl (Multiple Choice)
            </span>
          ) : (
            <span className="badge" style={{ background: 'rgba(168, 85, 247, 0.2)', color: '#d8b4fe', border: '1px solid rgba(168, 85, 247, 0.4)' }}>
              Einzelauswahl (Single Choice)
            </span>
          )}
        </div>
        <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>
          Stapel-Pos: <strong style={{ color: '#ffffff' }}>#{activeStackIndex + 1}</strong> von {totalStackSize}
        </div>
      </div>

      {/* Question Text */}
      <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#ffffff', marginBottom: '24px', lineHeight: '1.5' }}>
        {question.question}
      </h2>

      {/* Options List */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginBottom: '28px' }}>
        {question.options.map((option) => {
          const isSelected = selectedOptions.includes(option.id);
          let optionStyle = {
            padding: '16px 20px',
            borderRadius: '12px',
            border: '1px solid rgba(255, 255, 255, 0.1)',
            background: 'rgba(30, 41, 59, 0.5)',
            color: 'var(--text-main)',
            cursor: submitted ? 'default' : 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '14px',
            transition: 'all 0.2s ease',
            fontSize: '1rem'
          };

          if (!submitted && isSelected) {
            optionStyle.background = 'rgba(99, 102, 241, 0.25)';
            optionStyle.borderColor = '#6366f1';
          } else if (submitted) {
            if (option.isCorrect) {
              optionStyle.background = 'rgba(16, 185, 129, 0.25)';
              optionStyle.borderColor = '#10b981';
              optionStyle.color = '#a7f3d0';
            } else if (isSelected && !option.isCorrect) {
              optionStyle.background = 'rgba(239, 68, 68, 0.25)';
              optionStyle.borderColor = '#ef4444';
              optionStyle.color = '#fca5a5';
            }
          }

          return (
            <div
              key={option.id}
              onClick={() => handleOptionToggle(option.id)}
              style={optionStyle}
            >
              {/* Custom selection box */}
              <div style={{
                width: '24px',
                height: '24px',
                borderRadius: question.multipleChoice ? '6px' : '50%',
                border: isSelected ? '2px solid #6366f1' : '2px solid rgba(255, 255, 255, 0.3)',
                background: isSelected ? '#6366f1' : 'transparent',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontWeight: 700,
                fontSize: '0.85rem',
                color: '#ffffff',
                flexShrink: 0
              }}>
                {option.id}
              </div>
              <span style={{ flexGrow: 1 }}>{option.text}</span>
              {submitted && option.isCorrect && (
                <CheckCircle2 size={20} color="#10b981" />
              )}
              {submitted && isSelected && !option.isCorrect && (
                <XCircle size={20} color="#ef4444" />
              )}
            </div>
          );
        })}
      </div>

      {/* Action Buttons */}
      {!submitted ? (
        <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
          <button
            onClick={handleSubmit}
            disabled={selectedOptions.length === 0}
            className="btn-primary"
            style={{
              opacity: selectedOptions.length === 0 ? 0.5 : 1,
              cursor: selectedOptions.length === 0 ? 'not-allowed' : 'pointer'
            }}
          >
            <ShieldCheck size={18} /> Antwort überprüfen
          </button>
        </div>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          
          {/* Subconscious Dog Reward Stimulus (On Correct Answer) */}
          {isCorrect && dogMode && currentDog && (
            <div className="glass-card" style={{ padding: '20px', background: 'rgba(16, 185, 129, 0.12)', border: '1px solid rgba(16, 185, 129, 0.3)', display: 'flex', alignItems: 'center', gap: '20px', flexWrap: 'wrap' }}>
              <img
                src={currentDog.imageUrl}
                alt={currentDog.name}
                style={{ width: '80px', height: '80px', borderRadius: '50%', objectFit: 'cover', border: '3px solid #10b981', boxShadow: '0 4px 12px rgba(16, 185, 129, 0.3)' }}
              />
              <div style={{ flex: 1 }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '4px' }}>
                  <span style={{ fontWeight: 700, color: '#6ee7b7', fontSize: '1.05rem' }}>{currentDog.name}</span>
                  <span className="badge badge-green">{currentDog.badge}</span>
                </div>
                <p style={{ fontSize: '0.95rem', color: '#ecfdf5', italic: 'true', margin: 0 }}>
                  "{currentDog.quote}"
                </p>
              </div>
            </div>
          )}

          {/* Humorous Auditor Reaction (On Incorrect Answer) */}
          {!isCorrect && humorMode && currentHumor && (
            <div className="glass-card" style={{ padding: '20px', background: 'rgba(245, 158, 11, 0.12)', border: '1px solid rgba(245, 158, 11, 0.3)', display: 'flex', alignItems: 'center', gap: '20px', flexWrap: 'wrap' }}>
              <img
                src={currentHumor.imageUrl}
                alt="Auditor"
                style={{ width: '80px', height: '80px', borderRadius: '50%', objectFit: 'cover', border: '3px solid #f59e0b', boxShadow: '0 4px 12px rgba(245, 158, 11, 0.3)' }}
              />
              <div style={{ flex: 1 }}>
                <div style={{ fontWeight: 700, color: '#fcd34d', fontSize: '1.05rem', marginBottom: '4px' }}>
                  {currentHumor.title}
                </div>
                <p style={{ fontSize: '0.9rem', color: '#fef3c7', marginBottom: '6px' }}>
                  "{currentHumor.quote}"
                </p>
                <div style={{ fontSize: '0.8rem', color: '#fde68a', fontWeight: 600 }}>
                  💡 {currentHumor.humorTip}
                </div>
              </div>
            </div>
          )}

          {/* Infobox & ISO 900x Justification Accordion */}
          <div className="glass-card" style={{ padding: '20px', background: 'rgba(30, 41, 59, 0.7)' }}>
            <div
              onClick={() => setShowInfobox(!showInfobox)}
              style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', cursor: 'pointer', userSelect: 'none' }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <Info size={20} color="#6366f1" />
                <span style={{ fontWeight: 700, color: '#ffffff', fontSize: '1rem' }}>
                  Fachliche Infobox & ISO 900x Normbegründung
                </span>
              </div>
              <span style={{ fontSize: '0.85rem', color: '#a5b4fc', textDecoration: 'underline' }}>
                {showInfobox ? 'Einklappen' : 'Ausklappen'}
              </span>
            </div>

            {showInfobox && (
              <div style={{ marginTop: '16px', paddingTop: '16px', borderTop: '1px solid rgba(255, 255, 255, 0.1)' }}>
                <div style={{ marginBottom: '14px' }}>
                  <strong style={{ color: '#a5b4fc', fontSize: '0.9rem', display: 'block', marginBottom: '4px' }}>
                    📖 Sachverhalt & Erklärung:
                  </strong>
                  <p style={{ fontSize: '0.92rem', color: '#e5e7eb', lineHeight: '1.6' }}>
                    {question.infobox}
                  </p>
                </div>

                <div style={{ background: 'rgba(99, 102, 241, 0.1)', padding: '12px 16px', borderRadius: '10px', borderLeft: '4px solid #6366f1' }}>
                  <strong style={{ color: '#6366f1', fontSize: '0.85rem', display: 'block', marginBottom: '2px' }}>
                    📜 Begründung nach DIN EN ISO 900x:
                  </strong>
                  <span style={{ fontSize: '0.88rem', color: '#c7d2fe' }}>
                    {question.isoJustification}
                  </span>
                </div>
              </div>
            )}
          </div>

          {/* Continue button */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>
              {isCorrect ? '✅ Frage wandert nach unten in den gemasterten Stapel.' : '🔄 Frage wird 2-3 Plätze weiter untergemischt.'}
            </span>
            <button onClick={handleNext} className="btn-primary">
              Nächste Frage im Stapel <ArrowRight size={18} />
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
