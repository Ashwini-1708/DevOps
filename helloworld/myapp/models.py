from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    
class Student3(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()


class Student1(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class Student2(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class Student3(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class Student4(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class Student5(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()




