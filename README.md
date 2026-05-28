
# 📚 StudyMate - AI Study Planner

> Stop guessing what to study. Let AI figure it out for you.

Built for the **Pirates of the Coral-bean Hackathon** by WeMakeDevs.
<img width="955" height="440" alt="StudyMate" src="https://github.com/user-attachments/assets/78157b42-9120-49cb-bc98-236e1eb9d199" />


---

## 🎯 Problem It Solves
Students waste time figuring out what to study.
StudyMate reads your actual calendar and notes
and tells you exactly what to focus on — automatically.

---

## 🚀 What It Does
- 📅 Reads your Google Calendar events and deadlines
- 📝 Reads your Notion notes and assignments
- 🤖 Uses Groq AI to generate a personalized 7-day study plan
- 🎨 Beautiful web UI built with Streamlit

---

## 🏗️ How It Works

```
Google Calendar + Notion
         ↓
      Coral SQL
         ↓
    Python Agent
         ↓
   Groq (Llama 3.3)
         ↓
  📚 Personalized Study Plan
```

---

## 🌟 Why Coral?
Without Coral, I'd need separate API integrations
for Calendar and Notion. Coral lets me query both
with simple SQL — saving hours of setup.

---

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Coral SQL | Query Google Calendar & Notion |
| Groq AI (Llama 3.3) | Generate study plans |
| Streamlit | Web interface |
| Python | Backend logic |

---

## ⚙️ Setup
1. Install Coral: https://docs.coral.dev
2. Connect sources:
```
coral source add google_calendar
coral source add notion
```
3. Create `.env` file:
```
GROQ_API_KEY=your_key_here
```
4. Install dependencies:
```
pip install streamlit groq python-dotenv
```
5. Run:
```
streamlit run app.py
```

---

## 👩‍💻 Built by
**Bibi Jahera Shaik**
Pirates of the Coral-bean Hackathon · WeMakeDevs
