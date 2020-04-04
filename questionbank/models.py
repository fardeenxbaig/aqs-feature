from django.db import models
from django.utils.translation import gettext_lazy as _
import fernet_fields as fields
from accounts.models import User
from django_encrypted_filefield.fields import EncryptedImageField
from utils.models import Topics, CourseOutcome, BloomsCategory, QuestionTypes

# Create your models here.
class Question(models.Model):
    question = fields.EncryptedTextField(_("question"), null=True, blank=True)
    has_images = models.BooleanField(default=False)
    marks = models.IntegerField()
    topic = models.ForeignKey(to=Topics, on_delete=models.CASCADE)
    course_outcomes = models.ManyToManyField(to=CourseOutcome)
    blooms_category = models.ManyToManyField(to=BloomsCategory)
    has_subquestions = models.BooleanField(default=True)
    question_type = models.ForeignKey(to=QuestionTypes, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.question
    

class SubQuestion(models.Model):
    question = fields.EncryptedTextField(_("question"))
    question_id = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    marks = models.IntegerField()
    is_mcq_question = models.BooleanField(default=False)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.question


class Image(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    image = EncryptedImageField(upload_to="public/images/questions/")
    alt_text = models.CharField(max_length=100)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)


class Option(models.Model):
    question = models.ForeignKey(to=SubQuestion, on_delete=models.CASCADE)
    option = fields.EncryptedTextField()
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)


class Answer(models.Model):
    question = models.ForeignKey(to=SubQuestion, on_delete=models.CASCADE)
    answer = models.ForeignKey(to=Option, on_delete=models.CASCADE)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)