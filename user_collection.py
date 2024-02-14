"""
UserCollection class that stores user data in a list.
"""


class UserCollection:
    def __init__(self):
        self.users = []

    def __str__(self):
        return str(self.users)

    def add_user(self, user):
        self.users.append(user)
