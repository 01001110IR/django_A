from django.urls import path
from . import views

urlpatterns = [
path('user_profiles/', views.viewall, name='user_profiles'),      
path('users/', views.user_list, name='user_list'),  # רשימת משתמשים
 #! http://127.0.0.1:8000/users/   
    
path('users/<int:user_id>/', views.user_detail, name='user_detail'),  # פרטי משתמש
]#!    http://127.0.0.1:8000/users/<id>/
