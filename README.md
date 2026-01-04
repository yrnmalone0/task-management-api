# Task Management API
This is a Django-based Task Management API that allows users to register, manage their profiles, and handle tasks efficiently. The project includes custom user models, RESTful API endpoints, and media handling for profile pictures.

# Reflections
This project was an exciting opportunity to deepen my understanding of Django and Django REST Framework. Implementing a custom user model allowed me to explore the flexibility of Django's authentication system. I learned how to handle media files effectively, which is crucial for user profile management. The task management features provided a practical way to apply CRUD operations and filtering techniques in a real-world scenario. Overall, this project enhanced my skills in building robust APIs and managing user data securely.

# What you have accomplished so far?
- Set up a Django project with a custom user model.
- Created API endpoints for user registration and profile management.
- Implemented media handling for profile pictures.
- Developed task management features including creation, updating, deletion, and filtering of tasks.


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
1. *Register User*
    - *POST* /api/register_user/
      *Request Body:*
        ```json
        {
            "username": "johndoe",
            "password": "securepassword",
            "email": "johndoe@example.com",
            "bio": "A short bio",
            "profile_picture": "image_file"
        }
        ``` 

        *Response:*
        ```json
        {
            "id": 1,
            "username": "johndoe",
            "email": "johndoe@example.com",
            "bio": "A short bio",
            "profile_picture": "image_file"
        }
        ```

        *Response:*
        ```json
        {
            "id": 1,
            "username": "johndoe",
            "email": "johndoe@example.com",
            "bio": "A short bio",
            "profile_picture": "image_file"
        }
        ```         
2. *Update Profile* 
    - *PUT* /api/profile/
      *Request Body:*
        ```json
        {
            "bio": "Updated bio",
            "profile_picture": "new_image_file"
        }
        ```
      *Response:*
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
1. *Create Task*
    - *POST* /api/tasks/
      *Request Body:*
        ```json
        {
            "title": "New Task",
            "description": "Task description",
            "due_date": "2024-12-31",
            "priority_level": "High"
        }
        ```
      *Response:*
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
2. *List Tasks*
    - *GET* /api/tasks/
      *Response:*
        ```json
        [
            {
                "id": 1,
                "title": "New Task",
                "description": "Task description",
                "due_date": "2024-12-31",
                "priority_level": "High",
                "is_completed": false
            },
            ...
        ]
        ``` 
3. *Update Task*
    - *PUT* /api/tasks/{id}/
      *Request Body:*
        ```json
        {
            "title": "Updated Task",
            "description": "Updated description",
            "due_date": "2025-01-15",
            "priority_level": "Medium",
            "is_completed": true
        }
        ```
      *Response:*
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
4. *Delete Task*
    - *POST* /api/tasks/{id}/delete/
      *Response:*
        ```json
        {
            "detail": "Task deleted successfully."
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








