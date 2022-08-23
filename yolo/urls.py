from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('add/', views.add_note),
    path('delete_account', views.delete_account),
    path('delete/<str:id>/', views.delete),
    path('edit/<str:id>/', views.edit),
]