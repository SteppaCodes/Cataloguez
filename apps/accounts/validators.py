from django.forms import ValidationError
from django.core.validators import RegexValidator

def validate_name(value):
    # check if theres space in the name provided
    if len(value.split()) > 1:
        raise ValidationError("No space between names")
    # check if the user has alphanumeric characters in the name provided
    elif not value.isalpha():
        raise ValidationError("Name can contain only alphabets")
    return value 

alternate_validate_name = RegexValidator(
    regex=r"^[a-zA-Z]*$", message="No spaces between names"
)