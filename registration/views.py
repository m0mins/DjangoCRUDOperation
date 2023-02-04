from django.shortcuts import render
from django.http import HttpResponse
from . forms import EmployeeForm

def index(request):
    return render(request,'index.html')

def employee_list(request):
    return render(request,'employee_list.html')
def employee_form(request):
    form=EmployeeForm()
    return render(request,'employee_form.html',{'form':form})
def employee_delete(request):
    return