import sqlite3


class Query:

    def __init__(self):
        self.connection = sqlite3.connect("database", timeout=1)
        self.conn = self.connection.cursor()

        # Lista todos os livros em ordem alfabética.
    def query1(self):
        self.listar = self.conn.execute(
            "SELECT title FROM book ORDER BY title")
        print(self.listar.fetchall())

        # Busca livros pelo título.
    def query2(self):
        self.listar = self.conn.execute(
            "SELECT title FROM book WHERE title LIKE '%tronos%'")
        print(self.listar.fetchall())

        # Buscar livros pelo autor.
    def query3(self):
        self.listar = self.conn.execute(
            "SELECT author, title FROM book WHERE author LIKE '%George%'")
        print(self.listar.fetchall())

    # def query4(self):
    #     self.listar = self.conn.execute(
    #         "SELECT bwas_read, FROM bookshelf  INNER JOIN title t ON (b.id = t.id ) WHERE w.was_read = 1 GROUP BY w.was_read")
    #     print(self.listar.fetchall())


Query().query1()
Query().query2()
Query().query3()
# Query().query4()
