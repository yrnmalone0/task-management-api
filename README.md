# Task Management API
This is a Django-based Task Management API that allows users to register, manage their profiles, and handle tasks efficiently. The project includes custom user models, RESTful API endpoints, and media handling for profile pictures.

## Features
- Custom User Model: Extended Django's default user model to include additional fields like bio and profile picture.
- User Registration: API endpoint for new users to register.
- Profile Management: API endpoint for users to update their profile information.
- Media Handling: Support for uploading and serving profile pictures.
- Task Management: Create, view, update, and delete tasks with user authentication.
- JWT Authentication: Secure API endpoints using JSON Web Tokens.
- Task Completion: Mark tasks as completed or pending.
- Filtering and Searching: Filter tasks by status, priority, and due dates.

## Endpoints

### User Endpoints
1. **Register User**
    - **POST** /api/register_user/

        **Request Body (Payload):**
        ```json
        {
            "username": "johndoe",
            "password": "securepassword",
            "email": "johndoe@example.com",
            "bio": "A short bio",
            "profile_picture": "image_file"
        }
        ``` 

        **Response:**
        ```json
        {
            "id": 1,
            "username": "johndoe",
            "email": "johndoe@example.com",
            "bio": "A short bio",
            "profile_picture": "image_file"
        }
        ```

2. **Update Profile**
    - **PUT** /api/update_profile/

        **Request Body (Payload):**
        ```json
        {
            "bio": "Updated bio",
            "profile_picture": "new_image_file"
        }
        ```

        **Response:**
        ```json
        {
            "id": 1,
            "username": "johndoe",
            "email": "johndoe@example.com",
            "bio": "Updated bio",
            "profile_picture": "new_image_file"
        }
        ``` 

### Task Endpoints
1. **Create Task**
    - **POST** /api/create_tasks/

        **Request Body (Payload):**
        ```json
        {
            "title": "New Task",
            "description": "Task description",
            "due_date": "2024-12-31",
            "priority_level": "High"
        }
        ```

        **Response:**
        ```json
        {
            "id": 1,
            "title": "New Task",
            "description": "Task description",
            "due_date": "2024-12-31",
            "priority_level": "High",
            "is_completed": false
        }
        ``` 

2. ***List Tasks**
    - **GET** /api/tasks/

        **Response:**
        ```json
        {
            "id": 1,
            "title": "New Task",
            "description": "Task description",
            "due_date": "2024-12-31",
            "priority_level": "High",
            "is_completed": false
        }
        ``` 

3. ***List Single Task / Get Task Details**
    - **GET** /api/task/{id}/

        **Response:**
        ```json
        {
            "id": 1,
            "title": "New Task",
            "description": "Task description",
            "due_date": "2024-12-31",
            "priority_level": "High",
            "is_completed": false
        }
        ``` 

4. **Update Task**
    - **PUT** /api/update_task/{id}/

        **Request Body (Payload):**
        ```json
        {
            "title": "Updated Task",
            "description": "Updated description",
            "due_date": "2025-01-15",
            "priority_level": "Medium",
            "is_completed": true
        }
        ```

        **Response:**
        ```json
        {
            "id": 1,
            "title": "Updated Task",
            "description": "Updated description",
            "due_date": "2025-01-15",
            "priority_level": "Medium",
            "is_completed": true
        }
        ```

5. **Delete Task**
    - **POST** /api/delete_task/{id}/

        **Response:**
        ```json
        {
            "message": "Task deleted successfully."
        }
        ``` 

6. **Mark Task as Completed**
    - **POST** /api/mark_task/{id}/

        **Response:**
        ```json
            {
                "message": "Task completion status updated",
                "data": {
                    "id": 1,
                    "title": "Complete DRF authentication module",
                    "description": "Implement JWT authentication and user profile update endpoints for the task management API.",
                    "due_date": "2026-01-10T00:00:00Z",
                    "priority_level": "High",
                    "status": "Completed",
                    "creator": {
                        "id": 1,
                        "username": "eD",
                        "first_name": "",
                        "last_name": ""
                    },
                    "completed": true,
                    "completed_at": "2026-01-04T03:29:07.866618Z",
                    "created_at": "2026-01-03T17:22:02.193796Z",
                    "updated_at": "2026-01-04T03:29:07.867617Z"
                }
            }
        ```

## Technologies Used
- Django
- Django REST Framework
- SQLite (default database, can be changed)
- JWT Authentication
- Pillow (for image handling)

## Installation
1. Clone the repository:
   ```bash
   git clone

    cd task-management-api
    ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```  
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```








