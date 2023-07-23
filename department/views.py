from django.shortcuts import render
from .models import Department, DepartmentGallery, Category
from doctor.models import Doctor
# Create your views here.

def department_list(request):
    department_list = Department.objects.all()
    context = {
        'department_list': department_list
    }
    return render(request, 'department/department_list.html', context)

def department_detail(request, slug):
    department = Department.objects.get(slug = slug)
    doctor = Doctor.objects.all()
    context = {
        'department': department,
        'doctor': doctor
    }
    return render(request, 'department/department_detail.html', context)