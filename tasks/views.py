
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefa
from .forms import TarefaForm

def lista_tarefa(request):
    tarefas = Tarefa.objects.all().order_by('-criada_em')
    return render(request, 'todo_app/lista.html', {'tarefas': tarefas})

def visualizar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    return render(request, 'todo_app/visualizar.html', {'tarefa': tarefa})

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'todo_app/form_tarefa.html', {'form': form, 'titulo': 'Nova Tarefa'})

def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'todo_app/form_tarefa.html', {'form': form, 'titulo': 'Editar Tarefa'})

def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefas')
    return render(request, 'todo_app/confirmar_exclusao.html', {'tarefa': tarefa})