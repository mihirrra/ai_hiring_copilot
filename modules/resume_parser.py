import os                           # import library
from dotenv import load_dotenv
from pypdf import PdfReader
import spacy 


load_dotenv()

nlp=spacy.load("en_core_web_sm")   # load nlp english model  It understands English text and can identify names, organizations, skills, and other entities.




'''This function  1:

Takes a PDF file path as input
Opens the PDF using PdfReader
Loops through all pages
Extracts text from each page
Combines all pages into one string
Returns the full text'''

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text



'''This function  2:
Resume text: "I know Python, SQL and Machine Learning"
After lowercase: "i know python, sql and machine learning"
Loop checks:

"python" in text → ✅ added
"sql" in text → ✅ added
"machine learning" in text → ✅ added
"docker" in text → ❌ not added

Returns: ["python", "sql", "machine learning"]'''

def extract_skills(text):
    skills_list = ["python", "sql", "machine learning", "deep learning",
                   "nlp", "langchain", "faiss", "streamlit", "fastapi",
                   "power bi", "excel", "tensorflow", "pytorch", "docker",
                   "git", "aws", "flask", "opencv", "pandas", "numpy","tableau", "seaborn", "matplotlib", "random forest", 
"eda", "power query", "regression", "classification"]
    text_lower = text.lower()
    found_skills = []
    for skill in skills_list:
        if skill in text_lower:
            found_skills.append(skill)
    return found_skills




'''This function  3:
This function combines everything:

Takes PDF path as input
Calls extract_text_from_pdf() to get raw text
Calls extract_skills() to get skills
Returns a dictionary with all extracted info'''


def parse_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    skills = extract_skills(text)
    return {
        "raw_text": text,
        "skills": skills
    }



'''if __name__ == "__main__": means — only run this code if this file is run directly. Not when it's imported by another file.
Example:

You run python resume_parser.py → test runs 
app.py imports parse_resume from this file → test does NOT run '''

if __name__ == "__main__":
    result = parse_resume("data/sample_resume.pdf")
    print("Skills found:", result["skills"])