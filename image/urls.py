from django.conf.urls import url
from . import views

urlpatterns=[
    
     url(r'^location/', views.image_location, name='location'),
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_image,name = 'pastImage'),
    url(r'^search/', views.search_results, name='search'),
]
