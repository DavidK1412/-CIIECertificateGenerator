from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
import uuid


class UserManager(BaseUserManager):
    # Create a user with email and password

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        # Create a superuser with email and password
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField('email', max_length=100, unique=True)
    password = models.CharField('password', max_length=256)
    name = models.CharField('name', max_length=200)
    can_create_users = models.BooleanField(default=False)

    def save(self, **kwargs):
        some_salt = 'V2lzaCBvbiBhbiBFeWVsYXNo'
        self.password = make_password(self.password, some_salt)
        super().save()

    objects = UserManager()
    USERNAME_FIELD = 'email'
