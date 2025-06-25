from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Todo.objects.create(title=title)
        return redirect('home')
    return render(request, 'add.html')

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('home')
    return render(request, 'edit.html', {'todo': todo})

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('home')

def toggle_complete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('home')
