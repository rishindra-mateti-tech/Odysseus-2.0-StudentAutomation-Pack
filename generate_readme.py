readme_content = """# Odysseus 2.0 Student Pack 🎓💼

An open-source, local-first, privacy-focused automation suite built for students to manage the job application lifecycle. This toolkit hooks into the **Odysseus AI Workspace**, tracks application states automatically via local email triage, and features a local semantic LaTeX resume tailor that matches your real experience to job descriptions without API costs.

## 🚀 Key Features
* **100% Free & Local:** Powered by local inference engines (Conifer/LM Studio) running open-source models like `Qwen-2.5-Coder`—no OpenAI/Gemini API keys or fees required.
* **Email Triage Engine:** Connects securely over IMAP to parse inbox confirmations, track status changes (Applied, Technical Exam, Interview Scheduled), and keep a local database updated.
* **Semantic LaTeX Customizer:** Dynamically adapts raw Overleaf LaTeX blocks to match the contextual needs of a job description without breaking formatting constraints or inventing fake data.
* **One-Click Browser Scraper:** An execution script that scrapes live job descriptions right from your browser window and sends them straight to your local scoring engine.

## 📁 Repository Architecture
```text
Odysseus 2.0 Students pack/
│
├── backend/
│   ├── tailor_engine.py       # Core Python engine connecting to local LLMs
│   └── email_parser.py        # Secure IMAP script to fetch and log applications
│
├── templates/
│   └── resume_template.tex    # Sample LaTeX template for user customization
│
└── browser_extension/
    └── tampermonkey_script.js # Scraper script for LinkedIn/Indeed