# Generated by Django 4.2.4 on 2023-08-29 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('py_testing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='detailed_answer',
            field=models.TextField(blank=True),
        ),
    ]
