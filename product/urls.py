#from django.conf.urls import url
from django.urls import path, re_path
from .views import *
from . import views

urlpatterns =[
    re_path(r'^$', views.index, name='index'),
    path(r'category/<int:id>/', category_view, name='category-detail'),
    re_path(r'about/', views.about, name='about'),
    re_path(r'politique/', views.politique, name='politique'),
    re_path(r'livraison/', views.livraison, name='livraison'),
    ]