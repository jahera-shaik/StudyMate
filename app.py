import streamlit as st
import subprocess
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="StudyMate", page_icon="📚", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
* { font-family: 'Poppins', sans-serif; }
.stApp { background: linear-gradient(135deg, #0a0e2a 0%, #0d2137 40%, #0a3d4a 70%, #0d4f5c 100%); min-height: 100vh; }
.hero { text-align: center; padding: 50px 20px 30px; }
.hero-badge { display: inline-block; background: rgba(0,212,255,0.15); border: 1px solid rgba(0,212,255,0.4); color: #00d4ff; padding: 6px 20px; border-radius: 50px; font-size: 0.8rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 20px; }
.hero h1 { font-size: 3.5rem !important; font-weight: 800 !important; background: linear-gradient(90deg, #00d4ff, #0099cc, #00ffcc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 10px !important; }
.hero-sub { color: rgba(255,255,255,0.6); font-size: 1.1rem; margin-bottom: 10px; }
.powered { color: rgba(0,212,255,0.7); font-size: 0.85rem; letter-spacing: 1px; }
.glass-card { background: rgba(255,255,255,0.05); backdrop-filter: blur(20px); border: 1px solid rgba(0,212,255,0.2); border-radius: 20px; padding: 30px 20px; text-align: center; box-shadow: 0 8px 32px rgba(0,0,0,0.3); }
.card-icon { font-size: 2.5rem; margin-bottom: 12px; }
.card-title { color: #ffffff; font-weight: 600; font-size: 1rem; margin-bottom: 4px; }
.card-sub { color: rgba(255,255,255,0.5); font-size: 0.82rem; }
.stButton>button { background: linear-gradient(90deg, #00d4ff, #0099cc); color: #0a0e2a !important; border: none !important; border-radius: 50px !important; padding: 16px 40px !important; font-size: 1.05rem !important; font-weight: 700 !important; width: 100% !important; box-shadow: 0 4px 20px rgba(0,212,255,0.4) !important; }
.output-box { background: rgba(255,255,255,0.05); backdrop-filter: blur(20px); border: 1px solid rgba(0,212,255,0.25); border-radius: 20px; padding: 35px; color: rgba(255,255,255,0.9) !important; line-height: 1.9; box-shadow: 0 8px 32px rgba(0,0,0,0.3); font-size: 0.95rem; }
.divider { border: none; height: 1px; background: linear-gradient(90deg, transparent, rgba(0,212,255,0.3), transparent); margin: 30px 0; }
.footer { text-align: center; color: rgba(255,255,255,0.3); font-size: 0.78rem; padding: 20px 0 30px; }
#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

def query_coral(sql):
    result = subprocess.run(["coral", "sql", "--format", "json", sql], capture_output=True, text=True)
    return result.stdout

def get_study_plan():
    events = query_coral("SELECT summary, start_date, description FROM google_calendar.events LIMIT 20")
    notion_pages = query_coral("SELECT url FROM notion.search LIMIT 20")
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": f"""You are StudyMate, a smart student assistant.
Google Calendar events: {events}
Notion pages: {notion_pages}
1. Identify exams, assignments, study sessions
2. Create a prioritized study plan for next 7 days
3. Give 3 actionable tips for today
Use emojis, be friendly and motivating!"""}]
    )
    return response.choices[0].message.content

st.markdown("<div class='hero'><div class='hero-badge'>✦ AI Powered Study Assistant ✦</div><h1>📚 StudyMate</h1><p class='hero-sub'>Stop guessing what to study. Let AI figure it out for you.</p><p class='powered'>Coral SQL • Google Calendar • Notion • Groq AI</p></div>", unsafe_allow_html=True)
st.markdown("<hr class='divider'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='glass-card'><div class='card-icon'>📅</div><div class='card-title'>Google Calendar</div><div class='card-sub'>Syncs your events,<br>exams & deadlines</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='glass-card'><div class='card-icon'>📝</div><div class='card-title'>Notion</div><div class='card-sub'>Reads your notes,<br>tasks & assignments</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='glass-card'><div class='card-icon'>🤖</div><div class='card-title'>Groq AI</div><div class='card-sub'>Builds your smart<br>personalized plan</div></div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
col_left, col_center, col_right = st.columns([1, 2, 1])
with col_center:
    if st.button("🚀 Generate My Study Plan"):
        with st.spinner("✨ Reading your calendar & notes..."):
            plan = get_study_plan()
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"<div class='output-box'>{plan.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)
st.markdown("<div class='footer'>Built for Pirates of the Coral-bean Hackathon · WeMakeDevs &nbsp;|&nbsp; By Bibi Jahera Shaik</div>", unsafe_allow_html=True)