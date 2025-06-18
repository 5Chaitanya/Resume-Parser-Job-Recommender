import pandas as pd
import re

# Load CSV
skill_df = pd.read_csv("data/skills.csv")

# Lowercase and clean the skills DB
SKILL_DB = skill_df["Skills"].dropna().str.strip().str.lower().tolist()

def extract_skills(resume_text):
    resume_text = resume_text.lower()
    extracted_skills = set()

    for phrase in SKILL_DB:
        # Extract individual sub-skills from the phrase using parentheses or commas
        sub_skills = re.findall(r'\w[\w\s\+#.]+', phrase)  # captures things like "C++", "Power BI"
        for sub_skill in sub_skills:
            sub_skill = sub_skill.strip()
            pattern = r'\b' + re.escape(sub_skill) + r'\b'
            if re.search(pattern, resume_text):
                extracted_skills.add(phrase)
                break  # Once matched, keep the entire phrase and move on

    return sorted(extracted_skills)
