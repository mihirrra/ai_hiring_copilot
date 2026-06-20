import os
from dotenv import load_dotenv


def extract_jd_skills(jd_text):
    skills_list = ["python", "sql", "machine learning", "deep learning",
                   "nlp", "langchain", "faiss", "streamlit", "fastapi",
                   "power bi", "excel", "tensorflow", "pytorch", "docker",
                   "git", "aws", "flask", "opencv", "pandas", "numpy","tableau", "seaborn", "matplotlib", "random forest", 
"eda", "power query", "regression", "classification"]
    text_lower = jd_text.lower()
    found_skills = []
    for skill in skills_list:
        if skill in text_lower:
            found_skills.append(skill)
    return found_skills  

'''extract_jd_skills(jd_text)
Takes job description text as input.
Checks which skills from the predefined list appear in the JD.
Returns list of required skills.

Example:
JD says: "We need Python, SQL and Docker experience"
Function returns: ["python", "sql", "docker"]'''



def calculate_ats_score(resume_skills, jd_skills):
    matched = [skill for skill in resume_skills if skill in jd_skills]
    score =(len(matched) / len(jd_skills)) * 100  # use the formula here
    return {
        "score": round(score, 2),
        "matched_skills": matched,
        "total_jd_skills": len(jd_skills),
        "total_matched": len(matched)
    }














if __name__ == "__main__":
    # Sample test
    jd_text = "We need Python, SQL, Machine Learning, Power BI and Docker skills"
    resume_skills = ["python", "sql", "machine learning", "streamlit", "power bi", "excel"]
    
    jd_skills = extract_jd_skills(jd_text)
    result = calculate_ats_score(resume_skills, jd_skills)
    
    print(f"JD Skills: {jd_skills}")
    print(f"Matched Skills: {result['matched_skills']}")
    print(f"ATS Score: {result['score']}%")
    print(f"Matched: {result['total_matched']} out of {result['total_jd_skills']}")