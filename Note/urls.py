from django.urls import path
from .views import Note_list,NoteForm,note_create_view,index_view

urlpatterns = [
    path('note/',Note_list,name='note'),
    path('',index_view,name='index')
]