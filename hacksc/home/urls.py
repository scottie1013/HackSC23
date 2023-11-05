from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('recurrence', views.recurrence, name='recurrence'),
    path('pred', views.pred, name='pred'),
    path('base', views.base, name='base'),
    path('test', views.test, name='test'),
    path('index', views.pred, name='index'),
]