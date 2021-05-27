import sqlite3


class Book:
    def __init__(self):
        self.connection = sqlite3.connect("database", timeout=1)
        # self.cursor

    def book(self, book_id, title, author, publishing_company, publication_year):
        self.connection.execute("INSERT INTO book VALUES (NULL, '{user_id}', '{title}', '{author}', '{publishing_company}', '{publication_year}')".format(
            book_id=book_id,title=title, author=author, publishing_company=publishing_company, publication_year=publication_year))
        self.connection.commit()

        