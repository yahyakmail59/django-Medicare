from django.urls import include, path

from . import views
# from . import api 


app_name='department'

urlpatterns = [
    path('',views.department_list , name='department_list'),
    # path('add',views.add_doctor , name='add_doctor'),
    path('<str:slug>',views.department_detail , name='department_detail'),
    ]