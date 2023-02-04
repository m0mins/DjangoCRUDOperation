from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def employee_list(request):
    return render(request,'employee_list.html')
def employee_form(request):
    return render(request,'employee_form.html')
def employee_delete(request):
    return