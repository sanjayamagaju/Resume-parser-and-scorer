MODEL="gemini-flash-latest"

def get_resume_prompt(resume_content, job_description):
    prompt = f"""
        You are a professional resume analyzer.
    
        Resume:
        {resume_content}
    
        Job Description:
        {job_description}
    
        Task:
        - Analyze the resume against the job description.
        - Give a match score out of 100.
        - Highlight missing skills or experiences.
        - Suggest improvements.
    
        Return the result in structured format:
        Match Score: XX/100
        Missing Skills:
        - ...
        Suggestions:
        - ...
        Summary:
        ...
    """

    return prompt

JOB_DESCRIPTION = """
    We are looking for a Python Backend Developer to develop and maintain backend services for a Resume Parser application.
    
    Responsibilities
        Build REST APIs using Python frameworks like FastAPI, Flask, or Django
        Handle resume upload and parsing (PDF/DOCX/Image)
        Integrate OCR and AI-based data extraction
        Manage databases and backend logic
        Debug, test, and optimize application performance
        
    Required Skills
        Strong knowledge of Python
        Experience with FastAPI, Flask, or Django
        Knowledge of REST APIs and databases
        Familiarity with OCR or document processing
        Basic understanding of Git and Docker
        
    Preferred
        Experience with AI/LLM integration
        Knowledge of NLP or resume parsing systems
"""
