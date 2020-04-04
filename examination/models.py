from django.db import models
from questionpapers.models import QuestionPaper
from utils.models import Courses, Devices
from accounts.models import User
from questionbank.models import SubQuestion, Option, Answer

# Create your models here.
class Exam(models.Model):
    question_paper = models.OneToOneField(to=QuestionPaper, on_delete=models.PROTECT)
    examination_id = models.CharField(max_length=10)
    course = models.ForeignKey(to=Courses, on_delete=models.CASCADE)
    passkey = models.IntegerField()
    name = models.CharField(max_length=100)
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()

class DynamicExam(models.Model):
    question_paper = models.OneToOneField(to=QuestionPaper, on_delete=models.PROTECT)
    examination_id = models.CharField(max_length=10)
    course = models.ForeignKey(to=Courses, on_delete=models.CASCADE)
    passkey = models.IntegerField()
    name = models.CharField(max_length=100)
    minutes = models.IntegerField()

class Session(models.Model):
    examination = models.ForeignKey(to=Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    device = models.ForeignKey(to=Devices, on_delete=models.PROTECT)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    started_at = models.DateTimeField(auto_now=True)
    is_finished = models.BooleanField(default=False)
    finished_at = models.DateTimeField(null=True)

class Submission(models.Model):
    examination = models.ForeignKey(to=Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(to=SubQuestion, on_delete=models.PROTECT)
    answer = models.ManyToManyField(to=Option)
    is_marked = models.BooleanField(default=False)
    is_submitted = models.BooleanField(default=False)
    last_updated_at = models.DateTimeField(auto_now=True)
