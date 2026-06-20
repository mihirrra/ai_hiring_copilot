# 🤖 AI Hiring Copilot

An intelligent hiring platform that automates resume analysis, ATS scoring, mock interviews, and generates hiring reports using Gen AI.

## 🚀 What it does
- Parses resume PDF and extracts technical skills
- Calculates ATS match score against job description
- Identifies skill gaps
- Generates personalized interview questions using Groq LLaMA
- Evaluates candidate answers with AI feedback
- Generates final hiring report with recommendation

## 🛠️ Tech Stack
- **spaCy** — NLP resume parsing
- **Groq LLaMA** — Question generation and answer evaluation
- **Streamlit** — Interactive hiring dashboard
- **Python** — Core logic and modules

## ⚙️ How to Run
1. Clone the repository
2. Install: `pip install -r requirements.txt`
3. Download spaCy model: `python -m spacy download en_core_web_sm`
4. Add `GROQ_API_KEY` in `.env` file
5. Run: `python -m streamlit run app.py`

## 📁 Modules
- `resume_parser.py` — PDF text extraction and skill detection
- `ats_scorer.py` — ATS score calculation
- `gap_analyzer.py` — Missing skill identification
- `question_generator.py` — AI interview question generation
- `answer_evaluator.py` — AI answer evaluation
- `report_generator.py` — Final hiring report
