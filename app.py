import streamlit as st
from modules.resume_parser import parse_resume
from modules.ats_scorer import extract_jd_skills, calculate_ats_score
from modules.gap_analyzer import analyze_gaps
from modules.question_generator import generate_questions
from modules.answer_evaluator import evaluate_answer
from modules.report_generator import generate_report
import tempfile
import os

st.set_page_config(
    page_title="AI Hiring Copilot",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #0f1117;
    background-image: 
        radial-gradient(circle at 20% 50%, rgba(76, 175, 80, 0.05) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(33, 150, 243, 0.05) 0%, transparent 50%),
        url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%234CAF50' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}
.block-container {
    background-color: rgba(15, 17, 23, 0.92);
    border-radius: 15px;
    padding: 2rem;
    border: 1px solid rgba(76, 175, 80, 0.1);
}
            @keyframes pulse {
    0% {box-shadow: 0 0 0 0 rgba(76, 175, 80, 0.4);}
    70% {box-shadow: 0 0 0 10px rgba(76, 175, 80, 0);}
    100% {box-shadow: 0 0 0 0 rgba(76, 175, 80, 0);}
}
.stButton > button {
    background: linear-gradient(135deg, #1e7e34, #4CAF50);
    color: white;
    border: none;
    border-radius: 10px;
    animation: pulse 2s infinite;
    transition: all 0.3s ease;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(76, 175, 80, 0.4);
}
.metric-card {
    background: linear-gradient(135deg, #1e2130, #2d3250);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    border: 1px solid #4CAF50;
    animation: pulse 3s infinite;
}
.metric-card {
    background: linear-gradient(135deg, #1e2130, #2d3250);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    border: 1px solid #4CAF50;
}
.hire {color: #4CAF50; font-size: 24px; font-weight: bold;}
.maybe {color: #FFC107; font-size: 24px; font-weight: bold;}
.reject {color: #F44336; font-size: 24px; font-weight: bold;}
h1 {color: #4CAF50;}
.stProgress > div > div {background-color: #4CAF50;}
</style>
""", unsafe_allow_html=True)

if "stage" not in st.session_state:
    st.session_state.stage = "upload"
if "resume_skills" not in st.session_state:
    st.session_state.resume_skills = []
if "jd_skills" not in st.session_state:
    st.session_state.jd_skills = []
if "ats_result" not in st.session_state:
    st.session_state.ats_result = {}
if "gap_result" not in st.session_state:
    st.session_state.gap_result = {}
if "questions" not in st.session_state:
    st.session_state.questions = []
if "answers" not in st.session_state:
    st.session_state.answers = []
if "answered" not in st.session_state:
    st.session_state.answered = False
if "evaluation" not in st.session_state:
    st.session_state.evaluation = ""

st.markdown("<h1 style='text-align:center'>🤖 AI Hiring Copilot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#888'>Intelligent Resume Analysis & Interview Platform</p>", unsafe_allow_html=True)
st.divider()

steps = ["📄 Upload", "📊 ATS Score", "❓ Interview", "📋 Report"]
col1, col2, col3, col4 = st.columns(4)
for i, (col, step) in enumerate(zip([col1,col2,col3,col4], steps)):
    with col:
        if st.session_state.stage == ["upload","ats","interview","report"][i]:
            st.markdown(f"**🔵 {step}**")
        else:
            st.markdown(f"{step}")

st.divider()

if st.session_state.stage == "upload":
    st.markdown("### 📄 Step 1 — Upload Resume & Job Description")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Upload Resume PDF**")
        resume_file = st.file_uploader("Choose PDF", type=["pdf"])
        candidate_name = st.text_input("Candidate Name")
    with col2:
        st.markdown("**Paste Job Description**")
        jd_text = st.text_area("Job Description", height=200)

    if st.button("🚀 Analyze Resume", use_container_width=True):
        if resume_file and jd_text and candidate_name:
            with st.spinner("🔍 Analyzing resume..."):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(resume_file.read())
                    tmp_path = tmp.name
                result = parse_resume(tmp_path)
                os.unlink(tmp_path)
                jd_skills = extract_jd_skills(jd_text)
                ats_result = calculate_ats_score(result["skills"], jd_skills)
                gap_result = analyze_gaps(result["skills"], jd_skills)
                st.session_state.resume_skills = result["skills"]
                st.session_state.jd_skills = jd_skills
                st.session_state.ats_result = ats_result
                st.session_state.gap_result = gap_result
                st.session_state.candidate_name = candidate_name
                st.session_state.stage = "ats"
                st.rerun()
        else:
            st.error("Please fill all fields")

elif st.session_state.stage == "ats":
    st.markdown("### 📊 Step 2 — ATS Analysis Results")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("ATS Score", f"{st.session_state.ats_result['score']}%")
    with col2:
        st.metric("Matched Skills", st.session_state.ats_result['total_matched'])
    with col3:
        st.metric("Missing Skills", st.session_state.gap_result['total_missing'])

    st.progress(int(st.session_state.ats_result['score'])/100)

    col1, col2 = st.columns(2)
    with col1:
        st.success(f"✅ Matched: {st.session_state.ats_result['matched_skills']}")
    with col2:
        st.error(f"❌ Missing: {st.session_state.gap_result['missing_skills']}")

    if st.button("▶ Start Mock Interview", use_container_width=True):
        with st.spinner("🤖 Generating personalized questions..."):
            questions = generate_questions(
                st.session_state.resume_skills,
                st.session_state.jd_skills,
                st.session_state.gap_result['missing_skills']
            )
            st.session_state.questions = [q for q in questions.split('\n') if q.strip()]
            st.session_state.stage = "interview"
            st.rerun()

elif st.session_state.stage == "interview":
    st.markdown("### ❓ Step 3 — Mock Interview")
    st.info("Answer each question honestly. AI will evaluate your responses.")

    with st.form("interview_form"):
        st.markdown("**Interview Questions:**")
        for q in st.session_state.questions[:5]:
            if q.strip():
                st.markdown(q)
        candidate_answer = st.text_area("Your Answer", height=150)
        submitted = st.form_submit_button("📤 Submit Answer")

    if submitted and candidate_answer:
        with st.spinner("🤖 Evaluating your answer..."):
            evaluation = evaluate_answer(
                str(st.session_state.questions[:5]),
                candidate_answer
            )
            st.session_state.interview_score = 7
            st.session_state.evaluation = evaluation
            st.session_state.answered = True
            st.rerun()

    if st.session_state.get("answered"):
        st.success("✅ Answer evaluated!")
        st.write(st.session_state.evaluation)

    if st.session_state.get("answered"):
        if st.button("📋 Generate Final Report", use_container_width=True):
            st.session_state.stage = "report"
            st.session_state.answered = False
            st.rerun()

elif st.session_state.stage == "report":
    st.markdown("### 📋 Final Hiring Report")
    report = generate_report(
        st.session_state.candidate_name,
        st.session_state.ats_result,
        st.session_state.gap_result,
        st.session_state.interview_score
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("ATS Score", f"{report['ats_score']}%")
    with col2:
        st.metric("Interview Score", f"{report['interview_score']}/10")
    with col3:
        rec = report['recommendation']
        if rec == "Hire":
            st.markdown(f"<p class='hire'>✅ {rec}</p>", unsafe_allow_html=True)
        elif rec == "Maybe":
            st.markdown(f"<p class='maybe'>⚠️ {rec}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p class='reject'>❌ {rec}</p>", unsafe_allow_html=True)

    st.divider()
    st.markdown("**Matched Skills:**")
    st.success(f"{report['matched_skills']}")
    st.markdown("**Missing Skills:**")
    st.error(f"{report['missing_skills']}")

    if st.button("🔄 Start New Analysis", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

st.divider()
st.markdown("<p style='text-align:center;color:#555;font-size:12px'>Built with LangChain · Groq LLaMA · FAISS · Streamlit</p>", unsafe_allow_html=True)