from django.urls import include, path

from . import views
# from . import api 


app_name='doctor'

urlpatterns = [
    path('',views.home , name='home'),
    path('about/', views.about, name= 'about'),
    ]