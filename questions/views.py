import braintree
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, status
from iqtest import settings
from .braintree_config import gateway
from .models import Question, Result
from .serializers import QuestionSerializer, ResultSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .braintree_config import BraintreeConfig
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



from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Transaction

class BraintreePaymentView(APIView):
    def post(self, request):
        nonce = request.data.get("payment_method_nonce")
        amount = request.data.get("amount")

        if not nonce or not amount:
            return Response({"error": "Missing nonce or amount"}, status=400)

        result = self.create_transaction(nonce, amount)

        if result.is_success:
            try:
                # Получаем payment_method_token из credit_card
                payment_method_token = result.transaction.credit_card['token']

                subscription_result = self.create_subscription(payment_method_token)

                if subscription_result.is_success:
                    # Записываем транзакцию в БД
                    transaction_record = Transaction.objects.create(
                        transaction_id=result.transaction.id,
                        subscription_id=subscription_result.subscription.id,
                        amount=amount,
                        payment_method_token=payment_method_token
                    )

                    return Response({
                        "transaction_id": result.transaction.id,
                        "subscription_id": subscription_result.subscription.id,
                        "transaction_record_id": transaction_record.id  # ID записи в БД
                    })
                else:
                    return Response({
                        "error": "Failed to create subscription",
                        "details": subscription_result.message
                    }, status=400)

            except Exception as e:
                return Response({"error": f"Token error: {str(e)}"}, status=500)

        else:
            return Response({"error": str(result.message)}, status=400)

    def create_transaction(self, nonce, amount):
        return gateway.transaction.sale({
            "amount": amount,
            "payment_method_nonce": nonce,
            "options": {
                "submit_for_settlement": True,
                "store_in_vault": True  # Сохраняем платёжный метод для последующих операций
            }
        })

    def create_subscription(self, payment_method_token):
        # Создаём подписку, используя сохранённый token
        return gateway.subscription.create({
            "payment_method_token": payment_method_token,
            "plan_id": "vnpp"  # ID вашего плана
        })