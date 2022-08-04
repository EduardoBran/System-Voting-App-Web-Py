from django.urls import path

from . import views

app_name = 'votacao'
urlpatterns = [
    path('', views.index, name='index')
]
