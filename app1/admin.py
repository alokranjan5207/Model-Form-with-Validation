from django.contrib import admin
from .models import Student,Teacher
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','subject','contact']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['name','salary','contact']