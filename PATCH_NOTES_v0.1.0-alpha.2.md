# 🚀 QMB Trainer - Update v0.1.0-alpha.2 Patch Notes
### 🛠️ *"The Great ISO Audit & Quality Overhaul"*

> **Release Date:** August 5, 2026  
> **Build Version:** `v0.1.0-alpha.2` (Alpha Pre-Release Patch 1)  
> **Target Audience:** QMB Trainees & TÜV ISO 9001 Candidates  

---

## 📢 Developer Announcement

Greetings QMB Auditors & Learners!  

We are excited to deploy **Patch `v0.1.0-alpha.2`** for the **QMB Fahrschul-Trainer**. In this update, our auditing AI subagent fleet performed a deep-level, systematic cross-examination of all **368 unique questions** against official TÜV source documents, German commercial law (**ProdHaftG**, **BGB §823**, **ProdSG**, **MüG**), and international standards (**DIN EN ISO 9001:2015**, **ISO 19011**, **ISO 3000** / **31000**).

Previous AI-generated draft errors (such as default `Option A` bias and inverted multiple-choice flags) have been **100% eliminated**.

---

## 🌟 Major Highlights & Key Improvements

### 🔍 1. Complete Question Bank Audit (368 / 368 Verified)
- **103 Questions Re-aligned:** Fixed incorrect answer keys, inverted logic, and missing options across 10 distinct modules.
- **0 Unanswered Questions:** Eliminated all edge cases where no valid answer option was flagged.
- **Enhanced Accuracy Rate:** Question accuracy is now verified against authoritative ground-truth DOCX solution catalogs.

### 📜 2. Rich ISO Justification & Debate Modals
- Every corrected question now features a dynamic **`⚠️ KORREKTUR`** badge in the Infobox.
- Highlighting exact norm clauses (e.g., *ISO 9001:2015 Clause 9.1.2*, *ISO 31000 Clause 6.5*, *ProdHaftG §1*).
- Interactive debate modal provides side-by-side comparison between draft assumptions and strict ISO conclusions.

---

## 🛠️ Detailed Patch Breakdown

### ⚖️ Product Liability & German Law (Module 8.1)
- **Fixed `qmb-all-019` (ProdHaftG Liability):** Corrected liable parties to EU/EEA Importers and End-Product Manufacturers.
- **Fixed `qmb-all-022` (Market Surveillance Laws):** Removed *AGG (Equal Treatment Act)* from product safety legislation; confirmed *MüG* and *EU-MÜV*.
- **Fixed `qmb-all-025` (Product Safety Measures):** Expanded correct options to include *Goods Receipt Inspection*, *FMEA Risk Methods*, and *Control Process Documentation*.
- **Fixed `qmb-all-027` (Corporate Liability Criteria):** Re-anchored liability to *Proof of Damage* and *Causality* (BGB §823 & ProdHaftG §1).

### 🎲 Risk Management & FMEA (Module 10.1 & ISO 31000)
- **Fixed `qmb-all-172` (ISO 9000 Risk Definition):** Re-aligned definition to *"Effect of uncertainty on objectives"* (ISO 9000:2015 Clause 3.7.9).
- **Fixed `qmb-all-178` & `180` (Risk Assessment & FMEA):** Verified *SWOT Analysis* and *FMEA* as valid assessment methods; updated Risk Priority Number (RPN / RPZ) formulas.
- **Fixed `qmb-all-179` (FMEA Severity Criteria):** Confirmed all 4 impact criteria (*Monetary*, *Environmental*, *Customer Satisfaction*, *Human Safety*).
- **Fixed `qmb-all-184` & `185` (Risk Roles & Governance):** Recognized *Risk Owners*, *System Officers*, and *Risk Managers*; added *Resource Planning* as core building block.
- **Fixed `qmb-all-193` (Risk Acceptance):** Clarified that conscious acceptance of residual risks is permitted under controlled conditions (ISO 31000 §6.5.2).

### 🔄 VUCA & Agile Quality Management (Module 10.2)
- **Fixed `qmb-all-007` (Voice of Customer - VoC):** Inverted incorrect option flags; VoC is now correctly defined as an umbrella term for customer needs and alignment tool.
- **Fixed `qmb-all-157` (Agile Iceberg Metaphor):** Marked *Mindset* and *Principles & Values* as the invisible underwater foundation.
- **Fixed `qmb-all-164` & `169` (PDCA & Lean Startup Integration):** Validated continuous improvement overlaps between Scrum & PDCA, and set Lean Startup phases to *Build-Measure-Learn*.

### ⚙️ Process Management (Chapter 2.2)
- **Fixed `qmb-all-047` & `054` (Key Processes):** Corrected definition of Key Processes to comprise *Core Processes* and *Management Processes* (excluding superfluous processes).

---

## 📱 UI, Standalone & Sync Fixes

- **Single-File Integrity:** Fully synchronized all fixes across `/qmb_fahrschul_app.html` and `/index.html`.
- **Git Deployment:** Hotfixed and pushed directly to `origin/master` (`commit 73525e6`).
- **Cache Optimization:** Recommended hard-refresh (`Ctrl + F5`) for instant client-side update.

---

## ❓ Need Help or Found a Bug?

Use our standalone **`qmb_issue_tracker.html`** tool to submit feedback or report any unclear ISO clauses directly to the class repository!

*Happy Auditing & Good Luck with your TÜV QMB Exam!* 🎓✨
