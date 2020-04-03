from django.db import models
from accounts.models import User

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    code = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='media/colleges/')

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=6, unique=True)
    program = models.ForeignKey(to=Program, on_delete=models.CASCADE)
    college = models.ForeignKey(to=College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(to=Department, on_delete=models.CASCADE)
    semester = models.IntegerField()
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CourseCoordinators(models.Model):
    faculty = models.ForeignKey(to=User, on_delete=models.CASCADE)
    course = models.ManyToManyField(to=Courses)

    def __str__(self):
        return self.faculty.first_name + ' ' + self.faculty.last_name


class Chapters(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(to=Courses, on_delete=models.CASCADE)
    module = models.IntegerField()

    def __str__(self):
        return self.name    


class Topics(models.Model):
    name = models.CharField(max_length=200)
    chapter = models.ForeignKey(to=Chapters, on_delete=models.CASCADE)
    part = models.IntegerField()

    def __str__(self):
        return self.name


class CourseOutcome(models.Model):
    name = models.CharField(max_length=1000)
    course = models.ForeignKey(to=Courses, on_delete=models.CASCADE)
    alt_text = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
    

class BloomsCategory(models.Model):
    name = models.CharField(max_length=100)
    alt_text = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
    