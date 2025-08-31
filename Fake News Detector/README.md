# 📰 AI Fake News Detector – Hackathon Project

## 🚀 Overview
The **AI Fake News Detector** is a hackathon project designed to combat misinformation and build **digital literacy** in line with **SDG 4 (Quality Education)**.  
Users paste a headline or short article, and the system:
1. Uses an **AI model** (HuggingFace Transformers) to analyze credibility.
2. Cross-checks with the **Google Fact Check API**.
3. Outputs a verdict (**True / Fake / Needs Caution**) with a short **educational explanation**.

---

## 🎯 SDG Alignment
- **SDG 4 – Quality Education** → Teaches students digital literacy and critical thinking.  
- **SDG 3 – Good Health & Well-Being** → Detects health misinformation.  
- **SDG 2 – Zero Hunger** → Future extension to verify agricultural and nutrition claims.  

---

## 🛠 Tech Stack
- **Frontend:** Streamlit (Python)  
- **Backend:** HuggingFace Transformers, Google Fact Check API  
- **Optional Database:** SQLite / PostgreSQL for storing fact-check history  
- **Deployment:** Streamlit Cloud / HuggingFace Spaces  

---

## 📂 Project Structure

**Installation**

---

## ⚡ Setup & Installation

1. **Clone repo**
```bash
"git clone https://github.com/Chifuonsteroids/PLP/fake-news-detector.git"
cd fake-news-detector

2. **Create a new environment**
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. **Install dependencies**
pip install -r requirements.txt

4. **Run application**
streamlit run app.py

5. **Deployment**

Deploy via Streamlit Cloud or HuggingFace Spaces.

Ensure requirements.txt is at the root level of the repo.