from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.authentication.validators import CustomUsernameValidator, PhoneNumberValidator


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = CustomUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=20,
        unique=True,
        help_text=_(
            "Required. Use no more than 20 characters."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("Username is already taken."),
        },
    )
    name = models.CharField(
        max_length=60,
        unique=True,
        help_text=_(
            "Name of club, section or shanyrak."
        ),
    )
    phone_number = models.CharField(
        max_length=11,
        validators=[PhoneNumberValidator()],
    )
    email = models.EmailField(_("email"), blank=True)

    is_staff = models.BooleanField(
        _("staff status"),
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
