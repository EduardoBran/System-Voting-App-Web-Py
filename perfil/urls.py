from django.urls import path

from . import views

app_name = 'perfil'

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('registro', views.registerPage, name='register'),
]
