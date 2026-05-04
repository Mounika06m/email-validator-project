import re
from exceptions import InvalidEmailError

def validate_email(email):
    """
    Validates the format of an email address.
    Raises InvalidEmailError if invalid.
    Returns True if valid.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not email:
        raise InvalidEmailError(email, "Email is empty")
    if not re.match(pattern, email):
        raise InvalidEmailError(email, "Format is incorrect")
    
    return True


def extract_details(email):
    """
    Extracts username and domain from a valid email.
    Returns a dict with 'username' and 'domain'.
    """
    validate_email(email)
    username, domain = email.split("@", 1)
    return {"username": username, "domain": domain}


def format_email(email, uppercase=False):
    """
    Formats email: lowercase by default, uppercase if flag is True.
    """
    validate_email(email)
    return email.upper() if uppercase else email.lower()