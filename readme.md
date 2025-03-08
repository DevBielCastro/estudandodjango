markdown
Copy
# 🚀 API de Gerenciamento de Usuários com Django REST Framework

API RESTful para CRUD de usuários, desenvolvida para estudos em Django. Inclui endpoints para criação, listagem, atualização e exclusão de usuários, além de templates básicos para visualização.

## 📌 Funcionalidades

- **CRUD Completo de Usuários**
- Busca de usuários por nickname
- Paginação de resultados
- Templates HTML integrados com CSS/JS
- Validação de dados via Serializers
- Configuração para MySQL

## 🛠 Tecnologias

- **Backend:** Django 4.2 + Django REST Framework 3.14
- **Frontend:** HTML5, CSS3, JavaScript
- **Banco de Dados:** MySQL 8.0+
- **Outras Ferramentas:** Git, pip

## ⚙️ Instalação

### Pré-requisitos
- Python 3.10+
- MySQL Server
- Git

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/api-usuarios-django.git
cd api-usuarios-django

# Ambiente virtual e dependências
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

pip install -r requirements.txt
Configuração do Banco de Dados
Crie um banco MySQL:

sql
Copy
CREATE DATABASE nome_banco CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
Configure o .env (baseado no .env.example):

ini
Copy
DB_NAME=nome_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
🚦 Execução
bash
Copy
python manage.py migrate
python manage.py runserver
Acesse: http://localhost:8000/api/

🌐 Endpoints da API
Método	Endpoint	Descrição
GET	/api/users/	Lista todos os usuários
POST	/api/users/	Cria novo usuário
GET	/api/users/<str:nick>/	Detalhes de um usuário
PUT	/api/users/<str:nick>/	Atualiza usuário
DELETE	/api/users/<str:nick>/	Exclui usuário
Exemplo de Request (POST):

json
Copy
{
  "user_nickname": "dev_gabriel",
  "user_name": "Gabriel Castro",
  "user_email": "gabriel@example.com",
  "user_age": 25
}
📂 Estrutura do Projeto
Copy
.
├── api_rest
│   ├── migrations/    # Migrações do banco
│   ├── templates/     # HTML templates
│   ├── static/        # CSS/JS assets
│   ├── models.py      # Modelo User
│   ├── views.py       # Lógica da API
│   └── urls.py        # Rotas da API
├── api_root
│   └── settings.py    # Configurações Django
└── requirements.txt   # Dependências
🤝 Como Contribuir
Faça um Fork do projeto

Crie uma Branch (git checkout -b feature/nova-feature)

Commit suas mudanças (git commit -m 'Adiciona nova feature')

Push para a Branch (git push origin feature/nova-feature)

Abra um Pull Request

📝 Licença
Distribuído sob a licença MIT. Veja LICENSE para mais detalhes.

Observações Importantes:

Configure corretamente as permissões do usuário MySQL

Migrações devem ser recriadas em novos ambientes (python manage.py makemigrations)

Para produção, configure ALLOWED_HOSTS no settings.py

Copy

### ✨ Sugestões de Melhoria (Adicione ao README se desejar):
```markdown
## 🚧 Melhorias Futuras
- [ ] Implementar autenticação JWT
- [ ] Adicionar documentação Swagger/OpenAPI
- [ ] Criar sistema de filtros avançados
- [ ] Adicionar testes automatizados