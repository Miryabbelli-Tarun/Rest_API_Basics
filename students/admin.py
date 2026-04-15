from django.contrib import admin

from students.models import Marks, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(Marks)