#!/usr/bin/env python3
"""Anwendung der Subagenten-Korrekturdaten R4 und R5"""
import json, sys, os

# Import from subagent files
sys.path.insert(0, '/home/ole/Projects/qmb-fahrschul-app/scripts')

# Load R4 data
exec(open('/home/ole/Projects/qmb-fahrschul-app/scripts/corrections_r4_data.py').read())
# Now CORRECTIONS_R4 is defined

# Load R5 data  
exec(open('/home/ole/Projects/qmb-fahrschul-app/scripts/corrections_r5_data.py').read())
# Now CORRECTIONS_R5 is defined

HTML_PATH = '/home/ole/Projects/qmb-fahrschul-app/index.html'

def apply_corrections(questions, corrections):
    count = 0
    broken_count = 0
    for q in questions:
        qid = q['id']
        if qid not in corrections:
            continue
        corr = corrections[qid]
        
        # Handle broken questions
        if corr.get('isBroken', False):
            q['isBroken'] = True
            broken_count += 1
            continue
            
        if 'options_correct' in corr and corr['options_correct']:
            old = [o['id'] for o in q['options'] if o['isCorrect']]
            for o in q['options']:
                if o['id'] in corr['options_correct']:
                    o['isCorrect'] = corr['options_correct'][o['id']]
            new = [o['id'] for o in q['options'] if o['isCorrect']]
            if old != new:
                q['hasDeviation'] = True
                count += 1
                print(f"  {qid}: {old} -> {new}")
        if 'multipleChoice' in corr:
            q['multipleChoice'] = corr['multipleChoice']
        if 'isoClause' in corr and corr['isoClause']:
            q['isoClause'] = corr['isoClause']
        if 'isoJustification' in corr and corr['isoJustification']:
            q['isoJustification'] = corr['isoJustification']
        if 'infobox' in corr and corr['infobox']:
            q['infobox'] = corr['infobox']
    return questions, count, broken_count

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()
start_idx = content.find('const allQuestionsData = [')
end_idx = content.find('];', start_idx) + 2
json_str = content[start_idx+len('const allQuestionsData = '):end_idx-1]
questions = json.loads(json_str)

# Merge both correction dicts
all_corrections = {}
all_corrections.update(CORRECTIONS_R4)
all_corrections.update(CORRECTIONS_R5)

print(f"Gesamtkorrekturen in Dict: {len(all_corrections)}")
print("=== Korrekturen R4+R5 ===")
questions, n, b = apply_corrections(questions, all_corrections)
print(f"\nAntwort-Korrekturen: {n}")
print(f"Broken markiert: {b}")

# Statistics
broken = [q for q in questions if q.get('isBroken', False)]
has_deviation = [q for q in questions if q.get('hasDeviation', False)]
print(f"\n=== Gesamtstatistik ===")
print(f"Total Fragen: {len(questions)}")
print(f"Broken: {len(broken)}")
print(f"Mit Korrekturen (hasDeviation): {len(has_deviation)}")
print(f"Gültige Fragen (nicht broken): {len(questions) - len(broken)}")

new_json = json.dumps(questions, ensure_ascii=False, indent=2)
new_content = content[:start_idx] + 'const allQuestionsData = ' + new_json + ';' + content[end_idx:]
with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("\nGespeichert.")
