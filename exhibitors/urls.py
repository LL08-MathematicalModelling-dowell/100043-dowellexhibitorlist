from django.urls import path

from . import views

app_name = 'exhibitors'

urlpatterns = [
    path('', views.index, name='main-view'),
    path('submit/1/', views.multistepform1_save, name='multistepform1'),
    path('submit/2/', views.multistepform2_save, name='multistepform2'),
    path('thanks/', views.response_recorded, name='thanks'),
    path('view_details/', views.event_details, name='view_details'),
    path('create_email/', views.create_email, name='mail'),
    path('email/', views.send_email, name='send-email'),
    path('files/', views.files_ListView, name='file-list-view'),
    path('search/files/', views.files_ListSearchView, name='file-search-view'),
    path('search/files/export', views.file_exportview, name='file-export-view'),
    path('files/<str:id>/', views.files_DetailView, name='file-detail-view'),
    path('files/delete/<str:id>/', views.file_DeleteView, name='file-delete-view'),
    path('files/update/<str:id>/', views.file_UpdateView, name='file-update-view'),
]
