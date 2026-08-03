import React from 'react';
import { BarChart3, CheckCircle2, RefreshCw, Trophy, Flame, RotateCcw, Target, ShieldCheck } from 'lucide-react';

export default function StatsDashboard({ stats, questions, onResetStats }) {
  const { totalAnswered, correctCount, wrongCount, masteredIds, categoryStats, history } = stats;

  const accuracyRate = totalAnswered > 0 ? Math.round((correctCount / totalAnswered) * 100) : 0;
  const totalQuestions = questions.length;
  const masteredPercent = Math.round((masteredIds.length / totalQuestions) * 100) || 0;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      
      {/* Top Metric Cards */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '16px' }}>
        
        {/* Richtig Quote */}
        <div className="glass-panel" style={{ padding: '20px' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Richtig-Quote</span>
            <Target size={20} color="#10b981" />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#6ee7b7' }}>
            {accuracyRate}%
          </div>
          <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)', margin: 0 }}>
            {correctCount} richtig von {totalAnswered} Versuchen
          </p>
        </div>

        {/* Gemasterte Fragen */}
        <div className="glass-panel" style={{ padding: '20px' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Gemastert</span>
            <Trophy size={20} color="#f59e0b" />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#fcd34d' }}>
            {masteredIds.length} <span style={{ fontSize: '1rem', color: 'var(--text-muted)' }}>/ {totalQuestions}</span>
          </div>
          <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)', margin: 0 }}>
            {masteredPercent}% aller Fragen im Stapel beherrscht
          </p>
        </div>

        {/* Wiederholungen */}
        <div className="glass-panel" style={{ padding: '20px' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Fehler-Wiederholungen</span>
            <RefreshCw size={20} color="#ef4444" />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#fca5a5' }}>
            {wrongCount}
          </div>
          <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)', margin: 0 }}>
            Erfolgreich nach hinten umgemischt
          </p>
        </div>

        {/* ISO 9001 Lern-Streak */}
        <div className="glass-panel" style={{ padding: '20px' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Lern-Streak</span>
            <Flame size={20} color="#6366f1" />
          </div>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#a5b4fc' }}>
            🔥 Aktiv
          </div>
          <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)', margin: 0 }}>
            Regelmäßiges Training sichert TÜV-Erfolg
          </p>
        </div>
      </div>

      {/* Category Mastery Breakdown */}
      <div className="glass-panel" style={{ padding: '24px' }}>
        <h3 style={{ fontSize: '1.1rem', fontWeight: 700, color: '#ffffff', marginBottom: '16px', display: 'flex', alignItems: 'center', gap: '8px' }}>
          <ShieldCheck size={20} color="#6366f1" /> Leistung nach ISO 9001 Themengebieten
        </h3>
        
        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {Object.entries(categoryStats).map(([cat, data]) => {
            const catRate = data.total > 0 ? Math.round((data.correct / data.total) * 100) : 0;
            return (
              <div key={cat}>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', marginBottom: '6px' }}>
                  <span style={{ fontWeight: 600, color: '#e5e7eb' }}>{cat}</span>
                  <span style={{ color: 'var(--text-muted)' }}>{data.correct} von {data.total} richtig ({catRate}%)</span>
                </div>
                <div style={{ width: '100%', height: '8px', borderRadius: '4px', background: 'rgba(15, 23, 42, 0.6)', overflow: 'hidden' }}>
                  <div
                    style={{
                      width: `${catRate}%`,
                      height: '100%',
                      background: catRate >= 80 ? '#10b981' : catRate >= 50 ? '#f59e0b' : '#ef4444',
                      borderRadius: '4px',
                      transition: 'width 0.4s ease'
                    }}
                  />
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Recent History Table */}
      <div className="glass-panel" style={{ padding: '24px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
          <h3 style={{ fontSize: '1.1rem', fontWeight: 700, color: '#ffffff', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <BarChart3 size={20} color="#3b82f6" /> Letzte Beantwortungshistorie
          </h3>
          <button onClick={onResetStats} className="btn-secondary" style={{ fontSize: '0.8rem', padding: '6px 12px' }}>
            <RotateCcw size={14} /> Statistik zurücksetzen
          </button>
        </div>

        {history.length === 0 ? (
          <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>Noch keine Fragen beantwortet.</p>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', maxHeight: '300px', overflowY: 'auto' }}>
            {history.slice(-10).reverse().map((item, idx) => (
              <div key={idx} className="glass-card" style={{ padding: '12px 16px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', fontSize: '0.88rem' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                  {item.isCorrect ? (
                    <CheckCircle2 size={18} color="#10b981" />
                  ) : (
                    <RefreshCw size={18} color="#ef4444" />
                  )}
                  <span style={{ color: '#ffffff', fontWeight: 500 }}>{item.questionText}</span>
                </div>
                <span className="badge badge-purple">{item.isoClause}</span>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
