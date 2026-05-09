# Smart Task Manager

A full-stack task management web application built using Flask, PostgreSQL, Pandas, NumPy, and Flask-SocketIO.

---

# Features

- User Registration & Login
- Password Hashing Authentication
- Task CRUD Operations
- PostgreSQL Database Integration
- Analytics Dashboard
- Real-Time Notifications using WebSockets
- Responsive Bootstrap UI

---

# Technologies Used

## Backend
- Flask
- Flask-SQLAlchemy
- Flask-SocketIO

## Database
- PostgreSQL

## Data Analytics
- Pandas
- NumPy

## Frontend
- HTML
- CSS
- Bootstrap
- JavaScript

---

# Project Structure

smart-task-manager/

├── app/

│   ├── models/

│   ├── routes/

│   ├── services/

│   ├── socket/

│   ├── static/

│   ├── templates/

│   ├── __init__.py

│   └── config.py

├── run.py

├── requirements.txt

└── README.md

---

# Installation

## Clone Repository

git clone <repository_url>

cd smart-task-manager

---

## Create Virtual Environment

python -m venv venv

---

## Activate Environment

### Windows

venv\Scripts\activate

---

## Install Dependencies

pip install -r requirements.txt

---

# PostgreSQL Setup

1. Install PostgreSQL
2. Create database:
   taskdb
3. Update config.py with PostgreSQL password

---

# Run Application

python run.py

---

# API Endpoints

## Authentication

POST /register

POST /login

---

## Tasks

GET /api/tasks

POST /api/tasks

PUT /api/tasks/<id>

DELETE /api/tasks/<id>

---

## Analytics

GET /api/analytics

---

# Real-Time Features

- Live task notifications using Flask-SocketIO
- Dashboard auto updates

---

# Future Improvements

- JWT Authentication
- Task Deadlines
- File Attachments
- Email Notifications
- Docker Deployment

---

# Author

UPPU KANNY