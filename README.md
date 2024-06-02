# To-Do-App API

## Visão Geral
Esta aplicação de tarefas fornece uma API robusta para gerenciar tarefas e categorias de tarefas. Ela suporta operações como registro de usuários, login e execução de operações CRUD em tarefas e categorias de tarefas.

## API Endpoints

### Gerenciamento de Usuários
- POST `/register/`: Registrar um novo usuário.
- POST `/login/`: Login para usuários existentes.
- GET `/users/`: Listar todos os usuários.

### Gerenciamento de Tarefas
- GET `/tasks/`: Listar todas as tarefas para o usuário autenticado.
- POST `/tasks/create/`: Criar uma nova tarefa.
- PUT/PATCH `/tasks/update/<int:task_id>/`: Atualizar uma tarefa existente.
- DELETE `/tasks/delete/<int:task_id>/`: Excluir uma tarefa.
- PATCH `/tasks/update_completed/<int:task_id>/`: Marcar uma tarefa como concluída.

### Gerenciamento de Categorias de Tarefas
- GET `/categories/`: Listar todas as categorias de tarefas para o usuário autenticado.
- POST `/categories/create/`: Criar uma nova categoria de tarefa.
- PUT/PATCH `/categories/update/<int:category_id>/`: Atualizar uma categoria de tarefa existente.
- DELETE `/categories/delete/<int:category_id>/`: Excluir uma categoria de tarefa.

## Autenticação
Todos os endpoints requerem autenticação. Certifique-se de estar usando um token válido obtido no ponto de extremidade de login para acessar as rotas protegidas.

## Tratamento de Erros
As respostas da API incluirão um código de status HTTP apropriado e, em caso de erro, um objeto JSON com detalhes sobre o erro.

## Desenvolvimento
Esta API é construída usando Django e Django REST Framework. Ela é projetada para fácil escalabilidade e integração com aplicações front-end.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

