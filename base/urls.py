

from django.contrib import admin
from django.urls import path 
from base.views import *
urlpatterns = [
    path('',HomeView.as_view(),name='task_list'),
    path('create/', task_create, name='task_create'),

]
