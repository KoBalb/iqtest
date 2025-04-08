from django.contrib import admin
from .models import Question, Transaction
# Register your models here.
from django.contrib import admin
from .models import Question, Result


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_src','correct_option','score','option_1','option_2','option_3','option_4')  # Здесь можно настроить отображение полей в списке

admin.site.register(Question, QuestionAdmin)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('email', 'score', 'time_test', 'gender', 'age', 'date')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'subscription_id', 'amount', 'payment_method_token', 'created_at')

admin.site.register(Transaction, TransactionAdmin)