from django.shortcuts import render,get_object_or_404
from student.forms import student_basic_form,student_query_form
from student.models import student_basic
# Create your views here.


def index(request):
    return render (request,'student/index.html')


def form(request):

    form=student_basic_form()
    return render(request,'student/form.html',{'form':form})

#for saving new data

def submit(request):
    if request.method=='POST':
        form_data=student_basic_form(request.POST)
        print('----student_basic.objects.filter(Registration_no=request.POST[Registration_no]).exists()----',student_basic.objects.filter(Registration_no=request.POST['Registration_no']).exists())
        if form_data.is_valid():
            #print('----student_basic.objects.filter(Registration_no=request.POST[Registration_no]).exists()----',student_basic.objects.filter(Registration_no=request.POST['Registration_no']).exists())
            #if(student_basic.objects.filter(Registration_no=request.POST['Registration_no']).exists()):
            sb=student_basic(F_name=request.POST['F_name'],L_name=request.POST['L_name'],Registration_no=request.POST['Registration_no'])
            sb.save()
            return render(request,'student/submit.html',{"message":"succesfully Submitted"})
        else:
            return render(request,'student/submit.html',{"message":"NOT succesfully Submitted"})
                


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




"""def update_action(request):

    if request.method == 'GET':
        Registration_no_query=request.GET['Registration_no']
        
        

        try:
            #Get the data from Database based on Registration no 
            sb_query=student_basic.objects.get(Registration_no=Registration_no_query)
            send_dict={'Found':'Succesfull','F_name':sb_query.F_name,'L_name':sb_query.L_name,'Registration_no':sb_query.Registration_no,'form':form}
        except:
            #if the data is not found with the registration no then this block will execute
            send_dict={'found':'NOT Succesfull','F_name':"XXXXX",'L_name':"XXXXX",'Registration_no':"XXXXX",'Form':form} 
        return render(request,'student/update.html',send_dict)

    if request.method == 'POST':
        try:
            Registration_no_query=request.POST['Registration_no']
            sb_query=student_basic.objects.get(Registration_no=Registration_no_query)
            sb_query.F_name=request.POST['F_name']
            sb_query.L_name=request.POST['L_name']
            sb_query.save()
            return render(request,'student/update_result.html',{{'success':'Succesfully Updated'}})
        
        except:
            
            return render(request,'student/update_result.html',{{'success':'Failed to Update'}})
            
    return render(request,'student/update_result.html')
            """
def update(request):
    form=student_query_form()
    return render(request,'student/update.html',{'get_form':form})

def update_action_read(request):

    if request.method == 'GET':
       
        Registration_no_query=request.GET['Registration_no']
        form=student_query_form()
        

        try:
            #Get the data from Database based on Registration no 
            sb_query=student_basic.objects.get(Registration_no=Registration_no_query)
            send_dict={'Found':True,'F_name':sb_query.F_name,'L_name':sb_query.L_name,'Registration_no':sb_query.Registration_no,'get_form':form}
        except:
            #if the data is not found with the registration no then this block will execute
            send_dict={'found':False,'F_name':"",'L_name':"",'Registration_no':"",'get_form':form} 
    
    return render(request,'student/update.html',send_dict)

def update_action_update(request):


    if request.method == 'GET':
        
        
        try:
            Registration_no_query=request.GET['Registration_no']
            sb_query=student_basic.objects.get(Registration_no=Registration_no_query)
            sb_query.F_name=request.GET['F_name']
            sb_query.L_name=request.GET['L_name']
            sb_query.save()

            return render(request,'student/update_result.html',{'success':'Succesfully Updated'})
        
        except:    
            return render(request,'student/update_result.html',{'success':'Failed to Update'})
               
    return render(request,'student/update_result.html')



def delete(request):
    form=student_query_form()
    return render(request,'student/delete.html',{'get_form':form})


def delete_read(request):
     
    if request.method == 'GET':
       
        Registration_no_query=request.GET['Registration_no']
        form=student_query_form()
        

        try:
            #Get the data from Database based on Registration no 
            sb_query=student_basic.objects.get(Registration_no=Registration_no_query)
            send_dict={'Found':True,'F_name':sb_query.F_name,'L_name':sb_query.L_name,'Registration_no':sb_query.Registration_no,'get_form':form}
        except:
            #if the data is not found with the registration no then this block will execute
            send_dict={'found':False,'F_name':"",'L_name':"",'Registration_no':"",'get_form':form} 
    
    return render(request,'student/delete.html',send_dict)


def delete_result(request):
       
    if request.method == 'GET':
        
        
        try:
            Registration_no_query=request.GET['Registration_no']
            #sb_query=student_basic.objects.get(Registration_no=Registration_no_query)
            sb_delete=get_object_or_404(student_basic,Registration_no=Registration_no_query)
            sb_delete.delete()

            return render(request,'student/delete_result.html',{'success':'Succesfully deleted'})
        
        except:    
            return render(request,'student/delete_result.html',{'success':'Failed to delete'})
               
    return render(request,'student/delete_result.html')