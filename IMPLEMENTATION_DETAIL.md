# Task Management API - Project Explanation

## Introduction
This project is a Django REST Framework (DRF) based API that allows users to manage tasks. Users can create tasks, assign them to multiple users, and retrieve tasks assigned to specific users. Authentication is handled using JSON Web Tokens (JWT), ensuring secure access to API endpoints.

## Understanding Django
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It follows the **MVT (Model-View-Template)** architecture, which is similar to **MVC (Model-View-Controller)** but adapted for Django.

Even though Django itself can create APIs using its built-in views and JSONResponse, but Django Rest Framework (DRF) makes API development much easier and more efficient. Here’s why we use DRF instead of plain Django:

1. Simplifies API Development
With DRF, you get built-in tools for serialization, authentication, and pagination, whereas in Django, you'd need to write a lot of custom code.

2. Built-in Serialization
Django does not have built-in serialization for converting complex data (like QuerySets) into JSON. You would need to manually use JsonResponse and format the data yourself.

DRF provides serializers.ModelSerializer, which automatically converts model instances into JSON.

3. Class-Based API Views
Django has function-based views, but they require a lot of boilerplate code for handling different request types (GET, POST, PUT, DELETE).

DRF provides ViewSets and Generic API Views, reducing the need to write repetitive code.

4. Authentication and Permissions
Django only has basic authentication (session-based).

DRF supports multiple authentication methods out-of-the-box, including JWT, OAuth, and Token Authentication.

5. Browsable API
DRF provides an interactive web interface to test API endpoints, whereas plain Django does not.

### MVT vs MVC
- **Model (M)**: Represents the data structure (Database tables)
- **View (V)**: Handles business logic and returns responses (like API responses)
- **Template (T)**: Handles the frontend HTML rendering (not used in this API project)

In contrast, MVC has a **Controller**, which is equivalent to Django's **View** in the MVT model.

## Key Django Concepts Used in This Project
### 1. Models
Django models define the database schema. In this project, we have two main models:
- `User`: Stores user details such as username, email, and mobile number.
- `Task`: Represents a task assigned to users, storing information like name, description, type, and status.

### 2. Serializers
Serializers in Django REST Framework convert complex data (like Django QuerySets) into JSON format so that they can be sent over an API. They also validate incoming data.
- `UserSerializer`: Converts `User` model data into JSON.
- `TaskSerializer`: Converts `Task` model data into JSON.

### 3. Views
Views handle API requests and responses. They define how the application processes requests.
- `TaskViewSet`: Handles creating, retrieving, updating, and deleting tasks.
- `UserViewSet`: Handles user-related operations.

### 4. URLs and Routing
Django uses a URL router to define API endpoints. The **DefaultRouter** from DRF is used to register routes like:
- `/api/tasks/` for task-related operations
- `/api/users/` for user-related operations

## How the Project Works
### Step 1: Setting Up the Project
1. Install Django and Django REST Framework.
2. Configure settings and database.
3. Create models for `User` and `Task`.
4. Run migrations to apply database changes.

### Step 2: Implementing Features
#### 1. User Authentication (JWT)
Users obtain an access token by logging in. This token is included in API requests for authentication.

#### 2. Task Management
- **Creating a Task**: Users can create tasks with a name, description, type, and status.
- **Assigning Tasks**: Tasks can be assigned to multiple users.
- **Fetching User Tasks**: Retrieve tasks assigned to a specific user.
- **Updating Task Status**: Change task status (Pending, In Progress, Completed, etc.).

### Step 3: Running the Application
1. Run the Django server using `python manage.py runserver`.
2. Use API clients (like Postman or Curl) to interact with the endpoints.

## API Response Examples
### 1. Create a Task
**Request:**
```json
POST /api/tasks/
{
    "name": "Implement JWT",
    "description": "Add authentication",
    "task_type": "FEATURE",
    "status": "PENDING"
}
```
**Response:**
```json
{
    "id": 1,
    "name": "Implement JWT",
    "description": "Add authentication",
    "task_type": "FEATURE",
    "status": "PENDING"
}
```

### 2. Assign Users to a Task
**Request:**
```json
POST /api/tasks/1/assign/
{
    "user_ids": [1, 2]
}
```
**Response:**
```json
{"message": "Users assigned successfully"}
```

### 3. Get Tasks for a User
**Request:**
```json
GET /api/users/1/tasks/
```
**Response:**
```json
[
    {
        "id": 1,
        "name": "Implement JWT",
        "status": "PENDING"
    }
]
```

## Conclusion
This project is a simple implementation of a task management system using Django and Django REST Framework. It covers essential backend development concepts, including models, serializers, views, authentication, and API routing. By following this structure, you can extend the application with additional features like role-based access control, notifications, or integration with external services.

