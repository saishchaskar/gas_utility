from django.contrib import admin
from django.urls import path
from services.views import  home , login , signup ,requests_list,show_details, edit_profile, add_todo , signout , delete_todo, change_todo,profile

urlpatterns = [
   path('' , home , name='home' ), 
   path('login/' ,login  , name='login'), 
   path('profile/' ,profile  , name='profile'), 
   path('edit/' ,edit_profile , name='edit_profile'), 
   path('signup/' , signup , name='signup'), 
   path('requests/' , requests_list,name='requests' ), 
   path('add-todo/' , add_todo ), 
   path('delete-todo/<int:id>' , delete_todo ), 
   path('show_details/<int:id>' , show_details ), 
   path('change-status/<int:id>/<str:status>' , change_todo ), 
   path('logout/' , signout ), 
]