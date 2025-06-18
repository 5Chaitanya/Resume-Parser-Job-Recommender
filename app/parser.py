from pdfminer.high_level import extract_text
import io

def extract_resume_text(pdf_file):
    try:
        # Convert uploaded file to bytes stream
        text = extract_text(pdf_file)
        return text
    except Exception as e:
        print(f"[ERROR] Failed to extract text: {e}")
        return ""
