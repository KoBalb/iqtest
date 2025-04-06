from django.shortcuts import render
from rest_framework import generics
from .models import Question
from .serializers import QuestionSerializer


# Create your views here.
class QuestionApiView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer