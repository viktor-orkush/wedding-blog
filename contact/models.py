from django.db import models


class Contact(models.Model):
    user = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=100, blank=False)
    message = models.CharField(max_length=256, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '"{user}"'.format(user=self.user)
