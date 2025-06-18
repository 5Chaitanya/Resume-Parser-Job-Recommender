from app.matcher import load_jobs, recommend_jobs

# Simulate extracted skills
resume_skills = ['python', 'sql','java','html']

job_df = load_jobs()
top_jobs = recommend_jobs(resume_skills, job_df)

print("Top Recommended Jobs:")
print(top_jobs)
