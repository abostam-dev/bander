from django.db import models
from django.contrib.auth.models import AbstractUser

# نموذج مستخدم مخصص
class Account(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="رقم الجوال")
    address = models.TextField(blank=True, null=True, verbose_name="العنوان")

    class Meta:
        verbose_name = "مستخدم"
        verbose_name_plural = "المستخدمون"

    def __str__(self):
        return self.username
