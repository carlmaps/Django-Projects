from django.urls import path
from blog import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
] 