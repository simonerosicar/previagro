class ValidationError(Exception):
    """Raised when request payload validation fails."""

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class AuthenticationError(Exception):
    """Raised when JWT authentication fails."""

    def __init__(self, message):
        super().__init__(message)
        self.message = message
