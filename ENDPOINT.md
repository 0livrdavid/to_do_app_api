## API Endpoints

### User Endpoints
- **Registrar Usuário**
  - **Endpoint:** `POST /user/register/`
  - **Payload:** 
    ```json
    {
      "username": "string",
      "name": "string",
      "password": "string",
      "email": "string"
    }
    ```
  - **Result:** 
    ```json
    {
      "success": "boolean",
      "date": "datetime",
      "msg": "string"
    }
    ```
- **Deletar Usuário**
  - **Endpoint:** `DELETE /user/delete/{user_id}/`
  - **Result:** 
    ```json
    {
      "success": "boolean",
      "date": "datetime",
      "msg": "string"
    }
    ```
- **Login Usuário**
  - **Endpoint:** `POST /user/login/`
  - **Payload:** 
    ```json
    {
      "username": "string",
      "password": "string"
    }
    ```
  - **Result:** 
    ```json
    {
      "success": "boolean",
      "date": "datetime",
      "msg": "string"
    }
    ```
- **Listar Usuários**
  - **Endpoint:** `GET /user/list`
  - **Result:** 
    ```json
    {
      "success": "boolean",
      "date": "datetime",
      "msg": "string",
      "data": [
        {
          "id": "int",
          "username": "string",
          "name": "string",
          "email": "string",
          "created_at": "datetime",
          "password": "string"
        }
      ]
    }
    ```
  

### Task Endpoints
- **Listar Tarefas**
  - **Endpoint:** `GET /task/list`
  - **Result:** 
    ```json
    {
      "success": "boolean",
      "date": "datetime",
      "msg": "string"
    }
    ```
- **Criar Tarefa**
  - **Endpoint:** `POST /task/create/`
  - **Payload:** 
    ```json
    {
      "title": "string",
      "description": "string",
      "due_date": "YYYY-MM-DD",
      "category_id": "int"
    }
    ```
  - **Result:** 
    ```json
    {
      "success": "boolean",
      "date": "datetime",
      "msg": "string"
    }
    ```
- **Atualizar Tarefa**
  - **Endpoint:** `PUT /task/update/{task_id}/`
  - **Payload:** 
    ```json
    {
      "title": "string",
      "description": "string",
      "due_date": "YYYY-MM-DD",
      "category_id": "int"
    }
    ```
  - **Result:** 
    ```json
    {
      "success": "boolean",
      "date": "datetime",
      "msg": "string"
    }
    ```
- **Deletar Tarefa**
  - **Endpoint:** `DELETE /task/delete/{task_id}/`
  - **Result:** 
    ```json
    {
      "success": "boolean",
      "date": "datetime",
      "msg": "string"
    }
    ```
- **Atualizar Tarefa Completada**
  - **Endpoint:** `PATCH /task/update_completed/{task_id}/`
  - **Payload:** 
    ```json
    {
      "completed": "boolean"
    }
    ```
  - **Result:** 
    ```json
    {
      "success": "boolean",
      "date": "datetime",
      "msg": "string"
    }
    ```

### Category Endpoints
- **Listar Categorias**
  - **Endpoint:** `GET /category/list`
  - **Result:** 
    ```json
    {
      "success": "boolean",
      "date": "datetime",
      "msg": "string"
    }
    ```
- **Criar Categoria**
  - **Endpoint:** `POST /category/create/`
  - **Payload:** 
    ```json
    {
      "name": "string"
    }
    ```
  - **Result:** 
    ```json
    {
      "success": "boolean",
      "date": "datetime",
      "msg": "string"
    }
    ```
- **Atualizar Categoria**
  - **Endpoint:** `PUT /category/update/{category_id}/`
  - **Payload:** 
    ```json
    {
      "name": "string"
    }
    ```
  - **Result:** 
    ```json
    {
      "success": "boolean",
      "date": "datetime",
      "msg": "string"
    }
    ```
- **Deletar Categoria**
  - **Endpoint:** `DELETE /category/delete/{category_id}/`
  - **Result:** 
    ```json
    {
      "success": "boolean",
      "date": "datetime",
      "msg": "string"
    }
    ```
