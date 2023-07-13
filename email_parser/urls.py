from django.urls import path

from . import views

app_name = 'newspaper'

urlpatterns = [
    path('', views.index, name='main-view'),
    path('events/', views.EventListView.as_view(), name='list-view'),
    path('event/<pk>/update/', views.UpdateEventView.as_view(), name='event-update'),

]
