# Django Blog App

A full-stack blog application built with Django, HTML/CSS, and JavaScript. Users can register, log in, create, update, delete, and read blog posts. Hosted on [PythonAnywhere](https://www.pythonanywhere.com).

## Live Demo
 [https://shridhar12.pythonanywhere.com/](https://shridhar12.pythonanywhere.com/)  


---

## Features

- User Registration and Authentication  
  Secure login, logout, and signup functionality.

- Create, Update, Delete Blog Posts  
  Authenticated users can manage their own blog entries with ease.

- List and View Blogs   
  View blogs by users.

- Clean UI with HTML, CSS, and JavaScript  
  Responsive design with interactive front-end experience.

- List and View Blogs
  View blogs posted by different users.

---

## Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript
- Database: SQLite 
- Deployment: PythonAnywhere

---

##  Project Structure

blog_app/ ├── blog_app/ │ ├── init.py │ ├── asgi.py │ ├── settings.py │ ├── urls.py │ └── wsgi.py ├── blog/ │ ├── admin.py │ ├── apps.py │ ├── models.py │ ├── serializers.py │ ├── tests.py │ ├── urls.py │ ├── views.py │ ├── static/ │ │ ├── script.js │ │ └── style.css │ ├── templates/ │ │ ├── base.html │ │ ├── blog_detail.html │ │ ├── create_blog.html │ │ ├── edit_blog.html │ │ ├── index.html │ │ ├── login.html │ │ ├── public_blogs.html │ │ └── signup.html │ └── migrations/ │ └── 0001_initial.py ├── db.sqlite3 └── manage.py

## Install dependencies
* pip install -r requirements.txt


## Run migrations and start server
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver
