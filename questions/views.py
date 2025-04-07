from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, status
from .models import Question, Result
from .serializers import QuestionSerializer, ResultSerializer
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


class ResultAPIView(APIView):
    def post(self, request):
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            post_new = serializer.save()
            return Response({'result': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)