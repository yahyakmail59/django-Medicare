from django.urls import include, path

from . import views
# from . import api 


app_name='doctor'

urlpatterns = [
    path('',views.doctor_list , name='doctor_list'),
    # path('add',views.add_doctor , name='add_doctor'),
    path('<str:slug>',views.doctor_detail , name='doctor_detail'),
    ]