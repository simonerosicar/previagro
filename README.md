# PREVIAGRO

## Objetivo

PREVIAGRO é um sistema backend para gerenciamento e consulta de previsões agrícolas, desenvolvido com Flask para suportar cadastro de usuários, autenticação JWT e operações CRUD de produtores.

## Tecnologias usadas

* Python
* Flask
* Flask-JWT-Extended
* SQLAlchemy
* SQLite
* Pytest

## Estrutura de pastas

```
previagro/
├── app/
│   ├── routes/
│   ├── services/
│   ├── repositories/
│   └── utils/
├── docs/
├── tests/
├── .github/
├── config.py
├── README.md
├── requirements.txt
├── run.py
└── .env.example
```

## Como instalar

1. Abra um terminal na pasta do projeto.
2. Crie e ative o ambiente virtual:
   * PowerShell:
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   * CMD:
     ```cmd
     python -m venv venv
     .\venv\Scripts\activate.bat
     ```
3. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```
4. Configure as variáveis de ambiente para desenvolvimento:
   ```powershell
   $env:SECRET_KEY = "sua-chave-secreta"
   $env:JWT_SECRET_KEY = "sua-chave-jwt-secreta"
   $env:SQLALCHEMY_DATABASE_URI = "sqlite:///previagro.db"
   ```
5. Execute a aplicação:
   ```powershell
   python run.py
   ```

## Como executar

Após ativar o ambiente virtual e configurar variáveis, rode:

```powershell
python run.py
```

A API ficará disponível em `http://127.0.0.1:5000/`.

## Como testar

Execute os testes automatizados com:

```powershell
.\venv\Scripts\python -m pytest -q
```

## Escolhas técnicas

* **Blueprints**: a aplicação foi segmentada em blueprints para separar rotas de autenticação, produtores e status, facilitando manutenção e expansão.
* **Services**: a lógica de negócio foi isolada em serviços, reduzindo acoplamento entre rotas e acesso a dados.
* **JWT**: autenticação baseada em tokens garante proteção de endpoints de escrita (`POST`, `PUT`, `PATCH`, `DELETE`) e validação de identidade sem estado.
* **SQLAlchemy**: ORM usado para mapear modelos com persistência SQLite, simplificando consultas e transações.

## Uso de IA

Inteligência artificial foi usada para:

* orientar a arquitetura modular do backend;
* validar e organizar o fluxo de autenticação JWT;
* gerar e estruturar testes automatizados com Pytest;
* refatorar serviços, repositórios e blueprints;
* documentar o projeto com README e documentos técnicos.

## User Stories

1. Como agricultor,
   quero consultar previsões agrícolas,
   para planejar minhas plantações.

2. Como técnico agrícola,
   quero cadastrar e atualizar produtores,
   para manter os dados do sistema atualizados.

3. Como administrador,
   quero acessar a API com autenticação segura,
   para proteger a plataforma de acessos não autorizados.

Revisão final acadêmica.
