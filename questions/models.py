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