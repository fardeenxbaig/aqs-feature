from django.db import models
from django.utils.translation import gettext_lazy as _
import fernet_fields as fields
from django_encrypted_filefield.fields import EncryptedImageField
from utils.models import Topics, CourseOutcome, BloomsCategory

# Create your models here.
class Question(models.Model):
    question = fields.EncryptedTextField(_("question"), null=True, blank=True)
    has_images = models.BooleanField(default=False)
    marks = models.IntegerField()
    topic = models.ForeignKey(to=Topics, on_delete=models.CASCADE)
    course_outcomes = models.ManyToManyField(to=CourseOutcome)
    blooms_category = models.ManyToManyField(to=BloomsCategory)
    has_subquestions = models.BooleanField(default=True)

    def __str__(self):
        return self.question
    

class SubQuestion(models.Model):
    question = fields.EncryptedTextField(_("question"))
    question_id = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    marks = models.IntegerField()
    is_mcq_question = models.BooleanField(default=False)

    def __str__(self):
        return self.question


class Image(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    image = EncryptedImageField(upload_to="public/images/questions/")
    alt_text = models.CharField(max_length=100)


class Option(models.Model):
    question = models.ForeignKey(to=SubQuestion, on_delete=models.CASCADE)
    option = fields.EncryptedTextField()


class Answer(models.Model):
    question = models.ForeignKey(to=SubQuestion, on_delete=models.CASCADE)
    answer = models.ForeignKey(to=Option, on_delete=models.CASCADE)