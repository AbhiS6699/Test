from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Add this related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Add this related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
