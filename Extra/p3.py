import sqlite3 as db

conn = db.connect('book.db')
c = conn.cursor()


def create_database():
    c.execute('''
        CREATE TABLE IF NOT EXISTS book_details (
        isbn INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        pub_year INTEGER,
        genre TEXT
        )
    ''')
    conn.commit()


def insert_values():
    tisbn = int(input("Enter ISBN : "))
    ttitle = input("Enter title of the book: ")
    tauthor = input("Enter author of the book: ")
    tyear = int(input("Enter year of publish: "))
    tgenre = input("Enter genre: ")

    c.execute("INSERT INTO book_details VALUES (?, ?, ?, ?, ?)", (tisbn, ttitle, tauthor, tyear, tgenre))
    conn.commit()
    print("Data inserted successfully!")


def update_genre():
    tisbn = int(input("Enter book isbn to change :"))
    tgenre = input("Enter new genre :")
    c.execute("update book_details set genre=? where isbn = ?", (tgenre, tisbn))
    conn.commit()
    print("Genre updated successfully!")


def display_values():
    c.execute("select name from sqlite_master where type='table'")
    table_names = c.fetchall()
    for table in table_names:
        table_name = table[0]
        c.execute("select * from " + table_name)
        rows = c.fetchall()
        for row in rows:
            print(row)


def main():
    create_database()

    while True:
        print("Menu:")
        print("1. Insert Book Details")
        print("2. Display Book Details")
        print("3. Update Book Details")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            insert_values()
        elif choice == '2':
            display_values()
        elif choice == '3':
            update_genre()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()


main()
