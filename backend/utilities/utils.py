from django.core.exceptions import ValidationError

def validate_non_zero_oder(value):
    if value == 0:
        raise ValidationError("Zero values are not allowed within order fields.")