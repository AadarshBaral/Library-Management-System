# Library Management System

### About:
This is a simple library management system build with Django. This app is totally based
up on django's admin panel. With this app, You cand Add books in the system and Issue books to a person 
A person has the ability to take only 1 book at a time and after he returns the book, it gets updated in the system and various actions can be performed with various
amount of data the user has provided.

## Installing the Application
- Make sure you have python installed
- Create a virtual environment using `python -m venv env_name` and activate
- install all the requirements using  `pip install -r requirements.txt`
- Clone the Application
- Run using `python manage.py runserver`


## Things I learned with this Application
- Database relationships
- Using Signals On Django Application
Django Signals allow you to perform something when something is done within a system
For example if a User is registering on an application, we can use signal to basically create the profile model as soon as the User model is saved. It offers various actions like pre_save() and post_save() which basically mean before saving the model instance and after saving the model instance

More about django signals [Here](https://www.pluralsight.com/guides/introduction-to-django-signals)

- Showing fields of one model in another model as a readonly method
Create a function in one model which instanciates the other model and return it as a property\variable
Then go to admin.py file and do this on the desired table

```
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ["method_you_created"]

```
