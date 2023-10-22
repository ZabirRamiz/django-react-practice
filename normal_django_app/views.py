from django.shortcuts import render
from .forms import *
# Create your views here.
def show_student(request):
    student_form_var = student_form()
    return render(request, 'normal_django_app\students.html', {"form": student_form_var})
    