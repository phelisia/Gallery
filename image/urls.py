from django.conf.urls import url
from . import views

urlpatterns=[
    
     url(r'^location/', views.image_location, name='location'),
     url(r'^$', views.index, name='index'),
     url(r'^search/', views.search_results, name='search_results'),
]
