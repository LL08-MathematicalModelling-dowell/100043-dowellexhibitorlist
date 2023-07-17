from django.urls import path
from . import views

urlpatterns = [
   
    path('search-function/',views.search,name='search_function'),
    path('dowell-search/',views.dowell_search,name='search_function_input'),
    
    
]