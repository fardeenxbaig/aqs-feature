from django.db import models
from questionbank.models import Question, Topics
from accounts.models import User

# Create your models here.
class Template(models.Model):
    name = models.CharField(max_length=256)
    marks = models.IntegerField()
    parts = models.IntegerField()
    questions = models.IntegerField()
    has_innovative = models.BooleanField()
    has_casestudy = models.BooleanField()


class QuestionPaper(models.Model):
    template = models.ForeignKey(to=Template, on_delete=models.PROTECT)
    questions = models.ManyToManyField(to=Question)
    syllabus = models.ManyToManyField(to=Topics)
    access_key = models.CharField(max_length=256)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)