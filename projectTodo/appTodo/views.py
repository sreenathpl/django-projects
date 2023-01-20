from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import form_task
from .models import task
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView


class listview_task(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'model_db'
    fields = ['name', 'priority', 'date']

class detailview_task(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'data'

class updateview_task(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'data'
    fields = ('name','priority', 'date')

    def get_success_url(self):
        return reverse_lazy('appTodo:cbvdetail',kwargs={'pk':self.object.id})

class deleteview_task(DeleteView):
    model = task
    template_name = 'delete.html'
    succcess_url = reverse_lazy('appTodo:cbvhome')

# Create your views here.
def todo(request):
    model_db = task.objects.all()
    if request.method == "POST":
        name = request.POST.get('name', '')
        priority = request.POST.get('priority')
        date = request.POST.get('task_date')

        model = task(name=name,
                     priority=priority,
                     date=date)
        model.save()

    return render(request, 'home.html', {'model_db': model_db})


def delete(request, task_id):
    del_task = task.objects.get(id=task_id)
    if request.method == "POST":
        del_task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, task_id):
    task_update = task.objects.get(id=task_id)
    form_update = form_task(request.POST or None,
                     request.FILES,
                     instance=task_update)

    if form_update.is_valid():
        print("Form is valid")
        form_update.save()
        return redirect("/")
    return render(request, 'edit.html', {'form': form_update, 'task': task_update})
