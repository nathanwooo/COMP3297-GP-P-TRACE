from django.urls import path,include    
from studysafe_trace import views



urlpatterns = [
    
    path("view_base",views.view_base),
    path("contacts/",views.view_contacts),
    path("venues/",views.view_venues),
    
   
]