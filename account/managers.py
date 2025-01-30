from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('Please enter a valid email address'))

    def create_user(self, first_name, last_name, user_name, email, password, **extra_fields):
        if not first_name:
            raise ValueError(_('Please enter your first name'))

        if not last_name:
            raise ValueError(_('Please enter your last name'))

        if not user_name:
            raise ValueError(_('Please enter your user name'))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('Please enter a your email address'))

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
            email=email,
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self.db)

        return user

    def create_superuser(self, first_name, last_name, user_name, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)

        if not password:
            raise ValueError(_('password required'))

        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
            email=email,
            password=password,
            **extra_fields
        )

        user.save(using=self.db)

        return user