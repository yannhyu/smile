from datetime import datetime
from django.db import models
from django.conf import settings


class Comment(models.Model):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()
