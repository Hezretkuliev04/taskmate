from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import Tasklist
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context = {
        'index_text':'Welcome To Index page',
    }
    return render(request ,'index.html', context)


@login_required
def todolist(request):
    if request.method=="POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit = False).manage = request.user
            form.save()
            messages.success(request , 'New Task Added!')
        return redirect('todolist')
    else:   
        all_tasks = Tasklist.objects.filter(manage  = request.user)
        paginator = Paginator(all_tasks, 3  )
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        
        return render(request ,'todolist.html', {'all_tasks': all_tasks})


def delete_task (request , task_id):
    if task.manage == request.user:
        task = Tasklist.objects.get(pk = task_id)
        task.delete()
    else:
        messages.error(request , 'Access Restricted , You are not allowed !')
    return redirect ('todolist')



def complete_task (request , task_id):
    if task.manage == request.user :
        task = Tasklist.objects.get(pk = task_id)
        task.done = True
        task.save()
    else:
        messages.error(request , 'Access Restricted , You are not allowed !')
    return redirect ('todolist')



def pending_task (request , task_id):
    task = Tasklist.objects.get(pk = task_id)
    task.done = False
    task.save()
    return redirect ('todolist')

def edit_task (request, task_id):
     
    if request.method=="POST":
        task = Tasklist.objects.get(pk= task_id)
        form = TaskForm(request.POST or None , instance=task)
        if form.is_valid():
            form.save()
        return redirect('todolist')
    else:   
        task_obj = Tasklist.objects.get(pk = task_id)
        return render(request ,'edit.html', {'task_obj': task_obj} )

def contact(request):
    context = {
        'contact_text':'Welcome To Contact page',
    }
    return render(request ,'contact.html', context)

def about(request):
    context = {
        'about_text':'Welcome To About US page',
    }
    return render(request ,'about.html', context)