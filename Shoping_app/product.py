class Product:
    def __init__(self):
        self.products = []
    
    def add_product(self, item):
        self.products.append(item)
        print(f'Product added Successfully: {item.name}')
    
    def find_product(self, item_name):
        for item in self.products:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def remove_product(self, item):
        product = self.find_product(item.name)
        if product:
            self.products.remove(item)
            print(f'Product removed Successfully: {item.name}')
        else:
            print(f'Product not found: {item.name}')
    
    def show_products(self):
        if not self.products:
            print("No products available.")
        else:
            print("*****Products*****")
            print("Name\tPrice\tStock")
            for item in self.products:
                print(f"{item.name}\t{item.price}\t{item.stock}")