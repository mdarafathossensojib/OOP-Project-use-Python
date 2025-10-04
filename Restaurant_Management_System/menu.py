class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f'Item added Successfully: {item.name}')

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f'Item remove Successfully: {item.name}')
        else:
            print(f'Item not found: {item_name}')

    def show_menu(self):
        if not self.items:
            print("Menu is Empty.")
        else:
            print("*****Menu*****")
            print("Item\tPrice\tQuantity")
            for item in self.items:
                print(f"{item.name}\t{item.price}\t{item.quantity}")
