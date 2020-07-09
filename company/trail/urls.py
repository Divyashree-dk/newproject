from trail.views import *
from django.urls import path
urlpatterns = [
    path('', company_list, name='company_list'),
    
    path('<int:id>/details/', company_details, name="company_details"),
    path('<int:id>/edit/', company_edit, name="company_edit"),
     path('add/', company_add, name="company_add"),
    path('<int:id>/delete/', company_delete, name="company_delete"),
    path('<int:id>/agent_details/', agent_details, name="agent_details"),
    path('<int:id>/agent_edit/', agent_edit, name="agent_edit"),
    path('<int:id>/agent_delete/', agent_delete, name="agent_delete"),




    ]