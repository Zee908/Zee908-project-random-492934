from django.shortcuts import render, redirect
from .models import Note
from .forms import ContentForm,NoteForm
from django.urls import reverse_lazy  

def Note_list(request):

    context = {
        'note_list': Note.objects.all(),
        'form': ContentForm()
    }
    return render(request, 'index.html', context)

def note_create_view(request):
    form=NoteForm()
    if request.method == "POST":
        form =NoteForm(request.POST)
        if form.is_valid():
            note=form.save()
            return redirect(reverse_lazy('Note:vivew'))
    
def index_view(request):
    note_view=Note_list.objects.all()
    return render(request,'view.html',{'note_return':note_view})



