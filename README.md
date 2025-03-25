# Task Management API

A Django REST Framework-based API for managing tasks and user assignments.

## Features

- Create and manage tasks
- Assign tasks to multiple users
- Retrieve tasks assigned to specific users
- User management system

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create Django project and apps:
```bash
#django-admin startproject taskmanager .
#python manage.py startapp tasks
#python manage.py startapp users
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## API Usage Guide

### Authentication

The API uses JWT (JSON Web Token) authentication. You need to include the access token in the Authorization header for all protected endpoints.

1. Get Access Token:
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "prashant",
    "password": "prashant"
  }'
```

Response:
```json
{
    "access": "access_token",
    "refresh": "refresh_token"
}
```

2. Refresh Token (when access token expires):
```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{
    "refresh": "refresh_token"
  }'
```

### User Management

1. Create a New User (No authentication required):
```bash
curl -X POST http://localhost:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "prashant",
    "email": "prashant@example.com",
    "password": "prashant",
    "first_name": "Prashant",
    "last_name": "Gupta",
    "mobile": "1234567890"
  }'
```

Response:
```json
{
    "id": 1,
    "username": "prashant",
    "email": "prashant@example.com",
    "first_name": "Prashant",
    "last_name": "Gupta",
    "mobile": "Prashant",
    "created_at": "2025-03-24T10:00:00Z",
    "updated_at": "2025-03-24T10:00:00Z"
}
```

2. Get User Details (Authentication required):
```bash
curl -X GET http://localhost:8000/api/users/1/ \
  -H "Authorization: Bearer access_token"
```

3. List All Users (Authentication required):
```bash
curl -X GET http://localhost:8000/api/users/ \
  -H "Authorization: Bearer access_token"
```

### Task Management

1. Create a New Task:
```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer access_token" \
  -d '{
    "name": "Implement User Authentication",
    "description": "Add JWT authentication to the API",
    "task_type": "FEATURE",
    "status": "PENDING"
  }'
```

2. Assign Task to Users:
```bash
curl -X POST http://localhost:8000/api/tasks/1/assign/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer access_token" \
  -d '{
    "user_ids": [1, 2]
  }'
```

3. Get Task Details:
```bash
curl -X GET http://localhost:8000/api/tasks/1/ \
  -H "Authorization: Bearer access_token"
```

4. List All Tasks:
```bash
curl -X GET http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer access_token"
```

5. Get Tasks for a Specific User:
```bash
curl -X GET "http://localhost:8000/api/tasks/user_tasks/?user_id=1" \
  -H "Authorization: Bearer access_token"
```

6. Update Task Status:
```bash
curl -X PATCH http://localhost:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer access_token" \
  -d '{
    "status": "IN_PROGRESS"
  }'
```

7. Delete a Task:
```bash
curl -X DELETE http://localhost:8000/api/tasks/1/ \
  -H "Authorization: Bearer access_token"
```

## Task Status Options
- PENDING
- IN_PROGRESS
- COMPLETED
- CANCELLED

## Task Types
- FEATURE
- BUG
- DOCUMENTATION
- MAINTENANCE

## Error Responses

The API returns appropriate HTTP status codes and error messages:

- 400 Bad Request: Invalid input data
- 401 Unauthorized: Missing or invalid authentication token
- 403 Forbidden: Insufficient permissions
- 404 Not Found: Resource not found
- 500 Internal Server Error: Server-side error

Example error response:
```json
{
    "error": "Invalid input data",
    "detail": "Task type must be one of: FEATURE, BUG, DOCUMENTATION, MAINTENANCE"
}
``` 