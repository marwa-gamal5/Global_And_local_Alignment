# from django.contrib import admin
# from django.urls import path
# from . import views
# #from Local import  views
#
# urlpatterns = [
#
#     path('input', views.input,name='idex'),
#     path('output', views.output, name='idex2'),
#     path('loading',views.load,name='loading'),
#     path('', views.home, name='home'),
#     path('input_local', views.input_local, name='input_local'),
#     path('output_local', views.output_local, name='output_local'),
#     path('home', views.home, name='home'),
#
#
# ]
from django.contrib import admin
from django.urls import path
from . import views
#from Local import  views

urlpatterns = [


    path('', views.home, name='home'),
    path('input', views.input, name='idex'),
    path('output', views.output, name='idex2'),
    path('loading', views.load, name='loading'),
    path('input_local', views.input_local, name='input_local'),
    path('output_local', views.output_local, name='output_local'),
]
