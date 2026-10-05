# FastAPI User API with JWT Authentication

A secure User Management REST API built using **FastAPI, MySQL, SQLAlchemy, Alembic, JWT Authentication, and Role-Based Access Control (RBAC)**.

This project extends a basic CRUD API by adding user authentication, password hashing, JWT-based authorization, protected routes, and role-based access control.

---

## 🚀 Features

- User registration
- User login
- Secure password hashing using bcrypt
- JWT-based authentication
- Protected API endpoints
- User profile endpoint
- Role-based access control
- Admin-only endpoints
- MySQL database integration
- SQLAlchemy ORM
- Alembic database migrations
- Pydantic request and response validation
- Environment variable configuration
- Interactive Swagger API documentation
- Simple HTML/CSS/JavaScript frontend

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend API framework |
| Uvicorn | ASGI server |
| MySQL | Relational database |
| SQLAlchemy | ORM and database operations |
| Alembic | Database migrations |
| Pydantic | Data validation |
| PyMySQL | MySQL database driver |
| JWT | Authentication and authorization |
| python-jose | JWT token creation and verification |
| Passlib | Password hashing |
| bcrypt | Secure password hashing algorithm |
| python-dotenv | Environment variable management |
| HTML/CSS/JavaScript | Frontend |

---

## 📁 Project Structure

```text
user-api-jwt/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── .gitignore
├── alembic.ini
├── auth.py
├── database.py
├── main.py
├── models.py
├── schemas.py
└── README.md

🔐 Authentication Flow

This project uses JWT (JSON Web Token) for authentication.

The authentication process works as follows:

User
 │
 ├── Register
 │      │
 │      └── Password is hashed
 │             │
 │             └── Stored in MySQL
 │
 ├── Login
 │      │
 │      └── Credentials verified
 │             │
 │             └── JWT token generated
 │
 └── Access Protected Route
        │
        └── JWT token sent in Authorization header
               │
               ├── Token valid → Access granted
               │
               └── Token invalid/missing → Access denied

🔒 Security

This project implements several security mechanisms.

Password Hashing

Passwords are hashed using bcrypt before being stored in MySQL.

JWT Authentication

JWT tokens are used to authenticate users when accessing protected routes.

Token Expiration

JWT tokens have a configured expiration time.

Role-Based Authorization

Admin-only routes verify the user's role before allowing access.

Environment Variables

Sensitive information such as:

MySQL password
JWT secret

is stored in .env rather than directly in the source code.

🧪 Validation and Error Handling

The API validates incoming data using Pydantic.

Examples of handled errors include:

Invalid email
Missing required fields
Duplicate email registration
Invalid login credentials
Missing authentication token
Invalid or expired JWT token
Unauthorized access
Insufficient permissions

🖥️ Frontend

A simple frontend is included using:

HTML
CSS
JavaScript

The frontend communicates with the FastAPI backend and allows users to interact with authentication and profile functionality.

📖 What I Learned

Through this project, I learned:

Building REST APIs using FastAPI
User registration and login
Password hashing with bcrypt
JWT authentication
JWT token verification
Protected API routes
Role-Based Access Control
HTTP authentication headers
SQLAlchemy ORM
MySQL database integration
Alembic database migrations
Pydantic validation
Environment variable management
API testing using Swagger UI
Connecting a frontend with a backend API
🔮 Future Improvements

Possible future improvements include:

Refresh tokens
Password reset functionality
Email verification
User profile editing
More granular permissions
Redis-based token/session management
Automated tests using Pytest
Docker containerization
API deployment
👩‍💻 Author

Harshini S

B.Tech Information Technology
