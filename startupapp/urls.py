from django.urls import path
from startupapp import views

urlpatterns = [
    path('', views.index, name="index")
    
]