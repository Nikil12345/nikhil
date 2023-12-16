"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.dis),
    #path('<n>',views.varrule),
    #path('str/<int:n>',views.eve),
    path('home',views.home),
    # path('contact/<t>',views.contact,name="a"),
    path('fainal',views.fainal),
    path('task',views.task),
    path('task2',views.task2),
    path('task3', views.task3),
    path('task4',views.task4),
    path('task5',views.task5),
    path('task6',views.task6),
    # path('key',views.key),
    # path('<v>',views.values),
    path('task7',views.task7),
    path('reg',views.register),
    path('dis',views.disp)


]

