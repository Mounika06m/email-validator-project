class InvalidEmailError(Exception):
    """Custom exception for invalid email addresses."""
    def __init__(self, email, reason=""):
        self.email = email
        self.reason = reason
        super().__init__(f"Invalid email '{email}': {reason}")