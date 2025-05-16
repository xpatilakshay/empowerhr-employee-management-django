# 💼 EmpowerHR - Employee Management System

EmpowerHR is a web-based Employee Management System developed using the Django framework. Designed with modern HR needs in mind, EmpowerHR streamlines employee management through a clean, intuitive interface. It supports essential HR functionalities such as adding, updating, filtering, and removing employee records. The platform is fully responsive and includes user authentication, a contact form with email integration, and role-based access controls.

---

## 🌟 Key Features

- 🧑‍💼 Add, Update, View & Remove Employees
- 🔎 Filter Employees by Name, Department, Role, or Location
- 🔐 Secure User Authentication (Login/Register/Logout)
- ✉️ Contact Form with SMTP Email Integration
- 🖥️ Responsive Dashboard Interface with Bootstrap 5
- ⚙️ MySQL Database Integration
- 🔏 Role-Based Access with Django login_required
- 🧾 Form Validation & Real-Time Feedback

---

## 🛠️ Technology Stack

- Python 3.10+
- Django 5.2.1
- MySQL Database
- HTML5, CSS3, Bootstrap 5
- FontAwesome Icons
- JavaScript (via Bootstrap bundle)
- Gmail SMTP for email service

---

## 🗂️ Project Structure

```plaintext
empowerhr/
│
├── ems/                     # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── ems_app/                 # Core application logic
│   ├── migrations/
│   ├── templates/           # HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── add_emp.html
│   │   ├── view_all.html
│   │   ├── update_emp.html
│   │   ├── update_details.html
│   │   ├── remove_emp.html
│   │   ├── filter_emp.html
│   │   ├── login.html
│   │   └── register.html
│   ├           
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
└── requirements.txt
