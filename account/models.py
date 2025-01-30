from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from account.managers import UserManager

# Create your models here.

class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name='First Name', max_length=100, unique=False)
    last_name = models.CharField(verbose_name='Last Name', max_length=100, unique=False)
    user_name = models.CharField(verbose_name='User Name', max_length=33, unique=True)
    email = models.EmailField(verbose_name='Email', max_length=200, unique=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_created=True, auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last Seen', auto_created=True, auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'user_name']

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def token(self):
        refresh=RefreshToken.for_user(self)
        return {
            'access':str(refresh.access_token)
        }

class UserProfile(models.Model):
    user_photo = models.ImageField(verbose_name='User Image', upload_to='users_photos', default='user.png', blank=True, null=True)
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}.photo'