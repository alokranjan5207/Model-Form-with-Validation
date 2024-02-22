from django.shortcuts import render
from .forms import StudentForm,TeacherForm
# Create your views here.
def student(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=StudentForm()
    else:
        fm=StudentForm()
    return render(request=request,template_name='student.html',context={'form':fm})


def teacher(request):
    if request.method=='POST':
        fm=TeacherForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=TeacherForm()
    else:
        fm=TeacherForm()
    return render(request=request,template_name='teacher.html',context={'form':fm})