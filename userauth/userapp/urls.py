from .import views
from django.urls import path

urlpatterns = [
    
    path('',views.Home,name='home'),
    path('register/',views.Register,name='register'),
]