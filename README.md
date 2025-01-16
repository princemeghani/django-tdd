# Django REST API Project

A Test-Driven Development (TDD) approach was followed to build this fully functional RESTful API using the Django Rest Framework (DRF). This project is designed to provide a robust and scalable backend solution for managing data, supporting CRUD operations, and enabling integration with frontend applications or other services. Automated tests ensure the reliability and correctness of the API, promoting maintainable and bug-free code.


## Requirements

Before running this project, ensure you have the following installed:

- **Python 3.8+**: The programming language used for development.
- **Django 3.2**: A powerful web framework for building the API.
- **Django REST Framework 3.12**: The toolkit for building Web APIs.
- **Other Dependencies**: Listed in `requirements.txt`.

## Setup Instructions

Follow these steps to set up the project locally:

### 1. Clone the Repository

Start by cloning the project repository to your local machine:

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 2. Create a Virtual Environment

Set up a virtual environment to isolate dependencies:

- On Linux/Mac:
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

- On Windows:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create an `.env` file by copying the sample configuration:

```bash
cp sample.env .env
```

Edit the `.env` file with your project-specific settings, such as database credentials and secret keys.

### 5. Apply Database Migrations

Set up the database by running migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the Development Server

Run the server locally:

```bash
python manage.py runserver
```

The API will be accessible at:

```
http://localhost:8000
```

### 7. Run Test Cases

Ensure all tests pass to verify the functionality of the API:

```bash
python manage.py test
```

## API Documentation

Interactive API documentation is available, allowing you to explore and test endpoints:

- **Swagger UI**: Visit `http://localhost:8000//api/docs#/` for an interactive API documentation interface.


## Features

- **RESTful API Endpoints**: Supports full CRUD operations.
- **Authentication**: Token-based authentication using Django Rest Framework.
- **Database Integration**: Configurable with PostgreSQL, SQLite, or other databases.
- **Modular Design**: Easily extensible for additional functionality.
- **Interactive Documentation**: Explore API endpoints with Swagger UI.

## Contribution Guidelines

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Make your changes and commit (`git commit -m 'Add a feature'`).
4. Push to your branch (`git push origin feature/YourFeatureName`).
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
