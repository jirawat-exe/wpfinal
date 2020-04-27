from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.add_order, name='add_order'),
    path('test/', views.add_order, name='test'),
]