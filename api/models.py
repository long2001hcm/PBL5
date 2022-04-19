from email.policy import default
from django.db import models

class User(models.Model):
    idUser = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

class Notify(models.Model):
    idNotify = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, null=False, on_delete=models.CASCADE, related_name='notify')
    Time = models.DateTimeField(auto_now_add=True)
    Text = models.TextField()
