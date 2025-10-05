class Order:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.stock
        else:
            self.items[item] = item.stock

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item in self.items:
            del self.items[item]
            print(f'Item removed from cart Successfully: {item.name}')
        else:
            print(f'Item not found in cart: {item.name}')

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    
    def clear_cart(self):
        self.items = {}