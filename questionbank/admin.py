from django.contrib import admin

# Register your models here.
from .models import Question, SubQuestion, Option, Answer, Image

admin.site.register(Question)
admin.site.register(SubQuestion)
admin.site.register(Option)
admin.site.register(Answer)
admin.site.register(Image)