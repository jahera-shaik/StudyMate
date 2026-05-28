import subprocess
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def query_coral(sql):
    result = subprocess.run(
        ["coral", "sql", "--format", "json", sql],
        capture_output=True, text=True
    )
    return result.stdout

def get_study_plan():
    print("Fetching your calendar events...")
    events = query_coral("SELECT summary, start_date, description FROM google_calendar.events LIMIT 20")
    print("Fetching your Notion pages...")
    notion_pages = query_coral("SELECT url FROM notion.search LIMIT 20")
    print("Asking AI to create your study plan...")
    
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
            "content": f"""You are StudyMate, a smart student assistant.
Google Calendar events: {events}
Notion pages: {notion_pages}
1. Identify exams, assignments, study sessions
2. Create a prioritized study plan for next 7 days
3. Give 3 actionable tips for today
Be friendly and motivating!"""
        }]
    )
    
    print("\nYOUR STUDY PLAN:")
    print("=" * 50)
    print(response.choices[0].message.content)

if __name__ == "__main__":
    get_study_plan()