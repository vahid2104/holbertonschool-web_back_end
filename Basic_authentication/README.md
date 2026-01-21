# Basic Authentication API

## Description
This project is part of the Holberton School Web Back-End curriculum.  
The goal of this project is to understand and implement **Basic Authentication**
on a simple REST API built with **Flask**.

The authentication system is implemented step by step for learning purposes.
In real-world applications, authentication frameworks or libraries should be used
instead of building a custom solution.

---

## Learning Objectives
By the end of this project, you should be able to explain:

- What authentication is
- What Basic Authentication is
- What Base64 encoding is
- How to send authorization headers
- How to protect API routes using authentication
- How to handle HTTP error codes (401, 403)

---

## Project Structure
Basic_authentication/
├── api/
│ └── v1/
│ ├── app.py
│ ├── views/
│ │ ├── index.py
│ │ └── users.py
│ └── auth/
│ ├── init.py
│ ├── auth.py
│ └── basic_auth.py
├── models/
│ └── user.py
├── requirements.txt
└── README.md

yaml
Copy code

---

## Authentication Flow
1. Requests are intercepted using Flask `before_request`
2. Public routes are excluded from authentication
3. For protected routes:
   - Missing `Authorization` header → **401 Unauthorized**
   - Invalid credentials → **403 Forbidden**
4. When credentials are valid, the request proceeds normally

---

## Error Handling
The API implements custom error handlers:

- **401 Unauthorized**
```json
{
  "error": "Unauthorized"
}
403 Forbidden

json
Copy code
{
  "error": "Forbidden"
}
Environment Variables
Variable	Description
API_HOST	API host (e.g. 0.0.0.0)
API_PORT	API port (e.g. 5000)
AUTH_TYPE	Authentication type (auth or basic_auth)

Running the API
bash
Copy code
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
Example Requests
Public endpoint
bash
Copy code
curl http://0.0.0.0:5000/api/v1/status
Protected endpoint (no auth)
bash
Copy code
curl http://0.0.0.0:5000/api/v1/users
Protected endpoint (Basic Auth)
bash
Copy code
curl http://0.0.0.0:5000/api/v1/users \
  -H "Authorization: Basic <base64(email:password)>"
Technologies Used
Python 3

Flask

Flask-CORS

Base64

pycodestyle

## Author
Vahid
Holberton School Student
