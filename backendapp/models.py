from django.db import models


class Subscriptions(models.Model):
    title = models.TextField(unique=True)
    detail = models.TextField()
    image = models.TextField(default='')
    price = models.TextField(default='500')

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.TextField()
    email = models.TextField()
    password = models.TextField()
    number = models.TextField()
    subs = models.TextField(default='')

    def __str__(self):
        return self.name
