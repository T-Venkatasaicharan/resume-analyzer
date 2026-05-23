import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.set_page_config(
    page_title="AI Resume Analyzer",
    
    layout="wide"
)

# CSS CODE 
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stTextArea textarea {
    border-radius: 10px;
}

.stButton button {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
}

.result-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #262730;
    color: white;
    margin-top: 20px;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #4CAF50;
}

.subtitle {
    text-align: center;
    color: #AAAAAA;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='title'> AI Resume Analyzer</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Analyze resumes using AI and get improvement suggestions instantly.</div>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    resume = st.text_area(
        "Paste Resume Content",
        height=350,
        placeholder="Paste your resume here..."
    )

with col2:

    job_role = st.text_input(
        "Target Job Role",
        placeholder="Example: Java Backend Developer"
    )

    experience = st.selectbox(
        "Experience Level",
        ["Fresher", "1-3 Years", "3-5 Years", "5+ Years"]
    )

    analyze = st.button("Analyze Resume")

if analyze:

    with st.spinner("Analyzing Resume..."):

        prompt = f"""
        Analyze this resume for the role: {job_role}

        Experience Level: {experience}

        Resume:
        {resume}

        Give:
        1. Strengths
        2. Missing Skills
        3. Improvement Suggestions
        4. ATS Optimization Tips
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = response.choices[0].message.content

        st.markdown(
            f"<div class='result-box'>{result}</div>",
            unsafe_allow_html=True
        )