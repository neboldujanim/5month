from django.contrib.auth.models import User
from django.db import models


class Code(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.IntegerField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.user.username
