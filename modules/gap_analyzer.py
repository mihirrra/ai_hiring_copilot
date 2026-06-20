import os
from dotenv import load_dotenv


def analyze_gaps(resume_skills, jd_skills):
    missing = [skill for skill in jd_skills if skill not in resume_skills]
    gap_percentage = (len(missing) / len(jd_skills)) * 100
    return {
        "missing_skills": missing,
        "gap_percentage": round(gap_percentage, 2),
        "total_missing": len(missing)
    }

if __name__ == "__main__":
    resume_skills = ["python", "sql", "machine learning", "power bi"]
    jd_skills = ["python", "sql", "machine learning", "power bi", "docker", "aws"]
    
    result = analyze_gaps(resume_skills, jd_skills)
    print(f"Missing Skills: {result['missing_skills']}")
    print(f"Gap Percentage: {result['gap_percentage']}%")
    print(f"Total Missing: {result['total_missing']}")