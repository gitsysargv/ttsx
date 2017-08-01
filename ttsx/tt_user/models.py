from django.db import models


class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    email = models.CharField(max_length=40)

    name = models.CharField(max_length=10, null=True, blank=True)
    addr = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        db_table = 'UserInfo'
