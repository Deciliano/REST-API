from storage import ProductStorage

class ProductService:
    def __init__(self):
        self.storage = ProductStorage()

    def get_all_products(self):
        return self.storage.all_products()
    
    def get_product(self, id):
        return self.storage.get_product(id)
    
    def add_product(self, new_product):
        return self.storage.insert_product(new_product)
    
    def update_product(self, id, update_product):
        return self.storage.update_product(id, update_product)
    
    def delete_product(self, id):
        return self.storage.delete_product(id)