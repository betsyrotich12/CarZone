from django.urls import path

from Pages import views

urlpatterns = [
    path('',views.home, name='home'),
    
]