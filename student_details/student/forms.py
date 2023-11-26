from django.forms import ModelForm
from student.models import student_basic

class student_basic_form(ModelForm):
    class Meta:
        model=student_basic
        fields=['F_name','L_name','Registration_no']


class student_query_form(ModelForm):
    class Meta:
        model=student_basic
        fields=['Registration_no']



