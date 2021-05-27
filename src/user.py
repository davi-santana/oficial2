import sqlite3


class User:
    def __init__(self):
        self.connection = sqlite3.connect("database", timeout=1)
        # self.cursor

    def user(self, user_id, name, email):
        self.connection.execute("INSERT INTO user VALUES ('{user_id}', '{name}', '{email}')".format(
            user_id=user_id, name=name, email=email))
        self.connection.commit()