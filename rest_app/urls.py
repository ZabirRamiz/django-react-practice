# from django.conf.urls import url 
from django.urls import path
from . import views 
 
urlpatterns = [ 
    path('tutorials', views.tutorial_list),
    path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    path('api/tutorials/published', views.tutorial_list_published)
]