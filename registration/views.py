from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import EmployeeForm
from .models import Employee

def index(request):
    return render(request,'index.html')

def employee_list(request):
    context={'employee_list':Employee.objects.all()}

    return render(request,'employee_list.html',context)
def employee_form(request):
    if request.method=='GET':
        form=EmployeeForm()
        return render(request,'employee_form.html',{'form':form})
    else:
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list')

def employee_delete(request):
    return