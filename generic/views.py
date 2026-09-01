from django.shortcuts import render, redirect
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from .form import YatriForm
from .models import Yatri

# Create your views here.

class Home(ListView):
    template_name='generic/home.html'
    model=Yatri
    context_object_name='data'

    def get_queryset(self):
        return Yatri.objects.filter(is_deleted=False)
    # def gat_queryset(self):
    #     return Yatri.objects.filter(age__gte=30)

class CreateDataView(CreateView):
    template_name='generic/form.html'
    model=Yatri
    form_class=YatriForm
    success_url='/generic/'

class UpdateDetailView(UpdateView):
    template_name='generic/form.html'
    model=Yatri
    form_class=YatriForm
    success_url='/generic/'

class DeleteDataView(DeleteView):
    model = Yatri
    success_url='/generic/'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()

        return redirect(self.success_url)
    






