# Kitchen-management

Kitchen Management is a Django web application designed to help restaurant
staff manage cooks, dishes, dish types, tables, and customer reservations.
The system provides authentication and role-based access, allowing staff to manage kitchen data and customers to create
and manage their own table reservations with selected dishes.

## Check it out!

[Kitchen management project deployed to Render](https://kitchen-management-tjs2.onrender.com/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
***
What things you need to install the software

```
Python 3.11 or higher
Git
```

### Installing
***
```shell
git clone https://github.com/gyxx1dd/kitchen-management.git
cd kitchen-management
python -m venv venv
.venv\Scripts\activate
pip install -r requirements.txt
Apply database migrations:
python manage.py migrate
Create a superuser to access the admin panel:
python manage.py createsuperuser
python manage.py runserver #starts Django Server
```

### Built With

***

* Django - Web framework

* SQLite - Database

* Bootstrap - Front-end framework

* django-crispy-forms - Form rendering

## Demo

![Website Interface](main.png)
<img width="1919" height="904" alt="image" src="https://github.com/user-attachments/assets/66171548-f569-4b1c-a39b-ef9336994e55" />
<img width="1919" height="910" alt="image" src="https://github.com/user-attachments/assets/d54cc95c-8664-43c6-b6fe-3a15ffcbcf4f" />
<img width="1919" height="906" alt="image" src="https://github.com/user-attachments/assets/e571077a-ce1e-4633-b11f-ef87f6c3939a" />
<img width="1919" height="906" alt="image" src="https://github.com/user-attachments/assets/1319646c-6373-4333-8a38-b4b08c11f6b8" />
<img width="1919" height="908" alt="image" src="https://github.com/user-attachments/assets/fc65936b-2871-4578-81b1-628a282fc0c7" />
