## API Endpoints

### User Endpoints
- **Registrar Usuário**
  - **Endpoint:** `POST /user/signup/`
  - **Headers:** `Content-Type: application/json`
  - **Payload:** 
    ```json
    {
      "username": "teste2",
      "name": "Teste 2",
      "password": "1234",
      "email": "teste2@example.com"
    }
    ```
- **Listar Usuários**
  - **Endpoint:** `GET /user/list`
- **Login Usuário**
  - **Endpoint:** `POST /user/signin/`
  - **Headers:** `Content-Type: application/json`
  - **Payload:** 
    ```json
    {
      "username": "testename",
      "password": "1234"
    }
    ```
- **Logout Usuário**
  - **Endpoint:** `POST /user/signout/`
  - **Headers:** `Authorization: Token ab80a1871f58f7d9168d981c6b0c6296c5a5d65a`
- **Deletar Usuário**
  - **Endpoint:** `DELETE /user/delete/1`

### Task Endpoints
- **Listar Tarefas**
  - **Endpoint:** `GET /task/list/2/`
  - **Headers:** `Authorization: Token c3f0a36256b6e18aa94a0fcf212c8eb1664d2027`
- **Listar Todas as Tarefas**
  - **Endpoint:** `GET /task/list_all/`
- **Criar Tarefa**
  - **Endpoint:** `POST /task/create/`
  - **Headers:** `Content-Type: application/json, Authorization: Token 8e1e94b60160c1f0d056a311cabf2d17b993acaa`
  - **Payload:** 
    ```json
    {
      "title": "Teste Tarefa 1",
      "description": "teste",
      "deadline": "2024-06-12T12:30:00Z",
      "priority": "low",
      "user": 2,
      "task_category": 2
    }
    ```
- **Atualizar Tarefa**
  - **Endpoint:** `PUT /task/update/1/`
  - **Headers:** `Content-Type: application/json, Authorization: Token b7c01eb7b7fa5a3d78494d8129b73c16806b7724`
  - **Payload:** 
    ```json
    {
      "title": "Tarefa Atualizada",
      "description": "Descrição atualizada da tarefa",
      "deadline": "2024-06-12T18:00:00Z",
      "priority": "high",
      "completed": true,
      "task_category": 1,
      "user": 1
    }
    ```
- **Deletar Tarefa**
  - **Endpoint:** `DELETE /task/delete/1/`
  - **Headers:** `Authorization: Token b7c01eb7b7fa5a3d78494d8129b73c16806b7724`

### Category Endpoints
- **Listar Categorias**
  - **Endpoint:** `GET /task_category/list`
  - **Headers:** `Authorization: Token c3f0a36256b6e18aa94a0fcf212c8eb1664d2027`
- **Listar Todas as Categorias**
  - **Endpoint:** `GET /task_category/list_all/`
- **Criar Categoria**
  - **Endpoint:** `POST /task_category/create/`
  - **Headers:** `Content-Type: application/json, Authorization: Token 176e30c3fbf76227cd808147080bcb63be19370c`
  - **Payload:** 
    ```json
    {
      "name": "Categoria 1",
      "description": "Descrição da categoria 1"
    }
    ```
- **Atualizar Categoria**
  - **Endpoint:** `PUT /task_category/update/1/`
  - **Headers:** `Content-Type: application/json, Authorization: Token 6a4b840bbefcb840c49710af1af4058971eddb38`
  - **Payload:** 
    ```json
    {
      "name": "Categoria 1 Atualizada",
      "description": "Descrição atualizada da categoria 1"
    }
    ```
- **Deletar Categoria**
  - **Endpoint:** `DELETE /task_category/delete/2/`
  - **Headers:** `Authorization: Token 6a4b840bbefcb840c49710af1af4058971eddb38`

