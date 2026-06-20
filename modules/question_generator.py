import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def generate_questions(resume_skills, jd_skills, missing_skills):
    prompt = f"""You are an expert technical interviewer.
Candidate has these skills: {resume_skills}
Job requires these skills: {jd_skills}
Candidate is missing these skills: {missing_skills}

Generate 5 technical interview questions:
- 3 questions on candidate's existing skills
- 2 questions on missing skills to test basic awareness
Return as numbered list."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    resume_skills = ["python", "sql", "machine learning", "power bi"]
    jd_skills = ["python", "sql", "machine learning", "power bi", "docker"]
    missing_skills = ["docker"]
    
    questions = generate_questions(resume_skills, jd_skills, missing_skills)
    print(questions)