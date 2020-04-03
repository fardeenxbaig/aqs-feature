from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    dob = models.DateField(_("date of birth"), null=True)
    mobile_no = models.CharField(_("mobile no"), max_length=20)

    REQUIRED_FIELDS = ['email', 'mobile_no']

    def __str__(self):
        return self.first_name