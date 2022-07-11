from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model
    """

    username = models.CharField(max_length=64, unique=True,
                                verbose_name='User name')
    email = models.EmailField(unique=True, blank=False, null=False,
                              verbose_name='Email')
    is_support = models.BooleanField(default=False,
                                     verbose_name='Support employee')
