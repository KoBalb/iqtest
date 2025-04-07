from rest_framework import serializers

from questions.models import Question, Result


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('__all__')

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['gender', 'age', 'email', 'score', 'time_test']

    def validate_gender(self, value):
        # Проверяем, что значение gender либо 'M', либо 'F'
        if value not in ['M', 'F']:
            raise serializers.ValidationError("Gender must be either 'M' or 'F'.")
        return value

    def validate_age(self, value):
        # Проверяем, что значение age соответствует одному из разрешенных вариантов
        if value not in [1, 2, 3, 4, 5]:
            raise serializers.ValidationError("Age must be one of the following values: 1, 2, 3, 4, or 5.")
        return value

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")
        return value

    def validate_score(self, value):
        if value < 0:
            raise serializers.ValidationError("Error: Score cannot be negative.")
        return value

    def validate_time_test(self, value):
        if value <= 0:
            raise serializers.ValidationError("Time test should be greater than zero.")
        return value