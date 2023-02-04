from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index,name='index'),
    path('',views.employee_form, name='employee_form'),

]