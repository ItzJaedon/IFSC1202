class RetailItem:
    def __init__(self, description="", units_on_hand=0, price=0):
        self.description = description
        self.units_on_hand = units_on_hand
        self.price = price
    def inventory_value(self):
        return self.units_on_hand * self.price
def print_inventory(items):
    print(f"{'Description':<20} {'Units on Hand':<15} {'Price':<15} {'Inventory Value':<20}")
    for item in items:
        print(f"{item.description:<20} {item.units_on_hand:<15} {item.price:<15} {item.inventory_value():<20.2f}")
def find_inventory(items, description):
    for i, item in enumerate(items):
        if item.description == description:
            return i
    return -1
items = []
with open("11.01 Inventory.txt", "r") as f:
    for line in f:
        description, units_on_hand, price = line.strip().split(",")
        items.append(RetailItem(description, int(units_on_hand), float(price)))
print("Initial Inventory:")
print_inventory(items)
print()
with open("11.01 InventoryUpdate.txt", "r") as f:
    for line in f:
        description, price = line.strip().split(",")
        i = find_inventory(items, description)
        if i != -1:
            items[i].price = float(price)
print("Updated Inventory:")
print_inventory(items)