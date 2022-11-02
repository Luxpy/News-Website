from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class CustomUsernameValidator(RegexValidator):
    regex = r"^([A-Za-z0-9\-\_]+)$"
    message = _(
        "Username must contain only letters, digits, underscores, dashes."
    )


class PhoneNumberValidator(RegexValidator):
    regex = r"^\?77(\d{9})$"
    message = _(
        "Phone number must be: +7 (7xx) xxx xx-xx."
    )
