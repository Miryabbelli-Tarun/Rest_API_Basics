from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    roll_no=models.CharField(max_length=10)

    def __str__(self):
        return self.name
subjects=[
    ('maths','maths'),
    ('english','english'),
    ('telugu','telugu'),
]
class Marks(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='marks')
    subject=models.CharField(choices=subjects)
    marks=models.IntegerField()

    def __str__(self):
        return self.subject