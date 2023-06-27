from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.new_work, name = 'home'),
]
