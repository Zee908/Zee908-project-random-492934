from django.shortcuts import render
# Create your views here.
def Note_list(request):
    return render(request,'index,html',{})
