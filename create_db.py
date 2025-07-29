import sqlite3

conn = sqlite3.connect('products.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        image TEXT
    )
''')

products = [
    ("T-shirt", 499, "https://via.placeholder.com/150"),
    ("Shoes", 1299, "https://via.placeholder.com/150"),
    ("Watch", 1999, "https://via.placeholder.com/150")
]
c.executemany("INSERT INTO products (name, price, image) VALUES (?, ?, ?)", products)

conn.commit()
conn.close()
print("Database created successfully!")
