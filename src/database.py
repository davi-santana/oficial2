import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("database")

    def create_table(self):
        self.connection.execute("""CREATE TABLE IF NOT EXISTS user(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        );
        """)

        self.connection.execute("""CREATE TABLE IF NOT EXISTS book(
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publishing_company TEXT NOT NULL,
            publication_year VARCHAR (4)
        );
        """)

        self.connection.execute("""CREATE TABLE IF NOT EXISTS bookshelf(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            acquisition_year VARCHAR(4),
            was_read BOOL ,
            reading_date DATE,
            user_id INTEGER,
            book_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES user(user_id),
            FOREIGN KEY(book_id) REFERENCES book(user_id)
        );
        """)
        print("creatade!")

Database().create_table()