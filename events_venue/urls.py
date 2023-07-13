from django.urls import path

from . import views

app_name = 'events_venue'

urlpatterns = [
    path('', views.index, name='main-view'),
    path('submit/', views.multistepformexample_save, name='multistepform'),
    path('thanks/', views.response_recorded, name='thanks')
]
