from django.urls import path
from .views import search,dowell_search

urlpatterns = [
   
    path('search-function/',search,name='search_function'),
    path('dowell-search/',dowell_search,name='search_function_input'),
    
    
]