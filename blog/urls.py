from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('maqolalar/<int:pk>',views.maqola,name='maqola')
]