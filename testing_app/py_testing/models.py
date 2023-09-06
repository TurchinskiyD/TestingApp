from django.db import models
from django.urls import reverse


# Create your models here.


class Topic(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField(blank=True)
    detailed_answer = models.TextField(blank=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('question', kwargs={'ques_id': self.pk})



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Test(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, related_name='tests')

    def __str__(self):
        return f"Test on {self.topic}"



