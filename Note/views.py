from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .models import Note
from .forms import ContentForm,NoteForm
from django.urls import reverse_lazy  
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
class NoteListViwe(ListView):
    model= Note
    template_name="view.html"
    context_object_name = 'note_list'
    ordering = ['-created_at'] 


class NoteCreateView(CreateView):
    model = Note
    template_name = "index.html"
    context_object_name= "content"
    fields= ['title', 'content']
    success_url = reverse_lazy("index")
    
def form_valid(self, form):
    messages.success(self.request, "یادداشت ذخیره شد.")
    return super().form_valid(form)
  
   
  

def form_invalid(self, form):
        messages.error(self.request, "اطلاعات معتبر نیست.")
        return super().form_invalid(form)


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("note-list")








