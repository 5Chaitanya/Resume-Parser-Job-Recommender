from app.skills_extractor import extract_skills

# Sample resume text (you can change this anytime)
sample_resume_text = """
Hi, I'm Chaitanya, a Data Science student familiar with Python, Pandas, NumPy, and Flask. 
I’ve built ML models and have experience in Power BI, SQL, and Streamlit.
"""

# Run the extractor
skills = extract_skills(sample_resume_text)

# Output the result
print("Extracted Skills:", skills)
