import streamlit as st
import tempfile
from parser import extract_resume_text
from skills_extractor import extract_skills
from matcher import load_jobs, recommend_jobs

st.set_page_config(page_title="Resume Job Recommender", layout="centered")
# Centered Main Heading (only this part)
st.markdown("""
    <h1 style='text-align: center; font-size: 2.8rem;'>📄 Job Recommender with Resume</h1>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    resume_text = extract_resume_text(temp_path)
    extracted_skills = extract_skills(resume_text)
    job_df = load_jobs("data/job_description.csv")
    top_jobs = recommend_jobs(extracted_skills, job_df)

    st.subheader("✅ Recommended Jobs")

    if top_jobs.empty:
        st.write("No suitable jobs found.")
    else:
        # Header row without background color
        st.markdown("""
        <style>
            .job-row { display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid #eee; }
            .job-cell { flex: 1; text-align: center; }
            .job-header { font-weight: bold; padding: 8px 0; }
            .job-number { width: 40px; text-align: center; }
        </style>
        <div class='job-row job-header'>
            <div class='job-number'>#</div>
            <div class='job-cell'>Title</div>
            <div class='job-cell'>Company</div>
            <div class='job-cell'>Apply Link</div>
        </div>
        """, unsafe_allow_html=True)

        for idx, row in enumerate(top_jobs.itertuples(), start=1):
            st.markdown(f"""
            <div class='job-row'>
                <div class='job-number'>{idx}</div>
                <div class='job-cell'>{row.title}</div>
                <div class='job-cell'>{row.company}</div>
                <div class='job-cell'>
                    <a href="{row.link}" target="_blank" style="color: #1a73e8; text-decoration: none;">🔗 Link</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
