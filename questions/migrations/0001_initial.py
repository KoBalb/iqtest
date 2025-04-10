# Generated by Django 5.2 on 2025-04-05 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_src', models.CharField(blank=True, max_length=255)),
                ('correct_option', models.PositiveSmallIntegerField()),
                ('points', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_src', models.CharField(blank=True, max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='questions.question')),
            ],
        ),
    ]
