from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class Question(models.Model):
    image_src = models.ImageField(upload_to='questions/', blank=True, null=True)
    CORRECT_OPTION_CHOICES = (
        (1, 'Правильна відповідь 1'),
        (2, 'Правильна відповідь 2'),
        (3, 'Правильна відповідь 3'),
        (4, 'Правильна відповідь 4'),
    )
    correct_option = models.PositiveSmallIntegerField(choices=CORRECT_OPTION_CHOICES)
    score = models.PositiveSmallIntegerField(default=10)
    option_1 = models.ImageField(upload_to='options/', blank=True, null=True)
    option_2 = models.ImageField(upload_to='options/', blank=True, null=True)
    option_3 = models.ImageField(upload_to='options/', blank=True, null=True)
    option_4 = models.ImageField(upload_to='options/', blank=True, null=True)

    def __str__(self):
        return f"Question #{self.id}"
    class Meta:
        verbose_name = "Питання"

class Result(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1,  choices=GENDER_CHOICES)
    AGE_CHOICES = (
        (1, '18-24'),
        (2, '25-34'),
        (3, '35-44'),
        (4, '45-60'),
        (5, '60+'),
    )
    age = models.PositiveSmallIntegerField(choices=AGE_CHOICES)
    email = models.EmailField(max_length=254)
    score = models.PositiveSmallIntegerField()
    time_test =  models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} — {self.score}"

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=255)
    subscription_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method_token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.transaction_id} - {self.subscription_id}"