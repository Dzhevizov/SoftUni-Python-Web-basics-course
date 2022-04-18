import re

from django.core.exceptions import ValidationError

REGEX_VALIDATION_MESSAGE = 'Ensure this value contains only letters, numbers, and underscore.'
REGEX_USERNAME = "^[A-Za-z0-9_]*$"


def regex_validator(value):
    regex = REGEX_USERNAME
    if not re.match(regex, value):
        raise ValidationError(REGEX_VALIDATION_MESSAGE)
