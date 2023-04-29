from django.db import models

class Student(models.Model):
    studentid = models.CharField(max_length=10, unique=True, default='')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
