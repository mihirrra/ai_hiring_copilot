import os
from dotenv import load_dotenv

load_dotenv()

def generate_report(candidate_name, ats_result, gap_result, interview_score):
    ats_score = ats_result["score"]
    
    # recommendation logic here
    if ats_score > 80:
        recommendation = "Hire"
    elif ats_score >= 60:
        recommendation = "Maybe"
    else:
        recommendation = "Reject"
    
    return {
        "candidate_name": candidate_name,
        "ats_score": ats_score,
        "matched_skills": ats_result["matched_skills"],
        "missing_skills": gap_result["missing_skills"],
        "interview_score": interview_score,
        "recommendation": recommendation
    }

if __name__ == "__main__":
    ats_result = {"score": 75, "matched_skills": ["python", "sql"], "total_jd_skills": 5, "total_matched": 3}
    gap_result = {"missing_skills": ["docker", "aws"], "gap_percentage": 33.33, "total_missing": 2}
    
    report = generate_report("Mihir Rathod", ats_result, gap_result, 7)
    print(f"Candidate: {report['candidate_name']}")
    print(f"ATS Score: {report['ats_score']}%")
    print(f"Matched Skills: {report['matched_skills']}")
    print(f"Missing Skills: {report['missing_skills']}")
    print(f"Interview Score: {report['interview_score']}/10")
    print(f"Recommendation: {report['recommendation']}")