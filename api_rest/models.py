# api_rest/models.py
from django.db import models

class User(models.Model):
    user_nickname = models.CharField(max_length=30, primary_key=True, unique=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)
    user_age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_nickname