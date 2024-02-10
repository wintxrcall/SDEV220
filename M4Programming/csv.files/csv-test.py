import csv
import sqlite3 as sql3

from sqlalchemy import create_engine, Table, MetaData, select

# 16.2
with open('books.csv', 'r') as file1:
    csv_reader = csv.DictReader(file1)

    books = list(csv_reader)

for book in books:
    print(book)

# 16.4
# connect to SQLite database
connection = sql3.connect('books.db')
# create cursor object to execute SQL commands
cursor = connection.cursor()

# create books table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        title TEXT,
        author TEXT,
        year INTEGER
    )
''')

connection.commit()


print("Database and table created successfully")

# 16.5
with open('books2.csv', 'r') as file2:
    reader = csv.DictReader(file2)
    for row in reader:
        cursor.execute('INSERT INTO books VALUES (?, ?, ?)', (row['title'], row['author'], row['year']))
connection.commit()

# 16.6
cursor.execute('SELECT title FROM books ORDER BY title ASC')
for row in cursor.fetchall():
    print(row[0])

# 16.7
cursor.execute('SELECT * FROM books ORDER BY year ASC')
print(cursor.fetchall())

# 16.8
# create SQLite engine to connect to database
engine = create_engine('sqlite:///books.db')

# reflect existing database schema
metadata = MetaData()

books_table = Table('books', metadata, autoload_with=engine)

select_statement = select(books_table.columns.title).order_by(books_table.columns.title)
with engine.connect() as connection:
    results = connection.execute(select_statement).fetchall()

print("Titles in Alphabetical Order: ")
for row in results:
    print(row[0])

connection.close()
