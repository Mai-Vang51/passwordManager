"""
User module that initialises a user's username and password.
"""


class User:
    def __init__(self, user_name, password):
        """Initialise user instance."""
        self.user_name = user_name
        self.password = password

    def __str__(self):
        """Return string representation of user_name and user password."""
        return f"{self.user_name} : {self.password}"
