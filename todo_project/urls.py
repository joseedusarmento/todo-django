from django.contrib import admin
from django.urls import path
from tasks.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_tarefa, name='lista_tarefas'),
    path('tarefa/visualizar/<int:tarefa_id>/', visualizar_tarefa, name='visualizar_tarefa'),
]