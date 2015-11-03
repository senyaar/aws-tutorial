import uuid

from django.db import models


class PageView(models.Model):
    request_time = models.DateTimeField(auto_now=True)
