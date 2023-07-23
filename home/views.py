from django.shortcuts import render
from department.models import Department
from doctor.models import Doctor
# Create your views here.


def home(request):
    department = Department.objects.all()
    doctor = Doctor.objects.all()
    context = {
        'department': department,
        'doctor': doctor
    }
    return render (request, 'pages/home.html', context)


def about(request):
    return render (request, 'pages/about.html', {})

