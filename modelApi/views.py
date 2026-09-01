from django.shortcuts import render,redirect
from .form import DetailForm

# Create your views here.
def index(request):
    form=DetailForm()
    if request.method== "POST":
        form=DetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'index.html',{'form':form})