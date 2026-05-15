# Projeto: Sistema de Cadastro de Tarefas
**Lucas Pereira Faria** 

### 1. `database.sql` (MySQL)
* **Criação**: Gera o banco de dados `primeiro_teste` e a tabela `tarefas`.
* **Estrutura**: Define as colunas `id` (identificador único automático) e `descricao` (o texto da tarefa).
* **Consulta**: Utiliza o comando `SELECT` para validar se os dados foram gravados corretamente.

### 2. `main.py` (Python + FastAPI)
* **Conexão**: Utiliza o `mysql.connector` para entrar no banco de dados com utilizador e senha.
* **Middleware (CORS)**: Configurado para permitir que o navegador (porta 5500) envie dados para a API (porta 8000) sem bloqueios de segurança.
* **Rota POST**: Recebe a tarefa do site e executa o `INSERT INTO` no banco de dados.
* **Rota GET**: Executa o `SELECT` no banco e envia a lista de tarefas de volta para o site.

### 3. `script.js` (JavaScript)
* **`cadastrar()`**: Captura o que foi escrito no `input`, envia para a API via `fetch` e depois limpa o campo.
* **`listar()`**: Pede a lista atualizada à API e reconstrói a lista visual no HTML automaticamente.