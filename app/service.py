from flask import abort
from app.storage import ProductStorage
import logging

class ProductService:
    def __init__(self):
        self.storage = ProductStorage()
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s -  %(message)s")

    def get_all_products(self):
        all_products = self.storage.all_products()
        if all_products:
            self.logger.info("All products")
            return all_products
        else:
            self.logger.warning("Products not found")
            abort(404, description='Products not found')
    
    def get_product(self, id):
        product = self.storage.get_product(id)
        if product:
            self.logger.info("Product with ID %s found", (id))
            return product
        else:
            self.logger.warning("Product with ID %s not found", (id))
            abort(404, description='Product not found.')
    
    def add_product(self, new_product):
        self.storage.create_table_products()
        insert_product = self.storage.insert_product(new_product)
        self.logger.info("Product create with success")
        return insert_product            
    
    def update_product(self, id, update_product):
        return self.storage.update_product(id, update_product)
    
    def delete_product(self, id):
        return self.storage.delete_product(id)