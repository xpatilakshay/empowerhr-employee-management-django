from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.index, name='index'),
   path('all_emp/', views.all_emp, name='all_emp'),
   path('add_emp/', views.add_emp, name='add_emp'),
   path('update_emp/', views.update_emp, name='update_emp'), 
   path('update_emp/<int:emp_id>/', views.update_details, name='update_details'),
   path('remove_emp/', views.remove_emp, name='remove_emp'),
   path('remove_emp/<int:emp_id>', views.remove_emp, name='remove_emp'),
   path('filter_emp/', views.filter_emp, name='filter_emp'),
   
   # Authentication URLs
   path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
   path('register/', views.register, name='register'),
   path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),

   #Emeil
   path('send-mail/', views.send_mail_view, name='send_mail'),

   #Newslettr
   path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),


]