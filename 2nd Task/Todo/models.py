from django.db import models
from django.contrib.auth.models import AbstractUser , Group ,Permission

class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])

class User1(AbstractUser):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')
    email = models.EmailField(unique=True,default='')
    username = models.CharField(max_length=150, unique=True, default='default_username')
    password = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.username

class Task(models.Model):
    task_text = models.CharField(max_length=200)
    task_status = models.CharField(max_length=20, choices=[
        ('incomplete', 'Incomplete'),
        ('delayed', 'Delayed'),
        ('in-progress', 'In Progress'),
        ('closed', 'Closed'),
    ])

    def __str__(self):
        return self.task_text