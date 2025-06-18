# 📄 Resume Parser + Job Recommender

An intelligent resume parsing and job recommendation system built using **Python**, **Streamlit**, **NLP**, and **Machine Learning**.

## 🚀 Features
- Upload a PDF resume
- Extract skills using NLP and regex-based matchers
- Recommend top 15 jobs based on skill similarity (max 3 per role)
- Clean, centered Streamlit UI for job suggestions

## 🧠 Tech Stack
- Python 3
- Streamlit
- Scikit-learn
- SpaCy
- Pandas

## 📁 Project Structure
resume_recom/
├── app/
│ ├── app.py # Streamlit frontend
│ ├── parser.py # Resume text extractor
│ ├── skills_extractor.py # Skills extractor using CSV DB
│ ├── matcher.py # Job recommender using TF-IDF
├── data/
│ ├── skills.csv # List of standard skills
│ ├── job_description.csv # Job listings

## ⚙️ How to Run
```bash
pip install -r requirements.txt
streamlit run app/app.py

📌 Note
Ensure the data/skills.csv and data/job_description.csv files exist and are correctly formatted.
