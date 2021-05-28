import sqlite3


class Query:
    def __init__(self):
        self.connection = sqlite3.connect("database", timeout=1)
        self.conn = self.connection.cursor()

    def query1(self):
        self.listar = self.conn.execute("SELECT title FROM book ORDER BY title")
        print(self.listar.fetchall())

    def query2(self):
        self.listar = self.conn.execute("SELECT title FROM book WHERE title = 'A guerra dos tronos'")
        print(self.listar.fetchall())

    def query3(self):
        self.listar = self.conn.execute("SELECT author, title FROM book WHERE author = 'George'")
        print(self.listar.fetchall())



    
        


Query().query1()
Query().query2()
Query().query3()
