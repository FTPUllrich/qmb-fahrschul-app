#!/usr/bin/env python3
"""
Parallel OCR Harvester for QMB MC Images (Default Tesseract Engine)
Version: v0.1.0-alpha.1
"""

import subprocess, glob, os, re, json
from concurrent.futures import ProcessPoolExecutor

root_dir = '/home/ole/Projects/qmb_extracted'

def process_img(img):
    try:
        res = subprocess.run(['tesseract', img, 'stdout'], capture_output=True, text=True, timeout=5)
        txt = res.stdout
        lines = [l.strip() for l in txt.split('\n') if l.strip()]
        if len(lines) >= 3:
            q_line = ''
            opts = []
            for l in lines:
                if '?' in l or re.search(r'\b(Welche|Was|Wer|Wie|Warum|Inwieweit|Welcher|Welches)\b', l, re.I):
                    if not q_line:
                        q_line = l
                    else:
                        q_line += ' ' + l
                elif len(l) > 3 and not l.startswith('Qualit') and not re.match(r'^\d+/\d+', l) and not 'Mehrfachauswahl' in l and not 'Einzelauswahl' in l:
                    opts.append(l)
            if q_line and len(opts) >= 2:
                return {'source': os.path.basename(img), 'question': q_line, 'options': opts}
    except Exception:
        pass
    return None

def main():
    png_files = glob.glob(f'{root_dir}/**/*.PNG', recursive=True) + glob.glob(f'{root_dir}/**/*.png', recursive=True)
    print(f"[FAST OCR] Processing {len(png_files)} PNG image files with 8 parallel workers...")

    with ProcessPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(process_img, png_files))

    results = [r for r in results if r]
    print(f"[FAST OCR] Harvested {len(results)} question cards from all images!")

    out_file = '/home/ole/Projects/qmb-fahrschul-app/scripts/ocr_results.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"[FAST OCR] Saved to {out_file}")

if __name__ == '__main__':
    main()
