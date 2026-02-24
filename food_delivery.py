menu = {
    "chicken" : 2650,
    "pizza"     : 2000,
    "burger": 4300,
    "fries":100
}
class CustomerOrder:
    def __init__(self,name):
        self.name = name
        self.items = {}
    def add_item(self,item_name,quantity=1):
            if item_name in menu:
                if item_name in self.items:
                    self.items[item_name] += quantity
                else:
                    self.items[item_name] = quantity
                    print(f"{quantity} x {item_name} added to order")
            else:
                print(f"sorry {item_name} is not on the menu")

    def remove_item(self,item_name, quantity=1):
        if item_name in self.items:
            if self.items[item_name] > quantity:
                self.items[item_name] -= quantity
                print(f"{quantity} x {item_name}  remove order")
            else:
                del self.items[item_name]
                print(f"{item_name} item removed completely")
        else:
            print(f"{item_name} not found")

    def get_total(self):
        total = 0
        for item, qty in self.items.items():
            total +=menu[item]
        return total
    def show_order(self):
        if not self.items:
            print("order is empty. ")

        else:
            print(f"\n{self.name}'s order: ")
            for item, qty in self.items.items():
                print(f" -{item} x{qty} : {menu[item] * qty}")
            print(f"\nTotal: {self.get_total()}")
name = input("Enter your name: ")
order = CustomerOrder(name)

while True:
    print("\nMenu:")
    for item, price in menu.items():
        print(f" - {item}: {price}")

    choice = input("\nEnter an item to add (or 'done' to finish): ").lower()
    if choice == "done":
        break

    if choice in menu:
        qty = int(input(f"How many {choice}s would you like? "))
        order.add_item(choice, qty)
    else:
        print("That item is not on the menu.")

order.show_order()

