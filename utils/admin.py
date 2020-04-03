from django.contrib import admin

from .models import College, Courses, CourseCoordinators, Topics, Chapters, Department, Program

# Register your models here.
admin.site.register(College)
admin.site.register(Courses)
admin.site.register(CourseCoordinators)
admin.site.register(Chapters)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Topics)