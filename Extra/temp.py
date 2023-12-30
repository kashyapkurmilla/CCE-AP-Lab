import sqlite3 as db

class BookDatabase:
    def __init__(self, database_name):
        self.conn = db.connect(database_name)
        self.c = self.conn.cursor()

    def create_database(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS book_details (
                isbn INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                pub_year INTEGER,
                genre TEXT
            )
        ''')
        self.conn.commit()

    def insert_values(self):
        tisbn = int(input("Enter ISBN: "))
        ttitle = input("Enter title of the book: ")
        tauthor = input("Enter author of the book: ")
        tyear = int(input("Enter year of publish: "))
        tgenre = input("Enter genre: ")

        self.c.execute("INSERT INTO book_details VALUES (?, ?, ?, ?, ?)", (tisbn, ttitle, tauthor, tyear, tgenre))
        self.conn.commit()
        print("Data inserted successfully!")

    def update_genre(self):
        tisbn = int(input("Enter book ISBN to change: "))
        tgenre = input("Enter new genre: ")

        self.c.execute("UPDATE book_details SET genre=? WHERE isbn = ?", (tgenre, tisbn))
        self.conn.commit()
        print("Genre updated successfully!")

    def display_values(self):
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table'")
        table_names = self.c.fetchall()
        for table in table_names:
            table_name = table[0]
            self.c.execute("SELECT * FROM " + table_name)
            rows = self.c.fetchall()
            for row in rows:
                print(row)

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    book_db = BookDatabase('book.db')

    # Call methods directly as needed
    book_db.create_database()
    book_db.insert_values()
    book_db.display_values()
    book_db.update_genre()

    book_db.close()
