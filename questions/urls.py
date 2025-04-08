from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from questions.views import QuestionApiView, ResultAPIView, BraintreePaymentView

urlpatterns = [
    path('questions/', QuestionApiView.as_view()),
    path("result/", ResultAPIView.as_view()),
    path('pay/', BraintreePaymentView.as_view(), name='braintree'),
]
