from django.urls import reverse_lazy

from . models import Task
from django.shortcuts import render, redirect
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class Tasklistview(ListView):
    model=Task
    template_name='home.html'
    context_object_name='task_key'

class Detaillistview(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='star'

class Taskupdateview(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name='t'
    fields=('name', 'priority', 'date')

def del_success_url(self):
    return reverse_lazy('cbvdetail', kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url=reverse_lazy('cbvhome')



def add(request):
    t = Task.objects.all()
    if request.method=="POST":
        n=request.POST.get('name','')
        p=request.POST.get('priority','')
        d= request.POST.get('date', '')
        task=Task(name=n, priority=p, date=d)
        task.save()
    return render(request,"home.html", {'task_key':t})


def delete(request,taskid):
    x=Task.objects.get(id=taskid)
    if request.method == 'POST':
        x.delete()
        return redirect('/')
    return render (request,'delete.html')


def update(request,uid):
    tsk=Task.objects.get(id=uid)
    f=TodoForm(request.POST or None, instance=tsk)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html', {'tsk_key':tsk, 'f_key':f})
