#!/usr/bin/env python3
"""
Konsolidierungsskript: Führt die analysierten MC-Fragen in die HTML-Datei ein.
Liest mc1_analyzed.json bis mc9_analyzed.json und aktualisiert die HTML.
"""

import json
import re
import os

BASE_PATH = '/home/ole/Projects/qmb-fahrschul-app/src/data'
HTML_PATH = '/home/ole/Projects/qmb-fahrschul-app/index.html'
BACKUP_PATH = '/home/ole/Projects/qmb-fahrschul-app/index_backup_pre_consolidation.html'

def load_all_analyzed():
    """Lädt alle analysierten MC-Fragen aus den JSON-Dateien."""
    all_analyzed = []
    for i in range(1, 10):
        path = os.path.join(BASE_PATH, f'mc{i}_analyzed.json')
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                all_analyzed.extend(data)
                print(f"✅ mc{i}_analyzed.json: {len(data)} Fragen geladen")
        else:
            print(f"⚠️  mc{i}_analyzed.json: NICHT GEFUNDEN")
    return all_analyzed

def load_current_questions():
    """Lädt alle aktuellen Fragen aus der HTML-Datei."""
    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start = content.find('const allQuestionsData = [')
    end = content.find('];', start) + 2
    json_str = content[start+len('const allQuestionsData = '):end-1]
    questions = json.loads(json_str)
    return questions, content, start, end

def match_questions(analyzed, current):
    """Matched analysierte Fragen mit aktuellen Fragen nach Fragetext."""
    matches = []
    unmatched_analyzed = []
    
    # Erstelle Lookup aus aktuellen Fragen
    current_lookup = {}
    for q in current:
        # Normalisierung des Fragetexts für Matching
        key = q['question'].strip().lower()[:80]
        current_lookup[key] = q
    
    for a in analyzed:
        if a.get('isBroken', False):
            unmatched_analyzed.append(('BROKEN', a))
            continue
        
        key = a['question'].strip().lower()[:80]
        if key in current_lookup:
            matches.append((current_lookup[key], a))
        else:
            # Versuch mit kürzerem Key
            short_key = a['question'].strip().lower()[:50]
            found = None
            for ck, cq in current_lookup.items():
                if ck[:50] == short_key:
                    found = cq
                    break
            if found:
                matches.append((found, a))
            else:
                unmatched_analyzed.append(('UNMATCHED', a))
    
    return matches, unmatched_analyzed

def update_question(current_q, analyzed_q):
    """Aktualisiert eine Frage mit den analysierten Antworten."""
    updated = current_q.copy()
    
    # Aktualisiere Antworten
    if len(analyzed_q['options']) == len(current_q['options']):
        # Prüfe ob die Texte übereinstimmen
        text_match = all(
            a['text'].strip()[:40].lower() == c['text'].strip()[:40].lower()
            for a, c in zip(analyzed_q['options'], current_q['options'])
        )
        
        if text_match:
            # Aktualisiere nur isCorrect
            old_correct = [o['id'] for o in current_q['options'] if o['isCorrect']]
            new_correct = [o['id'] for o in analyzed_q['options'] if o['isCorrect']]
            
            updated['options'] = [
                {**o, 'isCorrect': analyzed_q['options'][i]['isCorrect']}
                for i, o in enumerate(current_q['options'])
            ]
            
            if old_correct != new_correct:
                updated['hasDeviation'] = True
                updated['isoConclusion'] = f"KORREKTUR: Antworten geändert von {old_correct} zu {new_correct}. {analyzed_q.get('isoJustification', '')}"
                print(f"  🔧 {current_q['id']}: {old_correct} → {new_correct}")
            
        else:
            print(f"  ⚠️  Texte stimmen nicht überein für {current_q['id']}")
    
    # Aktualisiere ISO-Felder wenn vorhanden
    if analyzed_q.get('isoClause') and analyzed_q['isoClause'] != 'DIN EN ISO 9001:2015':
        updated['isoClause'] = analyzed_q['isoClause']
    
    if analyzed_q.get('isoJustification'):
        updated['isoJustification'] = analyzed_q['isoJustification']
    
    if analyzed_q.get('infobox'):
        updated['infobox'] = analyzed_q['infobox']
    
    if analyzed_q.get('multipleChoice') is not None:
        updated['multipleChoice'] = analyzed_q['multipleChoice']
    
    return updated

def main():
    print("=== QMB Konsolidierung ===\n")
    
    # Backup
    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        html_content = f.read()
    with open(BACKUP_PATH, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"✅ Backup erstellt: {BACKUP_PATH}\n")
    
    # Lade Daten
    analyzed = load_all_analyzed()
    current_questions, content, q_start, q_end = load_current_questions()
    
    print(f"\n📊 Analysierte Fragen: {len(analyzed)}")
    print(f"📊 Aktuelle Fragen: {len(current_questions)}\n")
    
    # Matching
    matches, unmatched = match_questions(analyzed, current_questions)
    print(f"✅ Gematchte Fragen: {len(matches)}")
    print(f"⚠️  Ungematchte/Broken: {len(unmatched)}\n")
    
    # Erstelle aktualisiertes Fragen-Dictionary
    updated_map = {q['id']: q for q in current_questions}
    
    print("=== Aktualisierungen ===")
    for curr_q, anal_q in matches:
        updated = update_question(curr_q, anal_q)
        updated_map[curr_q['id']] = updated
    
    # Behalte Reihenfolge
    updated_questions = [updated_map[q['id']] for q in current_questions]
    
    # Erstelle neuen JSON-String
    new_json = json.dumps(updated_questions, ensure_ascii=False, indent=2)
    
    # Ersetze in HTML
    old_section = content[q_start:q_end]
    new_section = 'const allQuestionsData = ' + new_json + ';'
    new_content = content[:q_start] + new_section + content[q_end:]
    
    # Schreibe HTML
    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\n✅ HTML aktualisiert: {HTML_PATH}")
    
    # Statistiken
    corrections = sum(1 for q in updated_questions if q.get('hasDeviation'))
    print(f"🔧 Korrekturen gesamt: {corrections}")
    
    # Ungematchte ausgeben
    if unmatched:
        print(f"\n⚠️  Ungematchte Fragen ({len(unmatched)}):")
        for typ, q in unmatched[:10]:
            print(f"  [{typ}] {q['question'][:60]}")

if __name__ == '__main__':
    main()
