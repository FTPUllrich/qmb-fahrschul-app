import React from 'react';
import { Layers, RefreshCw, CheckCircle2, Target, ArrowDownCircle } from 'lucide-react';

export default function StackProgress({ activeCount, retryCount, masteredCount, totalCount, accuracyRate, categoryFilter, setCategoryFilter, categories }) {
  return (
    <div className="glass-panel" style={{ padding: '20px 24px', marginBottom: '24px' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px', marginBottom: '16px' }}>
        
        {/* Driving school stack metrics */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '20px', flexWrap: 'wrap' }}>
          
          {/* Active Stack */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <div style={{ padding: '8px', borderRadius: '10px', background: 'rgba(99, 102, 241, 0.2)', color: '#a5b4fc' }}>
              <Layers size={20} />
            </div>
            <div>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                Aktueller Stapel
              </div>
              <div style={{ fontSize: '1.25rem', fontWeight: 700, color: '#ffffff' }}>
                {activeCount} <span style={{ fontSize: '0.85rem', fontWeight: 400, color: 'var(--text-muted)' }}>Fragen verbleibend</span>
              </div>
            </div>
          </div>

          <div style={{ height: '32px', width: '1px', background: 'rgba(255, 255, 255, 0.1)' }} />

          {/* Retry / Mixed back */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <div style={{ padding: '8px', borderRadius: '10px', background: 'rgba(245, 158, 11, 0.2)', color: '#fcd34d' }}>
              <RefreshCw size={20} />
            </div>
            <div>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                Wiederholungen (Gemischt)
              </div>
              <div style={{ fontSize: '1.25rem', fontWeight: 700, color: '#fcd34d' }}>
                {retryCount} <span style={{ fontSize: '0.85rem', fontWeight: 400, color: 'var(--text-muted)' }}>neu einsortiert</span>
              </div>
            </div>
          </div>

          <div style={{ height: '32px', width: '1px', background: 'rgba(255, 255, 255, 0.1)' }} />

          {/* Mastered / Below */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <div style={{ padding: '8px', borderRadius: '10px', background: 'rgba(16, 185, 129, 0.2)', color: '#6ee7b7' }}>
              <CheckCircle2 size={20} />
            </div>
            <div>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                Gemastert (Unten einsortiert)
              </div>
              <div style={{ fontSize: '1.25rem', fontWeight: 700, color: '#6ee7b7' }}>
                {masteredCount} / {totalCount}
              </div>
            </div>
          </div>
        </div>

        {/* Category filter dropdown */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Thema:</span>
          <select
            value={categoryFilter}
            onChange={(e) => setCategoryFilter(e.target.value)}
            style={{
              padding: '8px 14px',
              borderRadius: '10px',
              border: '1px solid var(--glass-border)',
              background: 'rgba(30, 41, 59, 0.8)',
              color: '#ffffff',
              fontSize: '0.85rem',
              outline: 'none',
              cursor: 'pointer'
            }}
          >
            <option value="ALL">Alle QM-Themen</option>
            {categories.map((cat) => (
              <option key={cat} value={cat}>{cat}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Fahrschulapp Progress Bar */}
      <div>
        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem', color: 'var(--text-muted)', marginBottom: '6px' }}>
          <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
            <ArrowDownCircle size={14} color="#6ee7b7" /> Fahrschulapp-Prinzip: Richtig = Nach unten | Falsch = Direkt neu untergemischt
          </span>
          <span style={{ fontWeight: 600, color: '#ffffff' }}>Richtig-Quote: {accuracyRate}%</span>
        </div>
        <div style={{ width: '100%', height: '10px', borderRadius: '5px', background: 'rgba(15, 23, 42, 0.6)', overflow: 'hidden', display: 'flex' }}>
          <div style={{ width: `${(masteredCount / totalCount) * 100}%`, background: 'linear-gradient(90deg, #10b981, #34d399)', transition: 'width 0.4s ease' }} title="Gemastert" />
          <div style={{ width: `${(retryCount / totalCount) * 100}%`, background: 'linear-gradient(90deg, #f59e0b, #fbbf24)', transition: 'width 0.4s ease' }} title="In Wiederholung" />
        </div>
      </div>
    </div>
  );
}
