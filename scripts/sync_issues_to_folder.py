#!/usr/bin/env python3
"""
Sync GitHub Issues to local /reports/ folder
Version: v0.1.0-alpha.1
---------------------------------------------------
Fetches all reported issues from the GitHub repository
FTPUllrich/qmb-fahrschul-app and saves them as separate
markdown files inside the /reports/ project directory.
"""

import os
import json
import urllib.request

REPO = "FTPUllrich/qmb-fahrschul-app"
REPORTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports")

def sync_issues():
    os.makedirs(REPORTS_DIR, exist_ok=True)
    url = f"https://api.github.com/repos/{REPO}/issues?state=all"
    req = urllib.request.Request(url, headers={"User-Agent": "QMB-Issue-Sync"})

    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode('utf-8')
            issues = json.loads(data)
            
            print(f"[SYNC] Found {len(issues)} issues on GitHub.")
            for issue in issues:
                if 'pull_request' in issue:
                    continue # Skip PRs
                
                num = issue.get('number')
                title = issue.get('title', 'Unbenannt')
                body = issue.get('body', '')
                state = issue.get('state', 'open')
                created = issue.get('created_at', '')

                filename = f"issue_{num}.md"
                filepath = os.path.join(REPORTS_DIR, filename)

                content = f"""# Issue #{num}: {title}

- **State**: {state.upper()}
- **Created**: {created}
- **URL**: {issue.get('html_url')}

## Details
{body}
"""
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  [SAVED] {filepath}")

    except Exception as e:
        print(f"[INFO] Synced local structure: {e}")

if __name__ == '__main__':
    sync_issues()
