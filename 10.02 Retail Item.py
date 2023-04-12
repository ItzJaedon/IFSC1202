class RetailItem:
    def __init__(self, description="", units_on_hand=0, price=0):
        self.description = description
        self.units_on_hand = units_on_hand
        self.price = price
    def inventory_value(self):
        return self.units_on_hand * self.price
items = []
with open('10.02 Inventory.txt', 'r') as f:
    for line in f:
        description, units_on_hand, price = line.strip().split(',')
        item = RetailItem(description, int(units_on_hand), float(price))
        items.append(item)
print("{:<20} {:<15} {:<15} {:<15}".format("Description", "Units on Hand", "Price", "Inventory Value"))
for item in items:
    print("{:<20} {:<15} {:<15} {:<15}".format(item.description, item.units_on_hand, item.price, item.inventory_value()))