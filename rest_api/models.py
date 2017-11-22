from django.db import models


class Bucketlist(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)