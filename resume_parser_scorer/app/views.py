from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils.utility_functions import extract_text_from_resume, analyse_resume


class ResumeParser(APIView):

    def post(self, request):
        file = request.FILES.get("file")
        job_description = request.data.get("job_description")

        if not file:
            raise ValidationError({"message": "File is required"})

        resume_content = extract_text_from_resume(file)
        response = analyse_resume(resume_content, job_description)
        return Response(response)
