# user-management-api
A simple Python FAST API based user management micro service
# User Management API

A FastAPI-based REST API for user management with PostgreSQL database integration.

## Features

- User registration and authentication
- JWT token-based authentication
- User profile management (create, read, update, delete)
- Role-based access control
- PostgreSQL database integration
- Secure password hashing
- Auto-generated API documentation

## Prerequisites

- Python 3.8+
- PostgreSQL

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/user-management-api.git
   cd user-management-api
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up PostgreSQL:
   - Create a database named `user_management`
   - Run database_set.sql under app/schema to create all the required database objects
   - Update `.env` file with your database credentials

## Configuration

Modify the `.env` file to configure your application:

```
# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=user_management
DB_USER=postgres
DB_PASSWORD=password

# JWT Configuration
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Running the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

- Interactive API documentation is available at http://localhost:8000/docs
- Alternative API documentation is available at http://localhost:8000/redoc

## API Endpoints

### Authentication
- `POST /api/v1/token` - Get authentication token

### Users
- `POST /api/v1/users` - Create a new user
- `GET /api/v1/users` - List all users (authenticated)
- `GET /api/v1/users/me` - Get current user details
- `GET /api/v1/users/{user_id}` - Get user by ID
- `PUT /api/v1/users/{user_id}` - Update user
- `DELETE /api/v1/users/{user_id}` - Delete user

## Default Superuser

On first run, the application creates a default superuser:
- Username: admin
- Password: adminpassword
- Email: admin@example.com
