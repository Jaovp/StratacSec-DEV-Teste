# StratacSec-DEV-Teste

## Requisitos de Ambiente

- **Python 3.11+**
- **Node.js 24.11.0**
- **Angular CLI 20.3.7**
- **Git**
- **SQLite3**

---

## Configuração do Backend (Django)

### Clonar o projeto

git clone https://github.com/seu-repositorio/gestao_salas.git
cd gestao_salas

### Aplicar migrações
python manage.py makemigrations
python manage.py migrate

### Criar Super Usuario
python manage.py createsuperuser

### Rodar Servidor
python manage.py runserver

O backend estará acessível em:
👉 http://127.0.0.1:8000/api/

---

## Configuração do Frontend (Angular)

### entrar na pasta frontend
cd frontend

### instalar dependências
npm install

### rodar o servidor
ng serve

O frontend estará disponível em:
👉 http://localhost:4200/
