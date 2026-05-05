# 🏥 Hospital Management System

A web-based **Hospital Management System** built using **Django** that
helps manage and track:

-   👨‍⚕️ Doctors\
-   🧑‍🤝‍🧑 Patients\
-   📅 Appointments

This system streamlines hospital operations by organizing records and
maintaining appointment workflows efficiently.

------------------------------------------------------------------------

## 🚀 Features

-   Manage patient records\
-   Manage doctor information\
-   Schedule and track appointments\
-   Maintain appointment history\
-   Email notifications support

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Backend: Python, Django\
-   Database: PostgreSQL

------------------------------------------------------------------------

## ⚙️ Requirements

-   Python 3.x\
-   PostgreSQL\
-   pip

------------------------------------------------------------------------

## 📦 Setup Instructions

### 1. Clone the Repository

    git clone <your-repo-link>
    cd <your-project-folder>

------------------------------------------------------------------------

### 2. Create Virtual Environment

    python -m venv venv

Activate: - Windows: `venv\Scripts\activate` - Mac/Linux:
`source venv/bin/activate`

------------------------------------------------------------------------

### 3. Install Dependencies

    pip install django psycopg2-binary

------------------------------------------------------------------------

### 4. PostgreSQL Setup

Create a database and note: - Database Name\
- Username\
- Password

------------------------------------------------------------------------

### 5. Configure Database (settings.py)

``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

------------------------------------------------------------------------

### 6. Configure Email (settings.py)

``` python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
```

------------------------------------------------------------------------

### 7. Apply Migrations

    python manage.py makemigrations
    python manage.py migrate

------------------------------------------------------------------------

### 8. Run the Server

    python manage.py runserver

Open in browser:

    http://localhost:8000/

------------------------------------------------------------------------

## 📱 Application Info

-   App name: `hospital`\
-   Ensure it is added in `INSTALLED_APPS` in `settings.py`

------------------------------------------------------------------------

## ⚠️ Notes

-   Do not delete the `migrations` folder\
-   `__pycache__` can be ignored\
-   Use `.env` for better security in production

------------------------------------------------------------------------

## ⭐ Future Improvements

-   Authentication system\
-   Role-based access\
-   UI improvements\
-   Deployment support
