from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, 'home.html')

def student_register(request):
    return render(request, 'student_register.html')

def student_result(request):
    students = ''
    if 'q' in request.GET:
        q = request.GET['q']
        students = Student.objects.filter(student_id=q)
    else:
        print("Failed")
    return render(request, 'student_result.html', {'students': students})

def about_us(request):
    return render(request, 'about_us.html')

def back_door(request):
    return render(request, 'back_door.html')