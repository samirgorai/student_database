from django.shortcuts import render
from student.forms import student_basic_form
from student.models import student_basic
# Create your views here.


def index(request):
    return render (request,'student/index.html')


def form(request):

    form=student_basic_form()
    return render(request,'student/form.html',{'form':form})

def submit(request):
    if request.method=='POST':
        form_data=student_basic_form(request.POST)
        if form_data.is_valid():
            sb=student_basic(F_name=request.POST['F_name'],L_name=request.POST['L_name'],Registration_no=request.POST['Registration_no'])
            sb.save()

    return render(request,'student/submit.html')
            
