from django.urls import path
from .views import Note_list
urlpatterns = [
    path('note/',Note_list,name='note')
]