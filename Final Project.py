class VendingItem:
    def __init__(self, name, initial_count, cost_per_item):
        self.Name = name
        self.InitialCount = initial_count
        self.CostPerItem = cost_per_item
        self.SoldCount = 0
        self.LostCount = 0
    def InitialValue(self):
        return self.InitialCount * self.CostPerItem
    def SoldValue(self):
        return self.SoldCount * self.CostPerItem
    def LostValue(self):
        return self.LostCount * self.CostPerItem
class Vending:
    def __init__(self):
        self.VendingList = []
        self.VendingTotalInitialValue = 0
        self.VendingTotalInitialCount = 0
        self.VendingTotalSoldValue = 0
        self.VendingTotalSoldCount = 0
        self.VendingTotalLostValue = 0
        self.VendingTotalLostCount = 0
    def load_vending_items_from_file(self, filename):
        with open(filename, "r") as f:
            for line in f:
                name, initial_count, cost_per_item = line.split()
                item = VendingItem(name, int(initial_count), float(cost_per_item))
                self.VendingTotalInitialValue += item.InitialValue()
                self.VendingTotalInitialCount += item.InitialCount
                self.VendingList.append(item)
    def print_vending(self):
        print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Name", "Initial Count", "Price Per Item", "Sold Count", "Sold Value", "Lost Count", "Lost Value"))
        for item in self.VendingList:
            print("{:<10} {:<15} ${:<14} {:<15} ${:<15} {:<15} ${:<15}".format(item.Name, item.InitialCount, item.CostPerItem, item.SoldCount, item.SoldValue(), item.LostCount, item.LostValue()))
        print("\n{:<26} ${:<14} {:<15} ${:<15} {:<15} ${:<15}".format("Total", self.VendingTotalInitialValue, self.VendingTotalInitialCount, self.VendingTotalSoldValue, self.VendingTotalLostCount, self.VendingTotalLostValue))
    def find_product(self, producttofind):
        for i, item in enumerate(self.VendingList):
            if item.Name == producttofind:
                return i
        return None
    def update_vending(self, productname):
        index = self.find_product(productname)
        if index is not None:
            item = self.VendingList[index]
            if item.SoldCount < item.InitialCount:
                item.SoldCount += 1
                self.VendingTotalSoldCount += 1
                self.VendingTotalSoldValue += item.CostPerItem
            else:
                item.LostCount += 1
                self.VendingTotalLostCount += 1
                self.VendingTotalLostValue += item.CostPerItem
vending_machine = Vending()
vending_machine.load_vending_items_from_file("Final Project Vending.txt")
with open("Final Project Sales.txt", "r") as f:
    for line in f:
        product = line.strip()
        vending_machine.update_vending(product)
vending_machine.print_vending()