from django.contrib import admin
from .models import Question
# Register your models here.
from django.contrib import admin
from .models import Question, Result


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_src','correct_option','score','option_1','option_2','option_3','option_4')  # Здесь можно настроить отображение полей в списке

admin.site.register(Question, QuestionAdmin)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('email', 'score', 'time_test', 'gender', 'age', 'date')