# spotlight_Ideas
A project for creating and manipulating project ideas

Requirements:
1. Django
2. Django-social-auth

To install django-social-auth with pip, type the following in your terminal
pip install social-auth-app-django

To use the app, do the following:
1. cd into the working directory, inside <code> spotlight_Ideas </code>. The working directory contains <code>ideas/</code>, <code>spotlight/</code> and <code>manage.py</code>
2. Migrate the database by typing <code> python manage.py migrate </code> in your terminal from working directory.
3. Run development server by typing <code> python manage.py runserver localhost:8000</code> from your working directory.
4. Go to your browser and navigate to <code>localhost:8000/ideas</code>. Login window will open up.

Note: It is important that you run the project from port 8000, otherwise the github social login won't work.
