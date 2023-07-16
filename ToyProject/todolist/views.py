from django.shortcuts import render, redirect, get_object_or_404
from todolist.models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    todos = Todo.objects.all()
    return render(request, "main.html", {"todos":todos})

@login_required
def write(request):
    if request.method == "POST":
        text=Todo()
        text.content = request.POST.get("content")
        text.author = request.user
        text.save()
        return redirect("todolist:main")
    return render(request, "write.html") 

@login_required
def rewrite(request, id):
    update_todo = get_object_or_404(Todo, pk=id)
    if request.method == 'POST':
        update_todo.content = request.POST.get('content')
        update_todo.save()
        return redirect('todolist:main')
    return render(request, 'rewrite.html', {'update_todo':update_todo})

@login_required
def delete(request, id): 
    delete_todo = get_object_or_404(Todo, pk=id) 
    delete_todo.delete()
    return redirect('todolist:main') 
