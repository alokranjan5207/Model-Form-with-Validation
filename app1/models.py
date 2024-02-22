from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    name=models.CharField(max_length=40)
    contact=models.IntegerField()
    class Meta:
        abstract=True

class Student(CommonInfo):
    subject_choice=(
        ('maths','maths'),
        ('phy','phy'),
        ('che','che'),
        ('bio','bio'),
        ('Eng','Eng'),
    )
    subject=models.CharField(max_length=30,choices=subject_choice)

class Teacher(CommonInfo):
    salary=models.IntegerField()