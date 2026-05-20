import fitz
import google.genai as genai
import os
from dotenv import load_dotenv

load_dotenv()

from .constants import get_resume_prompt, MODEL


def extract_text_from_resume(pdf_file):
    pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""

    for page in pdf:
        text += page.get_text()

    return text


def configure_gemini_model():
    api_key = os.getenv('GEMINI_API_KEY')
    client = genai.Client(api_key=api_key)

    return client


def analyse_resume(resume_contents, job_description):
    prompt = get_resume_prompt(resume_contents, job_description)

    client = configure_gemini_model()
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )
    return response.text
