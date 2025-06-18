import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load job descriptions
def load_jobs(csv_path="data/job_description.csv"):
    return pd.read_csv(csv_path)

# Recommend jobs
def recommend_jobs(resume_skills, job_df, top_n=15, max_per_title=3):
    # Drop rows with missing job descriptions
    job_df = job_df.dropna(subset=['description']).copy()

    # Convert resume skills to string
    resume_text = " ".join(resume_skills).lower()

    # Prepare documents list for TF-IDF
    documents = job_df['description'].str.lower().tolist()
    documents.insert(0, resume_text)  # resume at index 0

    # TF-IDF vectorization
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(documents)

    # Cosine similarity between resume and job descriptions
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # Add similarity scores
    job_df['similarity'] = cosine_similarities

    # Sort by similarity
    job_df = job_df.sort_values(by='similarity', ascending=False)

    # Limit max 3 per title
    limited_jobs = job_df.groupby('title').head(max_per_title)

    # Return top 15 total
    return limited_jobs.head(top_n)[['title', 'company', 'location', 'link', 'similarity']]
