# 🔥 AI Content Agency System

An AI-powered content strategy generator that creates weekly Instagram content plans, improves posts, and exports client-ready reports.

Built with Streamlit + Groq AI + Python.

---

## 🚀 Features

- 🧠 AI-generated 7-day content strategies
- 📅 Instagram content calendar generator
- ✍️ Captions, ideas, and scoring system
- 🔄 Regenerate/improve single posts
- 📊 AI strategy insights (best/worst posts)
- 📥 Export full reports as PDF
- 👥 Multi-client support
- 💾 Save and load history

---

## 🧱 Tech Stack

- Python
- Streamlit
- Groq API (LLaMA 3.1 models)
- ReportLab (PDF export)
- python-dotenv

---

## 📂 Project Structure

ai-agency-system/
│
├── app.py
├── agents/
│   ├── calendar.py
│   ├── clients.py
│   └── export.py
│
├── services/
│   ├── openai_client.py
│   └── db.py
│
├── requirements.txt
├── .env (not pushed)
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone repo
git clone https://github.com/YOUR_USERNAME/ai-agency-system.git  
cd ai-agency-system  

---

### 2. Create virtual environment
python -m venv venv  

source venv/bin/activate   (Mac/Linux)  
venv\Scripts\activate      (Windows)  

---

### 3. Install dependencies
pip install -r requirements.txt  

---

### 4. Add API key

Create a `.env` file:

GROQ_API_KEY=your_api_key_here

---

### 5. Run the app
streamlit run app.py  

---

## 🧠 How It Works

- Select a client
- AI generates a 7-day content plan
- Each post includes:
  - Idea
  - Caption
  - Score
- You can improve individual posts
- Export full strategy as PDF

---

## 📊 Example Output

Monday → Transformation hook post  
Tuesday → Common mistake in niche  
Wednesday → Quick win strategy  
Thursday → Behind the scenes content  
Friday → Authority post  
Saturday → Engagement post  
Sunday → Offer / CTA post  

---

## 🔥 Key Features

- Single-day AI regeneration
- Strategy insights (avg + best + worst)
- Multi-client switching
- PDF export system
- Modular backend structure

---

## ⚠️ Notes

- Requires Groq API key
- Do NOT upload `.env` to GitHub
- Use `.env.example` for sharing setup

---

## 🚀 Future Improvements

- Multi-user login system
- Database upgrade (PostgreSQL / Supabase)
- SaaS-style UI redesign
- Post scheduling automation
- Analytics dashboard per client

---

## 👨‍💻 Author

AI agency automation system built for content generation and strategy optimization.
