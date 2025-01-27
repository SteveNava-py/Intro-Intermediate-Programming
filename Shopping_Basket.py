class ShoppingBasket:
    # Constructor
    def __init__(self):
        self.items = []  # A list of all the items in the shopping basket
        self.quantities = []  # A list of the quantities corresponding to each item found in the items list
        self.checkout = False

    # A method to find and return the index of an item in the items list
    def find_item(self, item):
        for i in range(0, len(self.items)):
            if self.items[i].name == item.name:
                return i
        return -1

    # A method to add an item to the shopping basket

    def add_item(self, item, quantity=1):
        if quantity > 0:
            # Check if the item is already in the shopping basket
            index = self.find_item(item)
            if index != -1:
                self.quantities[index] += quantity
            # Part of the Bulk logic
            elif quantity > 10:
                discount = item / 0.20
                self.items.append(discount)
                self.quantities.append(quantity)
            else:
                self.items.append(item)
                self.quantities.append(quantity)
        else:
            print("Invalid operation - Quantity must be a positive number!")

    # A method to remove an item from the shopping basket (or reduce its quantity)
    # e.g. removeItem(someItem) removes the item completely
    #      removeItem(someItem, 4) removes 4 pieces of the item

    def remove_item(self, item, quantity=0):
        index = self.find_item(item)
        if index != -1:
            if quantity <= 0:
                # Remove the item
                self.items.remove(item)
                del self.quantities[index]
            elif self.quantities[index] >= quantity:
                self.update_item(item, self.quantities[index]-quantity)

    # A method to update the quantity of an item from the shopping basket to the given value

    def update_item(self, item, quantity):
        index = self.find_item(item)
        if index != -1:
            if quantity > 0:
                self.quantities[index] = quantity
            else:
                self.remove_item(item)

    # A method to view/list the content of the basket.

    def view(self):
        total_cost = 0
        print("---------------------")
        for i in range(0, len(self.items)):
            item = self.items[i]
            quantity = self.quantities[i]
            if quantity < 10:
                cost = quantity * item.price
                print(f" + {item.name:20s} - {quantity:4d} x ${item.price:5.2f} = ${cost:6.2f}")
                print(f"   ({item.description})")
                total_cost += cost
            # The second part of the Bulk logic
            else:
                dis_price = item.price * 0.20
                cost = quantity * dis_price
                print(f" + {item.name:20s} - {quantity:4d} x ${item.price:5.2f} x discount of 20% = ${cost:6.2f}")
                print(f"   ({item.description})")
                total_cost += cost
        print("---------------------")
        print(f" = ${total_cost:7.2f}")
        print("---------------------")

    # A method to calculate the total cost of the basket.

    def get_total_cost(self):
        total_cost = 0
        for i in range(len(self.items)):
            item = self.items[i]
            quantity = self.quantities[i]
            if quantity < 10:
                cost = quantity * item.price
                total_cost += cost
            # Bulk logic problem 3
            else:
                dis_price = item.price * 0.20
                cost = quantity * dis_price
                total_cost += cost
        return total_cost

    def filter_by_category(self):
        category = str(input("What is the category of your item?: "))
        return Item(0,0,0, category)
    # A method to empty the content of the basket

    def reset(self):
        self.items = []
        self.quantities = []

    # A method to return whether the basket is empty or not:

    def is_empty(self):
        return len(self.items) == 0

    # A method for the checkout process
    def do_checkout(self):
        answer = int(input("Would you like to checkout? (press 1 for yes, 2 for no ): "))
        if answer == 1:
            print("Thank you for shopping with us")
            print(self.view())
            self.checkout = True
            self.is_empty()
            self.reset()
        elif answer == 2:
            print("Very well, let's continue")
        else:
            print("invalid response")


class Item:
    # Constructor
    def __init__(self, name, description, price, category):
        self.name = name
        self.description = description
        self.price = price
        self.category = category


myBasket = ShoppingBasket()


def display_menu():
    # Prompting user their options
    print("\nShopping Basket Menu")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Item Quantity")
    print("4. View Basket")
    print("5. Filter Items by Category")
    print("6. Checkout")
    print("7. Exit")
    response = int(input("Please dial a number for your next action: "))
    if response == 1:
        name = str(input("What item would you like to add?: "))
        description = str(input("What is the description of the item?: "))
        price = float(input("How much does the item cost?: "))
        category = str(input("What is the category of your item?: "))
        if name in list(myBasket.items):
            print("Item is already in your basket")
        else:
            item = Item(name, description, price, category)
            myBasket.add_item(item, 1)
            print(str(name) + " has been added ")
    elif response == 2:
        myBasket.view()
        name = str(input("What item would you like to remove?: "))
        amount = int(input("How much of the item would you like to remove?: "))
        if name in list(myBasket.items):
            option = int(input("Do you want to remove the entire item or an amount? dial 1 for item or 2 for amount: "))
            if option == 1:
                myBasket.items.remove(name)
                print("Item has been removed")
            elif option == 2 and amount <= int(list(myBasket.quantities)):
                myBasket.remove_item(, amount)
                print(str(name) + " has been removed")
            else:
                print("Invalid option or Invalid Amount")
        else:
            print("Item not found in basket")
    elif response == 3:
        name = str(input("What item's quantity do you wish to update?: "))
        if name in list(myBasket.items):
            num = int(input("How many of this item do you wish to add?: "))
            item = Item(name, 0, 0, 0)
            myBasket.update_item(item, num)
            print(str(name) + " has been updated")
        else:
            print("Item not found in basket")
    elif response == 4:
        return myBasket.view()
    elif response == 5:
        cat = str(input("Would you like to sort by name or amount?: "))
        if cat == "name" or "Name":
            name = str(input("What is the name of your product?:  "))
            if name in list(myBasket.items):
                print(name + " is in your basket")
        elif cat == "amount" or "Amount":
            amount = int(input("How much of the product do you have?: "))
            if amount in list(myBasket.quantities):
                print(str(amount) + " is in your basket")
        else:
            print("The item is not found in your basket")
    elif response == 6:
        return myBasket.do_checkout()
    elif response == 7:
        print("Thank you for shopping with us")
        quit(ShoppingBasket)
    else:
        print("Invalid Response")


# Calling User Interaction Function and looping it

print(display_menu())
a = 1
while a < 10:
    print(display_menu())
