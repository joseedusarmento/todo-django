# 📝 To Do List - Django

## 📌 Visão Geral do Sistema
Este projeto é uma aplicação web desenvolvida em **Django** para gerenciamento de tarefas (To Do List).  
O sistema permite que o usuário:
- 📋 Liste todas as tarefas cadastradas
- 🔍 Visualize os detalhes de uma tarefa específica
- ➕ Crie novas tarefas
- ✏️ Edite tarefas existentes
- ❌ Exclua tarefas

O objetivo é fornecer uma interface simples e funcional para organização de atividades diárias.

---

## 👥 Integrantes
- José Eduardo  
- Silvio Ernesto

---

## 🚀 Instruções de Execução

### 1️⃣ Pré-requisitos
Antes de executar o projeto, certifique-se de ter instalado:
- **Python 3.x**
- **Pip** (gerenciador de pacotes do Python)
- **Virtualenv** (opcional, mas recomendado)
- **Django** (versão compatível com o projeto)

### 2️⃣ Clonar o repositório
```
git clone https://github.com/usuario/todo-list.git
cd todo-list
```

### 3️⃣ Criar e ativar o ambiente virtual (opcional, mas recomendado)
```
python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no Linux/Mac
source venv/bin/activate
```

### 4️⃣ Instalar dependências
```
pip install -r requirements.txt
```

### 5️⃣ Executar as migrações do banco de dados
```
python manage.py migrate
```

### 6️⃣ Executar o servidor local
```
python manage.py runserver
```
O sistema estará disponível em: **http://127.0.0.1:8000/**

---

## 🛠 Tecnologias Utilizadas
- **Django** (framework backend)
- **SQLite** (banco de dados padrão do Django)
- **HTML, CSS, JavaScript** (frontend básico)

---

## 📜 Licença
Este projeto é de uso acadêmico e livre para estudos e melhorias.