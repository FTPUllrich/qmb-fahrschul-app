import React from 'react';
import { Layers, Award, BookOpen, Image, BarChart3, Volume2, VolumeX, Dog, Smile } from 'lucide-react';

export default function Navbar({
  activeTab,
  setActiveTab,
  soundEnabled,
  setSoundEnabled,
  dogMode,
  setDogMode,
  humorMode,
  setHumorMode,
  masteredCount,
  totalCount
}) {
  const navItems = [
    { id: 'stack', label: 'Fahrschul-Stapel', icon: Layers },
    { id: 'exam', label: 'TÜV-Prüfung', icon: Award },
    { id: 'glossary', label: 'QM-Sachbegriffe', icon: BookOpen },
    { id: 'importer', label: 'Bild-Scanner', icon: Image },
    { id: 'stats', label: 'Statistik', icon: BarChart3 },
    { id: 'maydell', label: 'Maydells Fragen 100% legit', icon: Layers }
  ];

  return (
    <header className="glass-panel" style={{ padding: '16px 28px', marginBottom: '24px' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px' }}>
        {/* Brand */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <div style={{
            width: '42px',
            height: '42px',
            borderRadius: '12px',
            background: 'linear-gradient(135deg, #6366f1 0%, #10b981 100%)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: '1.4rem',
            boxShadow: '0 4px 12px rgba(99, 102, 241, 0.4)'
          }}>
            🚗
          </div>
          <div>
            <h1 style={{ fontSize: '1.35rem', fontWeight: 800, background: 'linear-gradient(90deg, #ffffff, #a5b4fc)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent', margin: 0 }}>
              QMB & QMF Fahrschul-Trainer
            </h1>
            <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)', margin: 0 }}>
              Qualitätsmanagement (TÜV / ISO 9001:2015) • Interaktives Stapelsystem
            </p>
          </div>
        </div>

        {/* Navigation Tabs */}
        <nav style={{ display: 'flex', alignItems: 'center', gap: '8px', background: 'rgba(15, 23, 42, 0.5)', padding: '6px', borderRadius: '14px', border: '1px solid rgba(255, 255, 255, 0.08)' }}>
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => setActiveTab(item.id)}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '8px',
                  padding: '8px 16px',
                  borderRadius: '10px',
                  border: 'none',
                  background: isActive ? 'linear-gradient(135deg, #6366f1 0%, #4f46e5 100%)' : 'transparent',
                  color: isActive ? '#ffffff' : 'var(--text-muted)',
                  fontWeight: isActive ? 600 : 500,
                  fontSize: '0.9rem',
                  cursor: 'pointer',
                  transition: 'all 0.2s ease',
                  boxShadow: isActive ? '0 4px 12px rgba(99, 102, 241, 0.35)' : 'none'
                }}
              >
                <Icon size={16} />
                <span>{item.label}</span>
              </button>
            );
          })}
        </nav>

        {/* Controls & Quick Stats */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          {/* Audio toggle */}
          <button
            onClick={() => setSoundEnabled(!soundEnabled)}
            title={soundEnabled ? 'Audio aktiviert' : 'Audio stummgeschaltet'}
            style={{
              padding: '8px 12px',
              borderRadius: '10px',
              border: '1px solid var(--glass-border)',
              background: soundEnabled ? 'rgba(16, 185, 129, 0.15)' : 'rgba(255, 255, 255, 0.05)',
              color: soundEnabled ? '#6ee7b7' : 'var(--text-muted)',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              fontSize: '0.85rem'
            }}
          >
            {soundEnabled ? <Volume2 size={16} /> : <VolumeX size={16} />}
            <span>Sound</span>
          </button>

          {/* Dog reward toggle */}
          <button
            onClick={() => setDogMode(!dogMode)}
            title={dogMode ? 'Lern-Hund Belohnungen aktiv' : 'Hunde-Modus inaktiv'}
            style={{
              padding: '8px 12px',
              borderRadius: '10px',
              border: '1px solid var(--glass-border)',
              background: dogMode ? 'rgba(99, 102, 241, 0.2)' : 'rgba(255, 255, 255, 0.05)',
              color: dogMode ? '#a5b4fc' : 'var(--text-muted)',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              fontSize: '0.85rem'
            }}
          >
            <Dog size={16} />
            <span>Hunde-Belohnung</span>
          </button>

          {/* Humor toggle */}
          <button
            onClick={() => setHumorMode(!humorMode)}
            title={humorMode ? 'Humor- & Meme-Feedback aktiv' : 'Humor-Modus inaktiv'}
            style={{
              padding: '8px 12px',
              borderRadius: '10px',
              border: '1px solid var(--glass-border)',
              background: humorMode ? 'rgba(245, 158, 11, 0.2)' : 'rgba(255, 255, 255, 0.05)',
              color: humorMode ? '#fcd34d' : 'var(--text-muted)',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              fontSize: '0.85rem'
            }}
          >
            <Smile size={16} />
            <span>Humor-Modus</span>
          </button>
        </div>
      </div>
    </header>
  );
}
