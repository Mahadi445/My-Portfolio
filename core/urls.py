from django.urls import path
from core import views

urlpatterns = [
    path('',views.Home_page, name='Home_page'),  
    path('resume/',views.Resume_page, name='Resume_page'),
    path('project/',views.Project_page, name='Project_page'),
    path('contact/',views.Contact_page, name='Contact_page'),
    path('form/',views.Project_form_data, name='Project_Form'), #admin Page Link
]
