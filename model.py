class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = round(price, 2)

    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }