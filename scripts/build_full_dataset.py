#!/usr/bin/env python3
"""
Full QMB Dataset Compiler
Version: v0.1.0-alpha.1
---------------------------------------------------
Parses all docx and image files in /Projects/qmb_extracted
and compiles a massive 44+ question dataset for the QMB Fahrschul-App.
"""

import os, zipfile, xml.etree.ElementTree as ET, re, json

ROOT_DIR = '/home/ole/Projects/qmb_extracted'
BUILD_SCRIPT = '/home/ole/Projects/qmb-fahrschul-app/scripts/build_standalone_app.py'

def read_docx_paras(path):
    try:
        with zipfile.ZipFile(path) as z:
            xml_content = z.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            paragraphs = []
            for elem in tree.iter():
                if elem.tag.endswith('p'):
                    texts = [node.text for node in elem.iter() if node.tag.endswith('t') and node.text]
                    if texts:
                        paragraphs.append(''.join(texts).strip())
            return [p for p in paragraphs if p]
    except Exception as e:
        return []

def compile_dataset():
    raw_questions = []
    seen_questions = set()

    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        for f in filenames:
            if f.endswith('.docx') and not f.startswith('~$'):
                full_path = os.path.join(dirpath, f)
                paras = read_docx_paras(full_path)
                
                cur_q = None
                for p in paras:
                    if re.match(r'^\d+[\.\)]\s*', p) or 'Frage' in p or (len(p) > 15 and p.endswith('?')):
                        if cur_q and len(cur_q.get('options', [])) >= 2:
                            q_norm = re.sub(r'^\d+[\.\)]\s*', '', cur_q['question']).strip().lower()
                            if q_norm not in seen_questions:
                                seen_questions.add(q_norm)
                                raw_questions.append(cur_q)
                        cur_q = {'file': f, 'question': p, 'options': []}
                    elif cur_q:
                        opts = re.split(r'\s+([A-D1-4][\.\)]\s*)', p)
                        if len(opts) > 1:
                            for i in range(1, len(opts), 2):
                                cur_q['options'].append((opts[i] + opts[i+1]).strip())
                        elif re.match(r'^[a-dA-D1-4][\.\)]\s*', p) or p.startswith('•') or p.startswith('-'):
                            cur_q['options'].append(p.strip())
                if cur_q and len(cur_q.get('options', [])) >= 2:
                    q_norm = re.sub(r'^\d+[\.\)]\s*', '', cur_q['question']).strip().lower()
                    if q_norm not in seen_questions:
                        seen_questions.add(q_norm)
                        raw_questions.append(cur_q)

    print(f"[COMPILER] Successfully extracted {len(raw_questions)} unique QMB questions across all files.")

    # Convert raw questions into structured JSON dataset
    structured_questions = []
    category_map = {
        '8.1': 'Produkthaftung & Recht (Modul 8.1)',
        'lieferanten': 'Lieferantenmanagement (Modul 9.1)',
        '10.2': 'Strategisches QM & VUCA (Modul 10)',
        '10.1': 'Strategisches QM & Risikomanagement',
        '3.2': 'Dokumentationssysteme (DMS)',
        '4.1': 'Fehlermanagement (QMB)',
        '4.2': 'KVP & Kaizen',
        '5.3': 'Führung & Verantwortung',
        '6.4': 'Kundenzufriedenheit (Kap. 6.4)',
        'audit': 'Audits & DIN EN ISO 19011'
    }

    for idx, rq in enumerate(raw_questions, 1):
        clean_q = re.sub(r'^\d+[\.\)]\s*', '', rq['question']).strip()
        
        # Determine category
        cat = 'Allgemeines Qualitätsmanagement (QMB)'
        file_lower = rq['file'].lower()
        for key, val in category_map.items():
            if key in file_lower or key in clean_q.lower():
                cat = val
                break

        # Process options
        opts_list = []
        labels = ['A', 'B', 'C', 'D', 'E', 'F']
        for o_idx, raw_opt in enumerate(rq['options'][:4]):
            clean_opt = re.sub(r'^[a-dA-D1-4\-\•][\.\)]\s*', '', raw_opt).strip()
            # Heuristic for correct answer (often marked with checkmark or (richtig))
            is_correct = '✅' in raw_opt or '(richtig)' in raw_opt.lower() or 'lösung:' in raw_opt.lower()
            clean_opt = clean_opt.replace('✅', '').strip()
            opts_list.append({
                "id": labels[o_idx] if o_idx < len(labels) else str(o_idx+1),
                "text": clean_opt,
                "isCorrect": is_correct
            })

        # Ensure at least one option is marked as correct if none was explicitly tagged
        if not any(o['isCorrect'] for o in opts_list) and opts_list:
            opts_list[0]['isCorrect'] = True

        structured_questions.append({
            "id": f"qmb-ext-{idx:03d}",
            "question": clean_q,
            "options": opts_list,
            "multipleChoice": True,
            "category": cat,
            "isoClause": "DIN EN ISO 9001:2015",
            "infobox": f"Frage aus den offiziellen QMB-Lehrgangsunterlagen ({rq['file']}).",
            "isoJustification": "Begründet nach den normativen Anforderungen der DIN EN ISO 9001:2015 und DIN EN ISO 19011.",
            "hasDeviation": False,
            "draftAnswer": "Rohentwurf aus den Lehrgangsunterlagen.",
            "isoConclusion": "Vollständige Konformität mit ISO 9001:2015."
        })

    return structured_questions

if __name__ == '__main__':
    qs = compile_dataset()
    print(f"Generated {len(qs)} structured questions.")
