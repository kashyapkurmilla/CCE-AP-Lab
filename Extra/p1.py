import sqlite3 as db

conn = db.connect('mydata.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE if not exists users3 (
    id integer PRIMARY KEY ,
    USERNAME text ,
    EMAIL text) 
''')
conn.commit()

cursor.execute("INSERT INTO users3 VALUES (?,?,?)", (153, 'los', 'kashyapkurma@gmail.com'))
conn.commit()

# cursor.execute()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = cursor.fetchall()

for table in table_names:
    table_name = table[0]
    print(f"Table: {table_name}")

    # Query the table to retrieve its contents
    cursor.execute(f"SELECT * FROM {table_name};")

    # Fetch all rows in the table
    table_contents = cursor.fetchall()

    # Print the table contents
    for row in table_contents:
        print(row)


# cursor.execute("SELECT * FROM USERS2")
# for row in cursor.fetchall():
#     print(row)

print(conn)
print(table_names)