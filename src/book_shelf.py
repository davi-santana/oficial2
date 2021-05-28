import sqlite3

class Book_Shelf:
    def __init__(self):
        self.connection = sqlite3.connect("database", timeout=1)
        # self.cursor

    def book_shelf(self, id,user_id, book_id, acquisition_year, was_read, reading_date):
        self.connection.execute("INSERT INTO bookshelf VALUES ('{id}','{user_id}', '{book_id}', '{acquisition_year}','{was_read}','{reading_date}')".format(
            id=id, user_id=user_id, book_id=book_id, acquisition_year=acquisition_year,was_read=was_read,reading_date=reading_date))
        self.connection.commit()