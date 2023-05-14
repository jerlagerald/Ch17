import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')
# 1.Select all authors’ last names from the authors table in descending order.
print("1. All authors’ last names from the authors table in descending order.")
print(pd.read_sql('SELECT last FROM authors order by last DESC', connection))

# 2.Select all book titles from the titles table in ascending order.
print("\n2. All book titles from the titles table in ascending order")
print(pd.read_sql("select title from titles order by title ASC", connection))

# 3.Use an INNER JOIN to select all the books for a specific author.
#Include the title, copyright year and ISBN. Order the information alphabetically by title.
print("3. Use an INNER JOIN to select all the books for a specific author(Deitel).\n"
      " Include the title, copyright year and ISBN. Order the information alphabetically by title.")
print(pd.read_sql("""select title,copyright,titles.isbn from titles inner join author_ISBN on titles.isbn = author_ISBN.isbn inner join authors on author_ISBN.id = authors.id 
            where authors.last= 'Deitel' order by title ASC""", connection).head())

# 4.Insert a new author into the authors table.
print("\n4. Insert a new Author")
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Tony', 'Evans')""")
print(pd.read_sql("select id,first, last from authors",connection, index_col = ['id']))

# 5.Insert a new title for an author.
#Remember that the book must have an entry in the author_ISBN table and an entry in the titles table.
cursor= cursor.execute("""insert into titles(isbn,title,edition,copyright) 
                        values('0134444329',"Introduction to Python Programming",4,'2016')""")

print("AFTER INSERTION")
print(pd.read_sql("select * from titles", connection))

connection.close()