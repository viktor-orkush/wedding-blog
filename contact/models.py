from django.db import models
from django.utils.datetime_safe import datetime


class Contact(models.Model):
    user = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=100, blank=False)
    # event_date = models.DateField(blank=True)
    message = models.CharField(max_length=256, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '"{user}"'.format(user=self.user)
