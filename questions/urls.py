from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from questions.views import QuestionApiView

urlpatterns = [
    path('questions/', QuestionApiView.as_view()),
]
