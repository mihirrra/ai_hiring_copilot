import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def evaluate_answer(question, candidate_answer):
    prompt = f"""You are an expert technical interviewer.
Evaluate this candidate's answer:

Question: {question}
Candidate Answer: {candidate_answer}

Evaluate on 3 criteria:
1. Technical Accuracy (out of 10)
2. Approach and Problem Solving (out of 10)
3. Communication Clarity (out of 10)

Give overall score out of 10 and brief feedback."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    question = "What is machine learning and how did you use it in your projects?"
    answer = "Machine learning is a subset of AI where models learn from data. I used Random Forest in my attrition project to predict employee churn with 85% accuracy."
    
    evaluation = evaluate_answer(question, answer)
    print(evaluation)