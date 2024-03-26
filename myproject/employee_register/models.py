from django.db import models

# Create your models here.



class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile= models.CharField(max_length=15)
    POSITION_CHOICES = [
        ('manager', 'Manager'),
        ('developer', 'Developer'),
        ('designer', 'Designer'),
    ]
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    
