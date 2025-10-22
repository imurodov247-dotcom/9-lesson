from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('create_profile/',views.create_profile,name='create_profile'),
    path('profiles/',views.profiles,name='profiles'),
    
    
]
