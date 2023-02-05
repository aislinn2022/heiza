from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .forms import TodoForm
from .models import task


class listview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'task1'


class detailview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task1'


class updateview(UpdateView):
        model = task
        template_name = 'update.html'
        context_object_name = 'task1'

        def get_success_url(self):
            return reverse_lazy('detailview',kwargs={'pk':self.object.id})


class deleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('listview')














# Create your views here.
def add(request):
    task1=task.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task1=task(name=name,priority=priority,date=date)
        task1.save()
        return redirect('/')

    return render(request,'home.html',{'task1':task1})
# def detail(request):
#
#     return render(request,'detail.html',{'task1':task1})

def delete(request,id):
    task1=task.objects.get(id=id)
    if request.method=='POST':
        task1.delete()
        return redirect('/')
    return render(request,'delete.html')



def edit(request,id):
    task1=task.objects.get(id=id)
    f=TodoForm(request.POST or None, instance=task1)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task1':task1})