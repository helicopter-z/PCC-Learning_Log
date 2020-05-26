# Web Applications

# Django (http://djangoproject.com/)
# - a web framework: a set of tolls designed to help you build interactive websites
# can respond to page requests and make it easier to read and write to a database, manage users, and much more

# Setting Up a Project
# spec: description of the project; specification
# - a full spec details the project goals, describes the project's functionality, and discusses its appearance and UI
# - should help you stay focused and on track

# The spec of this project can be:
# We’ll write a web app called Learning Log that allows users to log the topics they’re interested in and to make
# journal entries as they learn about each topic. The Learning Log home page should describe the site and invite users
# to either register or log in. Once logged in, a user should be able to create new topics, add new entries, and read
# and edit existing entries.

# To work with Django, we need to set up a virtual environment
# virtual environment: a place on your system where you can install and isolate packages from all other Python packages
# 1. cd to the folder where you want a virtual environment
# 2. python3 -m venv env_name
# 3. source env_name/bin/activate

# Starting a project:
# pip install Django
# django-admin.py startproject project_name .
# the dot. at the end creates the project with a directory structure that will make it easy to deploy the app to a server when we dinish developing it

# ls project_name
# __init__.py	asgi.py		settings.py	   urls.py		wsgi.py
# settings.py file controls how Django interacts with your system and manages your project
# urls.py file tells Django which pages to build in response to browser requests
# wsgi.py (web server gateway interface) file helps Django serve the files it creates

# http://127.0.0.1:8000/: the project is listening for requests on port 8000 on your computer
# localhost: a server that only processes requests on your system

# a Django project is organized as a group of individual apps

# superuser: a user who has all privileges available on on site
# privilege: controls the actions a user can take
# To create a superuser: python manage.py createsuperuser
# then go to http://local_host:8000/admin, enter admin's username/password

# Making pages with Django:
# - 3 steps: defining URLs -> writing views -> writing templates
# - each URL maps to a particular view - the view function retrieves and processes the data needed for that page
# the view function often calls a template, which builds a page for Learning Log

# base.html:
# <p>
# <a href="{% url 'learning_logs:index' %}">Learning Log</a>
# </p>
# {% block content %}{% endblock content %} -> template tag

# a link in HTML: <a href="link_url">link text</a>

# a loop in HTML:
# {% for item in list %}
#   do something with each item
# {% endfor %}

# any page that lets a user enter and submit information on a web page is a form
# when users enter information, we need to validate that the info provided is the right kind of data

# GET requests: for pages that only read data from the server
# POST requests: when the user needs to submit information through a form

# Django uses the template tag {% csrf_token %} to prevent attackers from using the form
# to gain unauthorized access to the server (this kind of attack is called a "cross-site request forgery")

# Django doesn't automatically generate a submit button for forms, so we have to define our own with:
# <button name="submit">button_text</button>



