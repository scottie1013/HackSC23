from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('prediction_result', views.prediction_result, name='prediction_result'),
    path('prediction_form', views.prediction_form, name='prediction_form'),
    path('base', views.base, name='base'),
    path('test', views.test, name='test'),
    path('index', views.index, name='index'),
    path('test1', views.test1, name='test1'),
    # path('predict_recurrence', views.predict_recurrence, name='predict_recurrence'),
    path('home', views.PredictCreate, name='home'),
    path('index', views.pred, name='index'),
    path('test2', views.pred, name='test2')
]