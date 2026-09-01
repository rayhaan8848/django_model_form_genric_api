from django.shortcuts import render,redirect
from django.views import View
from .models import People

# Create your views here.
# def home(request):
#     return render(request, 'baseView/home.html')

class IndexView(View):
    def get(self,request):

        return render(request,'baseView/home.html')
    def post(self,request):
        name=request.POST.get('name')
        age=request.POST.get('age')
        People.objects.create(name=name,age=age)
        return redirect('home')
