from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} {self.is_completed}"


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username}{self.password}{self.email}"




