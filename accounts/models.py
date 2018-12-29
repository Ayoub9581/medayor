from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.conf import settings
from django.core.validators import RegexValidator
# Create your models here.

USERNAME_REGEX = '^[a-zA-Z0-9.@+-]*$'



class MyUserManager(BaseUserManager):
    def create_user(self,username, email, password=None):
        if not email:
            raise ValueError('user must have an email')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username,email,password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self.db)
        return user


class MyUser(AbstractBaseUser):
    email       = models.EmailField(verbose_name="Email", max_length=255)
    username    = models.CharField(max_length=255, validators=[RegexValidator(
                    regex = USERNAME_REGEX,
                    message='Username must be alphanumeric',
                    code='invalude Username'
                    )] , unique=True)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the suer have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
        
