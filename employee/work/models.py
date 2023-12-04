from django.db import models

# Create your models here.
class Employee(models.Model):
    uname=models.CharField(max_length=30)
    email=models.EmailField(null=True)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)
    def _str_(self):
        return self.uname

#python manage.py makemigrations(convert to query)
#python manage.py migrate(sqlite)
#django default db sqlite3

#object relational mapping is the query of django 
# ctrl Z=exit from shell
#first import model in shell
#variable=modelname.objects.all()
#then mention the variable


class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=30)
    email=models.EmailField(null=True)
    place=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    def _str_(self):
        return (self.name)
    def _str_(self):
        return (self.email)
    def _str_(self):
        return(self.place)


# Models : which is used to perform certain actions using data
# Eg : CRUD :Create,Read/Retrieve,Update,Delete

class Emp(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=30)
    salary=models.PositiveIntegerField()
    contact=models.CharField(max_length=20)

class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    publication_year=models.PositiveIntegerField()
    genre=models.CharField(max_length=30)
    def __str__(self):
        return (self.title)

    
class Details(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    course=models.CharField(max_length=20)
    def __str__(self):
        return (self.name)

class Mobiles(models.Model):
    name=models.CharField(max_length=20)
    price=models.PositiveIntegerField()

class Students(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    course=models.CharField(max_length=30)