from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, status

from iqtest import settings
from .models import Question, Result
from .serializers import QuestionSerializer, ResultSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail

# Create your views here.
class QuestionApiView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ResultAPIView(APIView):
    def post(self, request):
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            post_new = serializer.save()
            send_mail(
                subject='IQ test completed!',
                message=f"You took the IQ test and your result: {post_new.score}. Congratulations!",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[post_new.email],
                fail_silently=False,
            )

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)