import React, { useState, useEffect } from 'react';
import { initialQuestions } from './data/questionsData';
import Navbar from './components/Navbar';
import StackProgress from './components/StackProgress';
import QuestionCard from './components/QuestionCard';
import StatsDashboard from './components/StatsDashboard';
import GlossaryView from './components/GlossaryView';
import ImageImporterView from './components/ImageImporterView';
import ExamModeView from './components/ExamModeView';

export default function App() {
  const [activeTab, setActiveTab] = useState('stack');

  // Settings state
  const [soundEnabled, setSoundEnabled] = useState(() => {
    return localStorage.getItem('qmb_sound') !== 'false';
  });
  const [dogMode, setDogMode] = useState(() => {
    return localStorage.getItem('qmb_dog') !== 'false';
  });
  const [humorMode, setHumorMode] = useState(() => {
    return localStorage.getItem('qmb_humor') !== 'false';
  });

  // Question database & stack state
  const [allQuestions, setAllQuestions] = useState(() => {
    const saved = localStorage.getItem('qmb_custom_questions');
    if (saved) {
      try {
        const parsed = JSON.parse(saved);
        return [...initialQuestions, ...parsed];
      } catch (e) {
        return initialQuestions;
      }
    }
    return initialQuestions;
  });

  const [categoryFilter, setCategoryFilter] = useState('ALL');

  // Active stack representation (Driving school pile)
  const [questionsStack, setQuestionsStack] = useState(() => {
    return [...allQuestions];
  });

  const [masteredIds, setMasteredIds] = useState(() => {
    const saved = localStorage.getItem('qmb_mastered');
    return saved ? JSON.parse(saved) : [];
  });

  const [retryCount, setRetryCount] = useState(0);

  // Analytics & Stats
  const [stats, setStats] = useState(() => {
    const saved = localStorage.getItem('qmb_stats');
    if (saved) {
      try {
        return JSON.parse(saved);
      } catch (e) {}
    }
    return {
      totalAnswered: 0,
      correctCount: 0,
      wrongCount: 0,
      masteredIds: [],
      categoryStats: {},
      history: []
    };
  });

  // Save state updates
  useEffect(() => {
    localStorage.setItem('qmb_sound', soundEnabled);
  }, [soundEnabled]);

  useEffect(() => {
    localStorage.setItem('qmb_dog', dogMode);
  }, [dogMode]);

  useEffect(() => {
    localStorage.setItem('qmb_humor', humorMode);
  }, [humorMode]);

  useEffect(() => {
    localStorage.setItem('qmb_stats', JSON.stringify(stats));
  }, [stats]);

  useEffect(() => {
    localStorage.setItem('qmb_mastered', JSON.stringify(masteredIds));
  }, [masteredIds]);

  // Categories list
  const categories = [...new Set(allQuestions.map(q => q.category))];

  // Filtered active stack based on category selection
  const activeDeck = questionsStack.filter(q => {
    if (categoryFilter === 'ALL') return true;
    return q.category === categoryFilter;
  });

  // Driving school stack algorithm handler
  const handleAnswer = (questionId, isCorrect) => {
    const currentQ = allQuestions.find(q => q.id === questionId);
    if (!currentQ) return;

    // Update statistics
    setStats(prev => {
      const cat = currentQ.category || 'Allgemein';
      const catPrev = prev.categoryStats[cat] || { total: 0, correct: 0 };
      const newCat = {
        total: catPrev.total + 1,
        correct: catPrev.correct + (isCorrect ? 1 : 0)
      };

      const newMastered = isCorrect && !prev.masteredIds.includes(questionId)
        ? [...prev.masteredIds, questionId]
        : prev.masteredIds;

      return {
        totalAnswered: prev.totalAnswered + 1,
        correctCount: prev.correctCount + (isCorrect ? 1 : 0),
        wrongCount: prev.wrongCount + (isCorrect ? 0 : 1),
        masteredIds: newMastered,
        categoryStats: { ...prev.categoryStats, [cat]: newCat },
        history: [
          ...prev.history,
          {
            questionId,
            questionText: currentQ.question.substring(0, 60) + '...',
            isoClause: currentQ.isoClause,
            isCorrect,
            timestamp: new Date().toISOString()
          }
        ]
      };
    });

    if (isCorrect) {
      // Correct answer: Remove from current top, move to bottom / mastered pool
      setQuestionsStack(prev => {
        const remaining = prev.filter(q => q.id !== questionId);
        return remaining; // Moved down to mastered list!
      });
      if (!masteredIds.includes(questionId)) {
        setMasteredIds([...masteredIds, questionId]);
      }
    } else {
      // Incorrect answer (Fahrschulapp-Prinzip): Re-insert question 2-3 positions down in upcoming deck!
      setRetryCount(prev => prev + 1);
      setQuestionsStack(prev => {
        const remaining = prev.filter(q => q.id !== questionId);
        // Insert 2 slots after current position so it reappears quickly
        const insertIndex = Math.min(2, remaining.length);
        const newStack = [...remaining];
        newStack.splice(insertIndex, 0, currentQ);
        return newStack;
      });
    }
  };

  // Import custom questions extracted from images
  const handleImportQuestions = (importedList) => {
    setAllQuestions(prev => [...prev, ...importedList]);
    setQuestionsStack(prev => [...prev, ...importedList]);

    const existingCustom = JSON.parse(localStorage.getItem('qmb_custom_questions') || '[]');
    localStorage.setItem('qmb_custom_questions', JSON.stringify([...existingCustom, ...importedList]));
  };

  const handleResetStats = () => {
    if (window.confirm('Möchtest du alle Lernstatistiken zurücksetzen?')) {
      setStats({
        totalAnswered: 0,
        correctCount: 0,
        wrongCount: 0,
        masteredIds: [],
        categoryStats: {},
        history: []
      });
      setMasteredIds([]);
      setQuestionsStack([...allQuestions]);
      setRetryCount(0);
      localStorage.removeItem('qmb_stats');
      localStorage.removeItem('qmb_mastered');
    }
  };

  const currentQuestion = activeDeck[0];
  const accuracyRate = stats.totalAnswered > 0 ? Math.round((stats.correctCount / stats.totalAnswered) * 100) : 100;

  return (
    <div style={{ minHeight: '100vh', padding: '24px 16px', maxWidth: '1200px', margin: '0 auto' }}>
      
      {/* Top Navbar */}
      <Navbar
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        soundEnabled={soundEnabled}
        setSoundEnabled={setSoundEnabled}
        dogMode={dogMode}
        setDogMode={setDogMode}
        humorMode={humorMode}
        setHumorMode={setHumorMode}
        masteredCount={masteredIds.length}
        totalCount={allQuestions.length}
      />

      {/* Main Tab Views */}
      {activeTab === 'stack' && (
        <>
          <StackProgress
            activeCount={activeDeck.length}
            retryCount={retryCount}
            masteredCount={masteredIds.length}
            totalCount={allQuestions.length}
            accuracyRate={accuracyRate}
            categoryFilter={categoryFilter}
            setCategoryFilter={setCategoryFilter}
            categories={categories}
          />
          <QuestionCard
            question={currentQuestion}
            onAnswer={handleAnswer}
            dogMode={dogMode}
            humorMode={humorMode}
            activeStackIndex={0}
            totalStackSize={activeDeck.length}
          />
        </>
      )}

      {activeTab === 'exam' && (
        <ExamModeView questions={allQuestions} />
      )}

      {activeTab === 'glossary' && (
        <GlossaryView />
      )}

      {activeTab === 'importer' && (
        <ImageImporterView onImportQuestions={handleImportQuestions} />
      )}

      {activeTab === 'stats' && (
        <StatsDashboard
          stats={stats}
          questions={allQuestions}
          onResetStats={handleResetStats}
        />
      )}
    </div>
  );
}
