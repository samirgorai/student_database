from django.shortcuts import render
from student.forms import student_basic_form,student_query_form
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


def query(request):
    form=student_query_form()
    return render(request,'student/query_student.html',{'form':form})

def querystudent(request):

    if request.method=='GET':
        Registration_no_query=request.GET['Registration_no']

        

        try:
            #Get the data from Database based on Registration no 
            sb_query=student_basic.objects.get(Registration_no=Registration_no_query)
            send_dict={'found':'Succesfull','F_name':sb_query.F_name,'L_name':sb_query.L_name,'Registration_no':sb_query.Registration_no}
        except:
            #if the data is not found with the registration no then this block will execute
            send_dict={'found':'NOT Succesfull','F_name':"XXXXX",'L_name':"XXXXX",'Registration_no':"XXXXX"}         

    return render(request,'student/result.html',send_dict)



            
