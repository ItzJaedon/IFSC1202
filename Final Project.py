class VendingMachine:
    def __init__(self, filename):
        self.products = []
        self.prices = {}
        self.inventory = {}
        self.VendingTotalInitialValue = 0
        self.VendingTotalInitialCount = 0
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                product_name = data[0]
                price = float(data[1])
                quantity = int(data[2])
                self.add_product(product_name, price, quantity)
    def add_product(self, product_name, price, quantity):
        self.products.append(product_name)
        self.prices[product_name] = price
        self.inventory[product_name] = quantity
    def buy_product(self, product_name):
        if product_name not in self.products:
            print(f"Error: {product_name} not found in vending machine")
            return
        if self.inventory[product_name] == 0:
            print(f"Error: {product_name} is out of stock")
            return
        self.inventory[product_name] -= 1
        self.VendingTotalInitialValue += self.prices[product_name]
        self.VendingTotalInitialCount += 1
        print(f"Thank you for buying {product_name} for ${self.prices[product_name]:.2f}. "
              f"There are {self.inventory[product_name]} {product_name}(s) left.")
    def print_vending(self):
        print(f"{'Product':<12} {'Price':<8} {'Quantity':<10}")
        for product_name in self.products:
            print(f"{product_name:<12} ${self.prices[product_name]:.2f} {self.inventory[product_name]:<10}")
        print(f"{'Total':<8} {self.VendingTotalInitialCount:<11} ${'' if self.VendingTotalInitialValue == 0 else self.VendingTotalInitialValue:.2f}")
vending_machine = VendingMachine('Final Project Vending.txt')
vending_machine.print_vending()
vending_machine.buy_product('Coke')
vending_machine.print_vending()