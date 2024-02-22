from django import forms
from .models import Student,Teacher



class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','subject','contact']
    def clean_contact(self):
        inputcontact=self.cleaned_data['contact']
        if inputcontact<0:
            raise forms.ValidationError('contact should be positive')
        return inputcontact

    def clean_name(self):
        inputname=self.cleaned_data['name']
        if inputname[0]!= type(str):
            raise forms.ValidationError('name should be String')
        return inputname



class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields='__all__'