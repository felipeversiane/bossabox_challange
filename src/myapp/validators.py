import datetime
from django.core.exceptions import ValidationError
import re


def validate_first_letter(str):    
    if str[0].isdigit():        
        raise ValidationError("First letter cannot be a number.")

def validate_letters(name):    
    if not re.match(r'^[A-Za-z ]+$', name):      
        raise ValidationError("Only letters and spaces allowed.")

def validate_value(value):
    if value <= 0:
        raise ValidationError("Value must be positive.")
        