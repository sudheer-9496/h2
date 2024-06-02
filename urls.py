from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('garden/', views.garden_view, name='garden'),
       path('furniture/', views.furniture_view, name='furniture'),
          path('fruitslist/', views.fruits_list, name='fruitslist'),
         path('payment/', views.payment_list, name='payment'),
]
