from django.shortcuts import render, get_object_or_404
from .models import Tarefa

def lista_tarefa(request):
    tarefas = Tarefa.objects.all().order_by('-criada_em')
    return render(request, 'todo_app/lista.html', {'tarefas': tarefas})

def visualizar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    return render(request, 'todo_app/visualizar.html', {'tarefa': tarefa})
