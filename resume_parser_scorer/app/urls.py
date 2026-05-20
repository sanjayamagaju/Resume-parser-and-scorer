from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ResumeParser

router = DefaultRouter()


urlpatterns = [
    path("", include(router.urls)),
    path("resume-parser/", ResumeParser.as_view()),
]
