from django.urls import path
from .views import NoteCreateView,NoteListViwe

urlpatterns = [
    path('note/',NoteCreateView.as_view(),name='note'),
    path('',NoteListViwe.as_view(),name='index')
]