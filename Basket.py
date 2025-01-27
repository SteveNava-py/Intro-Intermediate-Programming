class ShoppingBasket:
    # Constructor
    def __init__(self):
        self.items = []  # A list of all the items in the shopping basket
        self.quantities = []  # A list of the quantities corresponding to each item found in the items list
        self.checkout = False  # This attribute can be used in the checkout process

        # A method to find and return the index of an item in the items list
    def find_item(self, item):
        for i in range(0, len(self.items)):
            if self.items[i].name == item.name:
                return i
        return -1

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
    # This method is modified to reflect the change in the quantity and update the discount accordingly
    def update_item(self, item, quantity):
        index = self.find_item(item)
        if index != -1:
            if quantity > 0:
                self.quantities[index] = quantity
                # Apply bulk purchase discount if necessary
                if quantity >= 10:  # Assuming bulk purchase threshold is 10
                    item.set_discount(0.1)  # Apply 10% discount
                else:
                    item.set_discount(0)  # Remove discount if quantity falls below threshold
            else:
                self.remove_item(item)

    # Modify this method to include discount calculation
    def view(self):
        total_cost = 0
        print("---------------------")
        for i in range(0, len(self.items)):
            item = self.items[i]
            quantity = self.quantities[i]
            # Add logic here to calculate cost considering any discounts
            cost = quantity * item.price
            print(f" + {item.name:20s} - {quantity:4d} x ${item.price:5.2f} = ${cost:6.2f}")
            print(f"   ({item.description})")
            total_cost += cost
        print("---------------------")
        print(f" = ${total_cost:7.2f}")
        print("---------------------")

    # Modified method to include discount calculation
    def get_total_cost(self):
        total_cost = 0
        for i in range(0, len(self.items)):
            item = self.items[i]
            quantity = self.quantities[i]
            cost = quantity * item.get_discounted_price()
            total_cost += cost
        return total_cost

    # Modify the addItem method to handle bulk purchase discounts
    def add_item(self, item, quantity=1):
        if quantity > 0:
            index = self.find_item(item)
            if index != -1:
                self.quantities[index] += quantity
            else:
                self.items.append(item)
                self.quantities.append(quantity)
            # Apply bulk purchase discount
            # check if the items are greater than 10, use set_discount(0.1) for this item
        else:
            print("Invalid operation - Quantity must be a positive number!")

    # method to filter items by their category

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

    # A method to filter what is in the basket of the user by the category attribute
    # I went to office hours with Jonathan and had significant help from him and others there to make this function

    def filter_by_category(self, category):
        filtered_list = []
        for item in self.items:
            if item.category.lower() == category.lower():
                filtered_list.append(f"{item.name} + {item.description} + {item.price}")
            else:
                print("Invalid category")
        if len(filtered_list) > 0:
            print(" Items in your basket of this category are: " + list(filtered_list))
        else:
            print("Invalid amount or Invalid category provided")

    # A method to empty the content of the basket

    def reset(self):
        self.items = []
        self.quantities = []

    # A method to return whether the basket is empty or not:

    def is_empty(self):
        return len(self.items) == 0


# updated and ready for you
class Item:
    # Modified constructor to include category and discount
    def __init__(self, name, description, price, category):
        self.name = name
        self.description = description
        self.price = price
        self.discount = 0
        self.category = category

    # Method to set discount
    def set_discount(self, discount):
        self.discount = discount

    # Method to calculate price after discount
    def get_discounted_price(self):
        return self.price * (1 - self.discount)


# Function to display the menu
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


# List of items available for shopping
tomatoSoup = Item("Tomato Soup", "200mL can", 0.70, "Food")
spaghetti = Item("Spaghetti", "500g pack", 1.10, "Food")
blackOlives = Item("Black Olives Jar", "200g Jar", 2.10, "Food")
mozzarella = Item("Mozzarella", "100g", 1.50, "Dairy")
gratedCheese = Item("Grated Cheese", "100g", 2.20, "Dairy")
greenTea = Item("Green Tea", "100g pack", 3.50, "Beverage")
chocolateBar = Item("Chocolate Bar", "50g bar", 0.99, "Snack")
oliveOil = Item("Olive Oil", "500ml bottle", 5.49, "Food")
cereal = Item("Cereal", "500g box", 2.99, "Food")
almondMilk = Item("Almond Milk", "1L carton", 1.89, "Dairy")

# Creating a list of all available items
available_items = [tomatoSoup, spaghetti, blackOlives, mozzarella, gratedCheese,
                   greenTea, chocolateBar, oliveOil, cereal, almondMilk]

unique_categories = []
for item in available_items:
    if item.category not in unique_categories:
        unique_categories.append(item.category)

# Function to display available items
def display_available_items():
    print("\nAvailable Items:")
    for item in available_items:
        print(f"{item.name} - {item.description} - ${item.price}")


# Main Program Loop
myBasket = ShoppingBasket()

while True:
    display_menu()
    response = input("Enter your choice (1-7): ")

    if response == "1":
        display_available_items()  # Show available items to add
        item_name = input("Enter the name of the item to add: ")
        quantity = int(input("Enter the quantity: "))
        # Find the item object by name
        item_to_add = next((item for item in available_items if item.name.lower() == item_name.lower()), None)
        if item_to_add:
            myBasket.add_item(item_to_add, quantity)
            print(f"Added {quantity} of {item_name}.")
        else:
            print("Item not found.")

    elif response == "2":
        display_available_items()
        item_name = input("Enter the name of the item you want to remove: ")
        quantity = int(input("How much do you want to remove?: "))
        item_to_remove = next((item for item in available_items if item.name.lower() == item_name.lower()), None)
        if item_to_remove:
            myBasket.remove_item(item_to_remove, quantity)
            print(f" Removed {quantity} of {item_name}.")
        else:
            print("Item not found")

    elif response == "3":
        myBasket.view()
        item_name = (input("What item's quantity do you wish to update?: "))
        num = int(input("How many of this item do you wish to add?: "))
        item_to_update = next((item for item in available_items if item.name.lower() == item_name.lower()), None)
        if item_to_update:
            myBasket.update_item(item_to_update, num)
            print(f" {item_name} has been updated {num} times.")
        else:
            print("Item not found")

    elif response == "4":
        myBasket.view()

    elif response == "5":
        cat = input("What category would you like to filter by?: ")
        (myBasket.filter_by_category(cat))

    elif response == "6":
        myBasket.do_checkout()

    elif response == "7":
        print("Exiting the program.")
        break

    else:
        print("Invalid Response")
