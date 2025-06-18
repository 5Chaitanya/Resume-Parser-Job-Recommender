# test_parser.py
from app.parser import extract_resume_text

with open("data/sample_res/resume1.pdf", "rb") as f:
    text = extract_resume_text(f)
    print(text)
