# First oka database create cheyyali and  daaniloki book title, author name, publication year,genre add cheyyali
# 1.values store chesukoovali
# 2.genre untadi ga adi marchali by using book tiltle and author name
# 3.updation of genre
# Using list show cheyyali

import sqlite3 as db

conn = db.connect('book.db')
c = conn.cursor()
c.execute('''
    create table if not exists book_details(
    isbn integer primary key,
    title text,
    author text,
    pub_year year,
    genre text)
''')
conn.commit()
# c.execute("INSERT INTO book_details VALUES (12456, 'Sample Book 1', 'Author 1', 2023, 'Fiction')")
# c.execute("INSERT INTO book_details VALUES (79012, 'Sample Book 2', 'Author 2', 2022, 'Mystery')")
# c.execute("INSERT INTO book_details VALUES (45678, 'Sample Book 3', 'Author 3', 2021, 'Science Fiction')")

c.execute("select name from sqlite_master where type='table'")
table_names = c.fetchall()
for table in table_names:
    print(table)
    table_name = table[0]
    c.execute("select * from " + table_name)
    rows = c.fetchall()
    for row in rows:
        print(row[4])

conn.commit()

# c.execute("select * from book_details")
# rows = c.fetchall()
# for row in rows:
#     print(row)
