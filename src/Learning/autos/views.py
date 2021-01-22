from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View, ListView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy
from autos.models import Auto, Make
from autos.forms import MakeForm

# Create your views here.
class MainView(LoginRequiredMixin,View):
    def get(self, request):
        mc = Make.objects.all()
        al = Auto.objects.all()
        return render(request,
                      'autos/auto_list.html',
                      {'autos':al ,'make':mc})

class AutoCreate(LoginRequiredMixin, View):
    template = 'autos/auto_form.html'
    success_url = reverse_lazy('autos:all')
    def get(self,request):
        form = MakeForm()
        return render(request,
                      self.template,
                      {'form':form})
    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            return render(request,
                          self.template,
                          {'form':form})
        form.save()
        return redirect(self.success_url)

class AutoUpdate(LoginRequiredMixin,View):
    template = 'autos/auto_form.html'
    model = Auto
    success_url = reverse_lazy('autos:all')
    def get(self, request,pk):
        auto = get_object_or_404(self.model,pk=pk)
        form = MakeForm(instance=auto)
        return render(request,
                      self.template,
                      {'form':form})
    def post(self,request,pk):
        auto = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST,instance=auto)
        if not form.is_valid():
            return render(request,
                      self.template,
                      {'form':form})
        form.save()
        return redirect(self.success_url)

class AutoDelete(LoginRequiredMixin, View):
    template = 'autos/auto_delete.html'
    model = Auto
    success_url = reverse_lazy('autos:all')
    def get(self, request, pk):
        auto = get_object_or_404(self.model,pk=pk)
        form = MakeForm(instance=auto)
        return render(request,
                      self.template,
                      {'auto':auto})
    def post(self,request, pk):
        auto = get_object_or_404(self.model, pk=pk)
        auto.delete()
        return render(request,self.success_url)


class MakeView(LoginRequiredMixin, View):
    def get(self,request):
        mc = Make.objects.all()
        return render(request,
                      'autos/make_list.html',
                      {'makes':mc})

class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')