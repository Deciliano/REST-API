import sqlite3
from model import Product

class ProductStorage:
    def __init__(self, db ='products.db'):
        self.db = db

    def connect_db(self):
        return sqlite3.connect(self.db)
    
    def create_table_products(self):
        with self.connect_db() as conneting:
            cursor = conneting.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           price INT NOT NULL
                )
            ''')
            conneting.commit()

    def all_products(self):
        with self.connect_db() as connecting:
            cursor = connecting.cursor()
            cursor.execute('SELECT * FROm products')
            products = cursor.fetchall()
        return [Product(id=row[0], name=row[1], price=row[2]) for row in products]
        
    def get_product(self, id):
        with self.connect_db() as connecting:
            cursor = connecting.cursor()
            cursor.execute('SELECT * FROM products WHERE id = ?', (id,))
            product = cursor.fetchone()
        if product:    
            return Product(id=product[0], name=product[1], price=product[2])
        else:
            return None
        
    def insert_product(self, new_product):
        with self.connect_db() as connecting:
            cursor = connecting.cursor()
            cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (new_product['name'], new_product['price']))
            connecting.commit()

    def update_product(self, id, updated_product):
        with self.connect_db() as connecting:
            cursor = connecting.cursor()
            cursor.execute('UPDATE products SET name = ?, price = ? WHERE id = ?', (updated_product['name'], updated_product['price'], id))
            connecting.commit()

    def delete_product(self, id):
        with self.connect_db() as connecting:
            cursor = connecting.cursor()
            cursor.execute('DELETE FROM products WHERE id = ?', (id,))
            connecting.commit()