import React, { useState } from 'react';
import { initialGlossary } from '../data/glossaryData';
import { Search, BookOpen, Tag, Bookmark } from 'lucide-react';

export default function GlossaryView() {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('ALL');

  const categories = ['ALL', ...new Set(initialGlossary.map(item => item.category))];

  const filteredGlossary = initialGlossary.filter(item => {
    const matchesCategory = selectedCategory === 'ALL' || item.category === selectedCategory;
    const matchesSearch = 
      item.term.toLowerCase().includes(searchQuery.toLowerCase()) ||
      item.definition.toLowerCase().includes(searchQuery.toLowerCase()) ||
      item.keywords.some(k => k.toLowerCase().includes(searchQuery.toLowerCase()));
    return matchesCategory && matchesSearch;
  });

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      
      {/* Header & Search */}
      <div className="glass-panel" style={{ padding: '24px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '16px' }}>
          <BookOpen size={24} color="#6366f1" />
          <div>
            <h2 style={{ fontSize: '1.3rem', fontWeight: 800, color: '#ffffff', margin: 0 }}>
              Sammlung von QM-Sachbegriffen (QMF & QMB)
            </h2>
            <p style={{ fontSize: '0.85rem', color: 'var(--text-muted)', margin: 0 }}>
              Definitionen, Normverweise und Schlüsselkonzepte nach DIN EN ISO 9000:2015 & ISO 9001:2015
            </p>
          </div>
        </div>

        {/* Search input */}
        <div style={{ position: 'relative', marginBottom: '16px' }}>
          <Search size={18} color="var(--text-muted)" style={{ position: 'absolute', left: '16px', top: '50%', transform: 'translateY(-50%)' }} />
          <input
            type="text"
            placeholder="Sachbegriff suchen (z.B. Audit, HLS, PDCA, Ishikawa, Stakeholder...)..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{
              width: '100%',
              padding: '14px 16px 14px 48px',
              borderRadius: '12px',
              border: '1px solid var(--glass-border)',
              background: 'rgba(15, 23, 42, 0.6)',
              color: '#ffffff',
              fontSize: '0.95rem',
              outline: 'none'
            }}
          />
        </div>

        {/* Category filter chips */}
        <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
          {categories.map((cat) => (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              style={{
                padding: '6px 14px',
                borderRadius: '20px',
                border: '1px solid var(--glass-border)',
                background: selectedCategory === cat ? 'linear-gradient(135deg, #6366f1 0%, #4f46e5 100%)' : 'rgba(30, 41, 59, 0.5)',
                color: selectedCategory === cat ? '#ffffff' : 'var(--text-muted)',
                fontSize: '0.82rem',
                fontWeight: selectedCategory === cat ? 600 : 400,
                cursor: 'pointer',
                transition: 'all 0.2s ease'
              }}
            >
              {cat === 'ALL' ? 'Alle Begriffskategorien' : cat}
            </button>
          ))}
        </div>
      </div>

      {/* Terms Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: '20px' }}>
        {filteredGlossary.map((item) => (
          <div key={item.id} className="glass-card" style={{ padding: '20px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '10px', marginBottom: '10px' }}>
                <h3 style={{ fontSize: '1.15rem', fontWeight: 700, color: '#ffffff', margin: 0 }}>
                  {item.term}
                </h3>
                <span className="badge badge-purple" style={{ fontSize: '0.72rem' }}>
                  {item.category}
                </span>
              </div>

              <p style={{ fontSize: '0.9rem', color: '#d1d5db', lineHeight: '1.6', marginBottom: '16px' }}>
                {item.definition}
              </p>
            </div>

            <div>
              <div style={{ background: 'rgba(99, 102, 241, 0.1)', padding: '8px 12px', borderRadius: '8px', marginBottom: '12px', display: 'flex', alignItems: 'center', gap: '6px' }}>
                <Bookmark size={14} color="#a5b4fc" />
                <span style={{ fontSize: '0.8rem', color: '#a5b4fc', fontWeight: 500 }}>
                  Normbezug: {item.isoRef}
                </span>
              </div>

              <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
                {item.keywords.map((kw, idx) => (
                  <span key={idx} style={{ fontSize: '0.72rem', background: 'rgba(255, 255, 255, 0.05)', color: 'var(--text-muted)', padding: '2px 8px', borderRadius: '4px' }}>
                    #{kw}
                  </span>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
