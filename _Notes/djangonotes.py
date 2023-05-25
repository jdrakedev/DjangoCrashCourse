# Django notes

# Tutorial by Code With Tomi on YT

# To start choose a directory for your django project, navigate to that directory via CMD

# In CMD:
# type the command
django-admin startproject project_name

# next cd into the folder that was just created
cd project_name

# next run the command
python manage.py startapp app_name

# Project can contain many apps that perform different functions

# The next step is to open up the project_name directory in a code editor
# in VsCode, open a new terminal, and type this command to run the project on a localhost 
python manage.py runserver
# this will bring you to a django generic splash page

# URL Routing
# to configure the home URL
# create a new file in the app_name directory called:
urls.py

# in urls.py add this boilerplate code
from django.urls import path
from . import views # from root import file view (like preload in godot)

# in views file, run the index function('whatever is being done there is going to be rendered to the user')
urlpatterns = [
    path('', views.index, name='index') # giving the url a name of index
]

# in views.py, add this import statement and create the index function
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>welcome to my site</h1>')

# in the project_name dir, add 'include' to this import statement
from django.urls import path, include

# then add this line to the urlpatterns list
path('', include('demoapp.urls'))

# if we refresh the local browser we have open, we will now the see custom message we wrote

#Templates and Static Files 

# in the root directory(folder that encapsulates the entire project), create a new folder called:
templates

# this folder will be home to all html files for this project
# inside of the templates dir, create a file called:
index.html

# in order for the project to get the path to our html files
# we open the settings.py file located in the project_name dir
# inside the TEMPLATES list, locate this line
'DIRS': [],
# and change it to:
'DIRS': [BASE_DIR/'templates'],

# now that we have some html, we can alter the index() function in the views.py file, like so:
def index(request):
    # render the request for index.html
    return render(request, 'index.html')

# create a new folder in the root dir called
static
# this is where we will put any external files for the project (css, images, javascript)

# inside the static folder, create a file called:
style.css

# to configure our static files (tell django where to look for them)
# go to the project_name dir and inside of settings.py, add this import statement
import os

# then scroll to the bottom of the file
# add this line after the line: STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# now then, to link our css to the html, we add this line at the top of our html file
{% load static %} # to import static

# and then this line
<link href="{% static 'style.css' %}" rel="stylesheet" /> # to link the html to css folder/file

# Form Submission In Django
# still inside of the index.html file, we add a basic form, like so:
<form>
    <input type="text" name="name"/>
    <input type="submit" />
</form>

# and in our app_name dir in views.py
# create a new function called name
def name(request):
    return render(request, 'name.html')
    
# then in the templates folder create another html file called 
name.html

# to link our index.html file to our name.html file we add this to the form
<form action="name", method="POST">
# and this line right under it (for securing the users data)
{% csrf_token %}

# back in the views file we alter our name function
def name(request):
    name = request.POST['name']
    return render(request, 'name.html', {'name': name})

# We add this to our name.html file
<h1>Your name is {{name}}</h1>

# Django Admin Panel
# django has a built-in admin panel that allows you to 
# maintain your site fron an admin interface

# to reach the admin panel, type "/admin" at the end of the url in your localhost project

# to get the details of the admin panel that is specific to your project (to create an admin user)
# we must first edit the settings.py file located in the project_name dir
# find the list called INSTALLED_APPS and add(install) the name of the app we created to it, like so:
'app_name'

# next in open a new terminal in VsCode and run the following command:
python manage.py migrate
# this will migrate all of our models into our database

# next we run a command to create admin credentials:
python manage.py createsuperuser
# you will be prompted to create an admin name, could be:
admin
# will also have to create an email adress for the admin user
admin@gmail.com
# and a password
bxxxxxxx

# we can return to our localhost project and add '/admin' to the end of the url
# type in the credentials that were just created and you should be taken to the admin panel
# in the admin panel, we can view all the users on our platform by clicking on the Users option

# Models In Django
# "models are equivalent to database"
# So, the options that you have the admin panel (Groups, Users) are models, and therefore part of a database
# and the names of those models(tables) are Groups and Users
# inside of the Users model(table) we have the values(columns):
username, email_address, first_name, last_name, and staff_status

# we can create our own models, to do so, navigate to models.py in the app_name dir
# creating a model is very similar to creating a table in SQL
# start with the code
class ModelName(models.Model):
    title = models.CharField(max_length=1000)
    owner = models.CharField(max_length=1000)
    price = models.IntegerField()

# anytime we make changes to the models.py file we must migrate them with the command
python manage.py makemigrations

# followed by the command
python manage.py migrate

# next we must register our models, to do so, navigate to admin.py in the app_name dir
# add the import statement
from .models import ModelName
# then add the line
admin.site.register(ModelName)

# Adding And Fetching Data From Models
# to add data to our model, we can do so in the admin panel
# go to the model you created and click the "Add ModelName" button (top right-hand corner)
# then fill out the values with required data
# once the data has been filled out hit the "Save" button (middle right-hand side)

# to fetch data from the database(model)
# navigate to the views.py flie in the project_name dir
# add this this import statement
from .models import ModelName
# in our index() function, add the line
mod_name = ModelName.objects.all()
# and we pass a new object into the "return render(request, 'index.html')" line, like so:
return render(request, 'index.html', {'mod_name': mod_name})

# we must now create some fields for the returned data in our index.html file
# to access the data in our list (the data stored to the variable mod_name)
# we use an html for loop, like so:
{% for i in mod_name %}
<p>{{ i.title }}</p>
{% endfor %}

# we can open our localhost project and refresh the browser, 
# upon doing so we will see a list of all the data in the "title" table appear on out project page.

# Tutorial by Code With Tomi on YT DONE ##############################################################################################




















