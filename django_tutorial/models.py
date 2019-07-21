from django.db import models
class Question(models.Model):
    text = models.CharField(max_length=300)
    tarikh = models.DateTimeField()
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    vote = models.IntegerField(default=0)