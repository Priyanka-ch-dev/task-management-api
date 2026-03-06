Django Task Management API

Project Overview

This project is a Task Management REST API built using Django REST Framework with JWT Authentication.
Users can register, login, and manage tasks such as creating, updating, deleting, and assigning tasks.

The API also supports filtering, search, permissions, and pagination.

---

Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- Postman (for testing APIs)

---

Project Setup Instructions

1. Clone the repository

git clone <your-repository-link>
cd task-management-api

2. Create virtual environment

python -m venv env

3. Activate environment

Windows:

env\Scripts\activate

4. Install dependencies

pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install django-filter

5. Run migrations

python manage.py makemigrations
python manage.py migrate

6. Run server

python manage.py runserver

Server will run at:

http://127.0.0.1:8000/

---

API Documentation

Authentication APIs

Register User

POST "/api/register"

Example request:

{
 "username": "Priyanka",
 "password": "Priya@2002"
}

---

Login User

POST "/api/login"

Example request:

{
 "username": "Priyanka",
 "password": "Priya@2002"
}

Response:

{
 "access": "access_token",
 "refresh": "refresh_token"
}

---

Refresh Token

POST "/api/token/refresh"

{
 "refresh": "refresh_token"
}

---

Task APIs (JWT Authentication Required)

Create Task

POST "/api/tasks"

Example:

{
 "title": "Task 1",
 "description": "Complete Django assignment",
 "status": "pending",
 "priority": "high",
 "due_date": "2026-03-10",
 "assigned_to": 2
}

---

Get All Tasks

GET "/api/tasks"

---

Get Task by ID

GET "/api/tasks/{id}/"

Example:

GET /api/tasks/1/

---

Update Task

PUT "/api/tasks/{id}/"

---

Delete Task

DELETE "/api/tasks/{id}/"

---

Tasks Created by Logged-in User

GET "/api/my-tasks"

---

Tasks Assigned to Logged-in User

GET "/api/assigned-tasks"

---

Filtering and Search

Filter by status:

/api/tasks?status=completed

Filter by priority:

/api/tasks?priority=high

Search tasks:

/api/tasks?search=project

---

Permissions

The API enforces the following rules:

- Only the task creator can delete a task
- The assigned user can update the task status
- Other users cannot modify the task

---

Validation

The following validations are implemented:

- Title cannot be empty
- Due date cannot be in the past
- Assigned user must exist

---

JWT Authentication Testing Steps

Step 1 — Register User

POST /api/register

Step 2 — Login User

POST /api/login

Copy the access token from response.

---

Step 3 — Use Token in Postman

Add Header:

Authorization : Bearer <access_token>

Now you can access protected endpoints like:

GET /api/tasks
POST /api/tasks

---

Pagination (Bonus Feature)

Pagination is implemented using Django REST Framework.

Example:

GET /api/tasks?page=1

Response format:

{
 "count": 10,
 "next": "http://127.0.0.1:8000/api/tasks/?page=2",
 "previous": null,
 "results": [...]
}

---

Postman Collection

All APIs can be tested using Postman.

Steps:

1. Login and get JWT token
2. Add token in Authorization header
3. Test Task APIs





---

Author

PRIYANKA C H
