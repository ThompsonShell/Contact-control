import re
from django.core.exceptions import ValidationError

def is_valid_phone_number(phone_number):
    pattern = r'^\+998\d{9}$'
    if not re.match(pattern, phone_number):
        raise ValidationError('The phone number is not in the correct format. Example: +998901234567')
    return True