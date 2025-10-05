from product import Product

class Shop:
    def __init__(self, name):
        self.name = name
        self.products = Product()
    
    def add_product(self, item):
        self.products.add_product(item)
    
    def remove_product(self, item):
        self.products.remove_product(item)
    
    def show_products(self):
        self.products.show_products()

    def find_product(self, item_name):
        return self.products.find_product(item_name)