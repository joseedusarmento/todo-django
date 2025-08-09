# 📄 Requisitos - To Do List (Django)

## 1. Introdução
Este documento descreve os requisitos funcionais e não funcionais do sistema **To Do List**, desenvolvido em Django, com objetivo de gerenciar tarefas de forma simples e prática.

---

## 2. Escopo
O sistema permitirá cadastrar, visualizar, editar e excluir tarefas.  
Não será implementada autenticação de usuários nesta versão inicial.

---

## 3. Requisitos Funcionais (RF)
- **RF01** – O sistema deve listar todas as tarefas cadastradas.  
- **RF02** – O sistema deve permitir visualizar os detalhes de uma tarefa.  
- **RF03** – O sistema deve permitir criar novas tarefas.  
- **RF04** – O sistema deve permitir editar uma tarefa existente.  
- **RF05** – O sistema deve permitir excluir uma tarefa.  

---

## 4. Requisitos Não Funcionais (RNF)
- **RNF01** – O sistema deve ser desenvolvido em Django.  
- **RNF02** – O sistema deve utilizar SQLite como banco de dados padrão.  
- **RNF03** – A interface deve ser responsiva e acessível em navegadores modernos.  
- **RNF04** – O sistema deve rodar em servidor local.  

---

## 5. Restrições
- Apenas um usuário interage com o sistema nesta versão.  
- Não haverá integração com APIs externas.  

---

## 6. Prioridades
| Código  | Descrição                                         | Prioridade |
|---------|---------------------------------------------------|------------|
| RF01    | Listar todas as tarefas                           | Essencial  |
| RF02    | Visualizar detalhes de tarefa                     | Essencial  |
| RF03    | Criar novas tarefas                               | Essencial  |
| RF04    | Editar tarefa existente                           | Importante |
| RF05    | Excluir tarefa                                    | Importante |
| RNF03   | Interface responsiva                              | Desejável  |