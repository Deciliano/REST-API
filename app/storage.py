import sqlite3
import logging
from app.model import Product

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s -  %(message)s")

class ProductStorage:
    
    def __init__(self, db ='products.db'):
        self.db = db

    def connect_db(self):
        return sqlite3.connect(self.db)
    
    def create_table_products(self):
        with self.connect_db() as connecting:
            cursor = connecting.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           price INT NOT NULL
                )
            ''')
            connecting.commit()

    def all_products(self):
        try:
            with self.connect_db() as connecting:
                cursor = connecting.cursor()
                cursor.execute("SELECT * FROM sqlite_master WHERE type='table' AND name='products'")
                table_exists = cursor.fetchone()
                if not table_exists:
                    logger.warning("The table 'products' not exists")
                    return []
                cursor.execute("SELECT * FROM products")
                products = cursor.fetchall()
            return [Product(id=row[0], name=row[1], price=row[2]) for row in products]
        except sqlite3.Error as e:
            logger.error("Error to try access the database", e)
            return []
        
    def get_product(self, id):
        with self.connect_db() as connecting:
            cursor = connecting.cursor()
            cursor.execute("SELECT * FROM products WHERE id = ?", (id,))
            product = cursor.fetchone()
        if product:    
            return Product(id=product[0], name=product[1], price=product[2])
        else:
            return None
        
    def insert_product(self, new_product):
        with self.connect_db() as connecting:
            cursor = connecting.cursor()
            cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (new_product['name'], new_product['price']))
            connecting.commit()

    def update_product(self, id, updated_product):
        with self.connect_db() as connecting:
            cursor = connecting.cursor()
            cursor.execute("UPDATE products SET name = ?, price = ? WHERE id = ?", (updated_product['name'], updated_product['price'], id))
            connecting.commit()

    def delete_product(self, id):
        with self.connect_db() as connecting:
            cursor = connecting.cursor()
            cursor.execute("DELETE FROM products WHERE id = ?", (id,))
            connecting.commit()