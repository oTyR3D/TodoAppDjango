from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>/', views.delete_todo, name='delete_todo'),
    path('edit/<int:id>/', views.edit_todo, name='edit_todo'),
]
