from django.shortcuts import render
from .models import Note
from .form  import Contact
# Create your views here.
def Note_list(request):
    context = {
        'note_list':Note.objects.all()
    }
    return render(request,'index.html',context)
