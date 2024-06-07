#Q-01 Why Django should be used for web-development? Explain how you can create a project in Django?

'''
Django is a popular web development framework for building robust, scalable, and maintainable web applications.

Django comes with a wide range of built-in features and modules for common web development tasks..

Django follows best security practices. It provides built-in protection against common web vulnerabilities, including SQL injection, cross-site scripting (XSS), cross-site request forgery (CSRF), and clickjacking.

Django is designed to scale with the growth of a project. Its modular structure and flexibility allow developers to adapt the application architecture to changing requirements easily.

Create a project in Django :
Install Django:

pip install django
Create a Django Project:

django-admin startproject projectname
Navigate to the Project Directory:

cd projectname
Create a Django App:

python manage.py startapp appname
Configure Database: Update the DATABASES setting in the settings.py file to configure your database connection.

Run Migrations:

python manage.py migrate
Start the Development Server:

python manage.py runserver
This command starts the development server, and you can access your Django project at http://127.0.0.1:8000/ in your web browser.

These are the basic steps to set up a Django project. From here, you can define models, create views, set up URL patterns, and build out the functionality of your web application.

'''