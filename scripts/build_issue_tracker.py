#!/usr/bin/env python3
"""
Standalone QMB Issue Tracker & Bug Report Generator (Client-ID & GitHub Project Direct Integration)
Version: v0.1.0-alpha.2 (Alpha Pre-Release)
"""

import os

APP_VERSION = "0.1.0-alpha.2"

def generate_issue_tracker():
    html_content = r"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>QMB Fehlerberichte & Issue-Tracker (v0.1.0-alpha.2)</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

    :root {{
      --bg-dark: #0a0e17;
      --bg-card: rgba(22, 29, 45, 0.85);
      --border-color: rgba(255, 255, 255, 0.12);
      --primary: #6366f1;
      --primary-hover: #4f46e5;
      --success: #10b981;
      --error: #ef4444;
      --warning: #f59e0b;
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --radius-lg: 16px;
      --radius-md: 12px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-dark);
      background-image: 
        radial-gradient(at 15% 15%, rgba(239, 68, 68, 0.15) 0px, transparent 50%),
        radial-gradient(at 85% 85%, rgba(99, 102, 241, 0.15) 0px, transparent 50%);
      background-attachment: fixed;
      color: var(--text-main);
      min-height: 100vh;
      line-height: 1.6;
      padding: 24px 16px;
    }}

    .container {{ max-width: 1100px; margin: 0 auto; }}

    .glass-panel {{
      background: var(--bg-card);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--border-color);
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.4);
      border-radius: var(--radius-lg);
      padding: 24px;
      margin-bottom: 24px;
    }}

    .glass-card {{
      background: rgba(30, 41, 59, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-md);
      padding: 16px;
      margin-bottom: 12px;
    }}

    header {{ display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; }}

    .logo {{ display: flex; align-items: center; gap: 12px; }}
    .logo-icon {{
      width: 44px; height: 44px; border-radius: 12px;
      background: linear-gradient(135deg, #ef4444 0%, #6366f1 100%);
      display: flex; align-items: center; justify-content: center; font-size: 1.5rem;
    }}

    .badge {{ padding: 4px 10px; border-radius: 20px; font-size: 0.78rem; font-weight: 600; display: inline-block; margin-right: 6px; }}
    .badge-purple {{ background: rgba(99, 102, 241, 0.2); color: #a5b4fc; border: 1px solid rgba(99, 102, 241, 0.4); }}
    .badge-green {{ background: rgba(16, 185, 129, 0.2); color: #6ee7b7; border: 1px solid rgba(16, 185, 129, 0.4); }}
    .badge-red {{ background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); cursor: pointer; }}
    .badge-alpha {{ background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.4); }}
    .badge-client {{ background: rgba(245, 158, 11, 0.2); color: #fcd34d; border: 1px solid rgba(245, 158, 11, 0.4); }}

    .btn-primary {{
      background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
      color: white; border: none; padding: 12px 24px; border-radius: var(--radius-md);
      font-weight: 600; font-size: 1rem; cursor: pointer; transition: all 0.2s ease;
      box-shadow: 0 4px 14px rgba(99, 102, 241, 0.4);
    }}
    .btn-primary:hover {{ transform: translateY(-1px); box-shadow: 0 6px 20px rgba(99, 102, 241, 0.6); }}

    .btn-git {{
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: white; border: none; padding: 10px 16px; border-radius: 8px;
      font-weight: 600; font-size: 0.88rem; cursor: pointer; transition: all 0.2s ease;
      box-shadow: 0 4px 14px rgba(16, 185, 129, 0.3); text-decoration: none; display: inline-flex; align-items: center; gap: 6px;
    }}

    .ctrl-btn {{
      padding: 8px 14px; border-radius: 10px; border: 1px solid var(--border-color);
      background: rgba(255,255,255,0.06); color: var(--text-main); cursor: pointer; font-size: 0.85rem;
    }}

    .form-input, .form-select, .form-textarea {{
      width: 100%; padding: 12px 16px; border-radius: 10px;
      background: rgba(15, 23, 42, 0.7); border: 1px solid var(--border-color);
      color: #fff; font-family: inherit; font-size: 0.95rem; margin-bottom: 14px; outline: none;
    }}
    .form-textarea {{ min-height: 110px; resize: vertical; }}

    .grid-2 {{ display: grid; grid-template-columns: 1fr 1.3fr; gap: 24px; }}
    @media (max-width: 850px) {{ .grid-2 {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>

  <div class="container">
    
    <!-- Header -->
    <div class="glass-panel">
      <header>
        <div class="logo">
          <div class="logo-icon">🐛</div>
          <div>
            <div style="display: flex; align-items: center; gap: 8px;">
              <h1 style="font-size: 1.35rem; font-weight: 800; background: linear-gradient(90deg, #ffffff, #fca5a5); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                QMB Fehlerberichte & Issue-Tracker
              </h1>
              <span class="badge badge-alpha">v0.1.0-alpha.2</span>
            </div>
            <div style="display: flex; align-items: center; gap: 8px; margin-top: 4px;">
              <span style="font-size: 0.8rem; color: var(--text-muted);">Deine eindeutige Client-ID:</span>
              <span id="client-id-display" class="badge badge-client">client-loading</span>
            </div>
          </div>
        </div>

        <div style="display: flex; gap: 8px;">
          <a href="https://github.com/FTPUllrich/qmb-fahrschul-app/issues" target="_blank" class="btn-git">🐙 GitHub Projekt-Board ↗</a>
          <button class="ctrl-btn" onclick="exportJSON()">📥 Export JSON</button>
          <button class="ctrl-btn" onclick="clearAll()">🗑️ Leeren</button>
        </div>
      </header>
    </div>

    <!-- Main Grid -->
    <div class="grid-2">
      
      <!-- Submission Form -->
      <div class="glass-panel">
        <h2 style="font-size: 1.25rem; font-weight: 800; color: #fff; margin-bottom: 8px;">📝 Fehlerbericht / Release-Feedback</h2>
        <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 16px;">
          Jeder Bericht wird mit deiner Client-ID versehen und direkt im GitHub-Projekt registriert:
        </p>

        <form onsubmit="saveReport(event)">
          <label style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600; display: block; margin-bottom: 4px;">Kategorie / Typ:</label>
          <select id="report-type" class="form-select">
            <option value="🐛 Bug / Darstellungsfehler">🐛 Bug / Darstellungsfehler</option>
            <option value="❓ Unklarheit bei ISO-Klausel">❓ Unklarheit bei ISO-Klausel</option>
            <option value="📝 Rechtschreibfehler / Text">📝 Rechtschreibfehler / Text</option>
            <option value="💡 Verbesserungsvorschlag">💡 Verbesserungsvorschlag</option>
          </select>

          <label style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600; display: block; margin-bottom: 4px;">Betroffener Bereich / Modul:</label>
          <select id="report-area" class="form-select">
            <option value="QMB-Stapel (Fragenkatalog)">QMB-Stapel (Fragenkatalog)</option>
            <option value="📖 Sachwörterbuch (QMF & QMB)">📖 Sachwörterbuch (QMF & QMB)</option>
            <option value="🏆 TÜV-Prüfungssimulation">🏆 TÜV-Prüfungssimulation</option>
            <option value="Allgemein / Benutzeroberfläche">Allgemein / Benutzeroberfläche</option>
          </select>

          <label style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600; display: block; margin-bottom: 4px;">Dein Name / Kürzel (optional):</label>
          <input type="text" id="report-author" placeholder="z.B. Stephan (Schulklasse)" class="form-input" />

          <label style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600; display: block; margin-bottom: 4px;">Beschreibung des Problems:</label>
          <textarea id="report-desc" placeholder="Beschreibe das Problem oder die Abweichung so genau wie möglich..." class="form-textarea" required></textarea>

          <button type="submit" class="btn-primary" style="width: 100%;">Fehlerbericht erfassen & ins Git-Projekt senden 🚀</button>
        </form>
      </div>

      <!-- Issues List -->
      <div class="glass-panel">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
          <div>
            <h2 style="font-size: 1.25rem; font-weight: 800; color: #fff;">📋 Meine Berichte (Client-History)</h2>
            <span id="reports-count" style="font-size: 0.8rem; color: var(--text-muted);">0 Berichte</span>
          </div>
        </div>

        <div id="reports-list" style="max-height: 520px; overflow-y: auto;">
          <!-- Rendered by JS -->
        </div>
      </div>

    </div>

  </div>

  <script>
    // Generate or retrieve persistent Client-ID for this user
    let clientId = localStorage.getItem('qmb_client_id');
    if (!clientId) {{
      clientId = 'client-' + Math.random().toString(36).substring(2, 10);
      localStorage.setItem('qmb_client_id', clientId);
    }}
    document.getElementById('client-id-display').innerText = clientId;

    let reports = JSON.parse(localStorage.getItem('qmb_standalone_issues_' + clientId) || '[]');

    function saveReport(e) {{
      e.preventDefault();
      const type = document.getElementById('report-type').value;
      const area = document.getElementById('report-area').value;
      const author = document.getElementById('report-author').value.trim() || 'Mitschüler';
      const desc = document.getElementById('report-desc').value.trim();

      const newReport = {{
        id: 'issue-' + Date.now(),
        clientId: clientId,
        type: type,
        area: area,
        author: author,
        desc: desc,
        status: 'OFFEN',
        timestamp: new Date().toLocaleString('de-DE')
      }};

      reports.unshift(newReport);
      localStorage.setItem('qmb_standalone_issues_' + clientId, JSON.stringify(reports));
      document.getElementById('report-desc').value = '';
      renderList();

      // Automatically construct GitHub issue prefill URL for 1-click submission to GitHub project
      const issueTitle = encodeURIComponent(`[${{newReport.type}}] ${{newReport.area}} (von ${{newReport.author}})`);
      const issueBody = encodeURIComponent(
        `### 🐛 QMB Release Fehlerbericht\n\n` +
        `* **Client-ID**: \`${{newReport.clientId}}\`\n` +
        `* **Autor**: ${{newReport.author}}\n` +
        `* **Typ**: ${{newReport.type}}\n` +
        `* **Bereich**: ${{newReport.area}}\n` +
        `* **Zeitstempel**: ${{newReport.timestamp}}\n\n` +
        `### 📝 Problembeschreibung\n${{newReport.desc}}\n\n` +
        `---\n*Automatisch generiert über den QMB Standalone Issue-Tracker (${{newReport.clientId}})*`
      );

      const githubIssueUrl = `https://github.com/FTPUllrich/qmb-fahrschul-app/issues/new?title=${{issueTitle}}&body=${{issueBody}}`;

      if (confirm('✅ Bericht lokal gespeichert! Möchtest du den Bericht jetzt direkt ins GitHub-Projekt übertragen?')) {{
        window.open(githubIssueUrl, '_blank');
      }}
    }}

    function sendToGit(id) {{
      const r = reports.find(item => item.id === id);
      if (!r) return;
      const issueTitle = encodeURIComponent(`[${{r.type}}] ${{r.area}} (von ${{r.author}})`);
      const issueBody = encodeURIComponent(
        `### 🐛 QMB Release Fehlerbericht\n\n` +
        `* **Client-ID**: \`${{r.clientId}}\`\n` +
        `* **Autor**: ${{r.author}}\n` +
        `* **Typ**: ${{r.type}}\n` +
        `* **Bereich**: ${{r.area}}\n` +
        `* **Zeitstempel**: ${{r.timestamp}}\n\n` +
        `### 📝 Problembeschreibung\n${{r.desc}}\n\n` +
        `---\n*Automatisch generiert über den QMB Standalone Issue-Tracker (${{r.clientId}})*`
      );
      window.open(`https://github.com/FTPUllrich/qmb-fahrschul-app/issues/new?title=${{issueTitle}}&body=${{issueBody}}`, '_blank');
    }}

    function toggleStatus(id) {{
      const r = reports.find(item => item.id === id);
      if (!r) return;
      r.status = r.status === 'OFFEN' ? 'BEHOBEN' : 'OFFEN';
      localStorage.setItem('qmb_standalone_issues_' + clientId, JSON.stringify(reports));
      renderList();
    }}

    function deleteReport(id) {{
      reports = reports.filter(item => item.id !== id);
      localStorage.setItem('qmb_standalone_issues_' + clientId, JSON.stringify(reports));
      renderList();
    }}

    function clearAll() {{
      if (confirm('Möchtest du alle deine erfassten Fehlerberichte löschen?')) {{
        reports = [];
        localStorage.removeItem('qmb_standalone_issues_' + clientId);
        renderList();
      }}
    }}

    function exportJSON() {{
      const dataStr = JSON.stringify(reports, null, 2);
      navigator.clipboard.writeText(dataStr).then(() => {{
        alert('📋 Fehlerberichte als JSON in die Zwischenablage kopiert!');
      }}).catch(() => {{
        prompt('Hier ist dein JSON-Export:', dataStr);
      }});
    }}

    function renderList() {{
      const list = document.getElementById('reports-list');
      document.getElementById('reports-count').innerText = reports.length + " Berichte für " + clientId;

      if (reports.length === 0) {{
        list.innerHTML = `
          <div style="text-align: center; padding: 40px; color: var(--text-muted);">
            <div style="font-size: 2.5rem; margin-bottom: 8px;">🎉</div>
            <p>Unter deiner Client-ID (${{clientId}}) liegen noch keine Berichte vor.</p>
          </div>`;
        return;
      }}

      list.innerHTML = reports.map(r => `
        <div class="glass-card" style="border-left: 4px solid ${{r.status === 'OFFEN' ? '#ef4444' : '#10b981'}};">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 6px;">
            <div>
              <span class="badge ${{r.status === 'OFFEN' ? 'badge-red' : 'badge-green'}}" onclick="toggleStatus('${{r.id}}')">
                ${{r.status === 'OFFEN' ? '🔴 Offen (Klicken zum Schließen)' : '🟢 Behoben'}}
              </span>
              <span class="badge badge-purple">${{r.type}}</span>
            </div>
            <div style="display: flex; gap: 6px;">
              <button onclick="sendToGit('${{r.id}}')" class="btn-git" style="padding: 4px 8px; font-size: 0.75rem;" title="Ins GitHub-Projekt übertragen">🐙 Git</button>
              <button onclick="deleteReport('${{r.id}}')" style="background: transparent; border: none; color: var(--text-muted); cursor: pointer;">🗑️</button>
            </div>
          </div>
          <p style="font-size: 0.92rem; color: #fff; margin-bottom: 8px; line-height: 1.5;">${{r.desc}}</p>
          <div style="display: flex; justify-content: space-between; font-size: 0.78rem; color: var(--text-muted);">
            <span>📍 ${{r.area}} • 👤 ${{r.author}} (ID: ${{r.clientId}})</span>
            <span>🕒 ${{r.timestamp}}</span>
          </div>
        </div>
      `).join('');
    }}

    renderList();
  </script>
</body>
</html>
"""

    for path in ['/home/ole/Projects/qmb-fahrschul-app/qmb_issue_tracker.html', '/home/ole/qmb_issue_tracker.html']:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"[SUCCESS] Client-ID integrated Issue Tracker generated at {path}")

if __name__ == '__main__':
    generate_issue_tracker()
