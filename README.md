# Django Project README

This Django project is a simple web application for managing food items and user registration. It consists of two main apps: `food` for managing food items and `users` for user authentication and profile management.

## Features

- **Food App**: Allows users to view, add, update, and delete food items.
- **Users App**: Provides user registration and authentication features, along with profile management.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project_directory>
    ```

3. Install dependencies:

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

6. Access the application at `http://127.0.0.1:8000/`.

## Usage

- **Food App**:
  - View all food items at the homepage (`/food`).
  - Add a new food item by clicking on the "Add Item" button.
  - Update or delete existing food items by clicking on the corresponding links.
  
- **Users App**:
  - Register a new account by visiting `/register`.
  - Login using registered credentials at `/login`.
  - Access the profile page at `/profile`.

## Structure

- `food/`: Contains the app for managing food items.
- `users/`: Contains the app for user registration and authentication.
- `pictures/`: Directory for storing user profile pictures.
- `profile_pictures/`: Directory for storing food item images.
- `manage.py`: Django management script.
- `mysite/`: Django project settings.



## Acknowledgments

- Thanks to Django for providing an excellent web framework.
- Inspiration from various online tutorials and documentation.