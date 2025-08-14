from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefa, name='lista_tarefas'),  # lista todas as tarefas
    path('tarefa/<int:pk>/', views.visualizar_tarefa, name='visualizar_tarefa'),
    path('tarefa/nova/', views.criar_tarefa, name='criar_tarefa'),
    path('tarefa/<int:pk>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefa/<int:pk>/deletar/', views.deletar_tarefa, name='deletar_tarefa'),
    path('tarefa/visualizar/<int:tarefa_id>/', views.visualizar_tarefa, name='visualizar_tarefa_alt'),
]
