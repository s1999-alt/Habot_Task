# Employee Management REST API

A secure and RESTful Employee Management API built using Django and Django REST Framework, implementing CRUD operations, JWT-based authentication, filtering, pagination, validation, and unit testing.

## 📌 Features

- **Token-based authentication** using JWT
- **Custom user model** (AbstractUser) with email-based login
- **Secure CRUD operations** for Employee management
- **Filtering** by department and role
- **Pagination** (10 employees per page)
- **Proper HTTP status codes** and error handling
- **Unit tests** for core endpoints
- **Clean, modular, and scalable** code structure

## 🛠️ Tech Stack

- **Python 3.x**
- **Django**
- **Django REST Framework**
- **Simple JWT**
- **SQLite** (default, easily replaceable)

## 📂 Project Structure

```text
Habot_Task/
│
├── backend/
│   ├── accounts/
│   │   ├── models.py        # Custom AbstractUser
│   │   ├── serializers.py   # Register serializer
│   │   ├── views.py         # Register & Login APIs
│   │   └── urls.py
│   │
│   ├── employees/
│   │   ├── models.py        # Employee model
│   │   ├── serializers.py   # Employee serializer
│   │   ├── views.py         # Employee CRUD APIs
│   │   ├── tests.py         # Unit tests
│   │   └── urls.py
│   │
│   ├── backend/             # Project Configuration
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── manage.py
│   └── db.sqlite3
│
├── venv/
└── README.md
```

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/s1999-alt/Habot_Task.git
cd Habot_Task
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
# Activate the virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

### 4️⃣ Apply Migrations

Navigate to the `backend` directory where `manage.py` is located:

```bash
cd backend
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the Server

```bash
python manage.py runserver
```

Server will start at: `http://127.0.0.1:8000/`

## 🔐 Authentication

### Register

**POST** `/api/auth/register/`

```json
{
  "username": "admin",
  "email": "admin@example.com",
  "password": "password123",
  "confirm_password": "password123"
}
```

### Login

**POST** `/api/auth/login/`

```json
{
  "email": "admin@example.com",
  "password": "password123"
}
```

**Response:**

```json
{
  "access": "<jwt-access-token>",
  "refresh": "<jwt-refresh-token>"
}
```

**Note:** Include the access token in headers for protected endpoints:

```http
Authorization: Bearer <access-token>
```

## 👨‍💼 Employee API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/api/employees/` | Create employee |
| **GET** | `/api/employees/` | List employees |
| **GET** | `/api/employees/{id}/` | Retrieve employee |
| **PUT** | `/api/employees/{id}/` | Update employee |
| **DELETE** | `/api/employees/{id}/` | Delete employee |

### 🧾 Employee Fields

| Field | Type | Required | Notes |
| :--- | :--- | :--- | :--- |
| `id` | Integer | Auto | Primary Key |
| `name` | String | Yes | |
| `email` | Email | Yes | Unique |
| `department` | String | No | |
| `role` | String | No | |
| `date_joined` | Date | Auto | |

## 🔍 Filtering & Pagination

### Filter by Department
```http
GET /api/employees/?department=Engineering
```

### Filter by Role
```http
GET /api/employees/?role=Developer
```

### Pagination
```http
GET /api/employees/?page=2
```
*Default: 10 records per page*

## ❗ Error Handling & Status Codes

| Scenario | Status Code |
| :--- | :--- |
| Successful creation | `201 Created` |
| Validation error | `400 Bad Request` |
| Unauthorized access | `401 Unauthorized` |
| Employee not found | `404 Not Found` |
| Successful deletion | `204 No Content` |

## 🧪 Running Tests

Run the unit tests using Django's test runner:

```bash
python manage.py test
```

**Tests include:**
- Authentication enforcement
- Employee CRUD operations
- Duplicate email validation
- Filtering logic
- Invalid ID handling

## 🔒 Security Notes

- All **Employee APIs** are protected using **JWT authentication**.
- Only **authenticated users** can access employee data.
- Passwords are **securely hashed** using Django’s built-in mechanisms.

## 🚀 Future Improvements

- [ ] Role-based access control (Admin/HR)
- [ ] API documentation using Swagger / OpenAPI
- [ ] Docker support
- [ ] Rate limiting