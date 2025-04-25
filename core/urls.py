from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('register/', views.register, name='register'),
    path('reports/', views.reports, name='reports'),
    path('cs/', views.cs, name='cs'),
    path('ml/', views.ml, name='ml'),
    path('economics/', views.economics, name='economics'),
    path('data_analysis/', views.data_analysis, name='data_analysis'),
    path('data_mining/', views.data_mining, name='data_mining'),
    path('finance/', views.finance, name='finance'),
    path('business_analytics/', views.business_analytics, name='business_analytics'),
    path('case_studies/', views.case_studies, name='case_studies'),
    path('business/', views.business, name='business'),
    path('marketing/', views.marketing, name='marketing'),
    path('research/', views.research, name='research'),
    path('login/', views.login_page, name='login'),
    path('exams/', views.exams, name='exams'),
    path('assignment/', views.assignment, name='assignment'),
    path('technical_writing/', views.technical_writing, name='technical_writing'),

]