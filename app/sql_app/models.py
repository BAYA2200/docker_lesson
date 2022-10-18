from django.db import models

# Create your models here.
class Task (models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField()

    def __str__(self):
        return self.name

class Position(models.Model):
    position = models.CharField(max_length=30)
    department = models.CharField(max_length=30)


class Employee(models.Model):
    fio = models.CharField(max_length=50)
    birth_year = models.IntegerField()
    position = models.CharField(max_length=30)
    salary = models.CharField(max_length=50)
