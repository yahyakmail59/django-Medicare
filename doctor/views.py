from django.shortcuts import render
from .models import Doctor, Category
from department.models import Department
# Create your views here.

def doctor_list(request):
    category = Category.objects.all()
    doctors_list = Doctor.objects.all()
    department = Department.objects.all()

    context = {
        'doctors_list': doctors_list,
        'category': category,
        'department': department
    }
    return render(request, 'doctor/doctor_list.html', context)


def doctor_detail(request, slug):
    doctor_detail = Doctor.objects.get(slug=slug)
    context = {
        'doctor': doctor_detail
    }
    return render(request, 'doctor/doctor_details.html', context)