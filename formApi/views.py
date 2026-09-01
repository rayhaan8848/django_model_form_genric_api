from django.shortcuts import render, redirect
from .form import ContactForm
from .models import Contact

# Create your views here.
def home(request):
    form=ContactForm()
    if request.method == "POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            password=form.cleaned_data['password']
            gender=form.cleaned_data['gender']
            subject=form.cleaned_data['subject']
            Contact.objects.create(name=name,age=age,password=password,gender=gender,subject=subject)
            return redirect('home')
    return render(request, 'home.html',{'form': form})
