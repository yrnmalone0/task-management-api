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








