class MySet:

    def __init__(self):
        self.items = set()

    def add_item(self, item):
        self.items.add(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    def item_count(self):
        return len(self.items)