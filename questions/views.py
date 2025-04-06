from django.shortcuts import render
from rest_framework import generics
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail

# Create your views here.
class QuestionApiView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class EmailSendView(APIView):
    def post(self, request):
        try:
            send_mail(
                subject='Привет с Django!',
                message='Это тестовое письмо 📨',
                from_email='iqt53416@gmail.com',  # Твоя почта (должна совпадать с EMAIL_HOST_USER)
                recipient_list=['artem.kovalyk79@gmail.com'],  # <-- ЗАХАРДКОЖЕННЫЙ EMAIL
                fail_silently=False,
            )
            return Response({'message': 'Письмо отправлено!'})
        except Exception as e:
            return Response({'error': str(e)}, status=500)