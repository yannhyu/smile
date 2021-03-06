from datetime import datetime
from django.db import models
from django.conf import settings


class Comment(models.Model):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


class Launchpad(models.Model):
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def __str__(self):
        return self.name
