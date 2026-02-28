from django.urls import path
from . import views

urlpatterns = [
    # This maps the empty URL ('') to your list of notes
    path('', views.note_list, name='note_list'),
    
    # This maps the 'create/' URL to your form
    path('create/', views.note_create, name='note_create'),
    
    # This maps the 'delete/' URL for specific notes
    path('delete/<int:pk>/', views.note_delete, name='note_delete'),
]
