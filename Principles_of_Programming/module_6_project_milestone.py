class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_price != 0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${total_cost}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

def print_menu(shopping_cart):
    menu = '''\nMENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit\n'''
    command = ''
    while command != 'q':
        print(menu)
        command = input("Choose an option:\n")
        if command == 'a':
            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            item_to_purchase = ItemToPurchase(item_name, item_price, item_quantity)
            shopping_cart.add_item(item_to_purchase)
        elif command == 'r':
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            shopping_cart.remove_item(item_name)
        elif command == 'c':
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            item_quantity = int(input("Enter the new quantity:\n"))
            item_to_purchase = ItemToPurchase(item_name, item_quantity=item_quantity)
            shopping_cart.modify_item(item_to_purchase)
        elif command == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            shopping_cart.print_descriptions()
        elif command == 'o':
            print("\nOUTPUT SHOPPING CART")
            shopping_cart.print_total()

# Main function
def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    new_cart = ShoppingCart(customer_name, current_date)
    print_menu(new_cart)

if __name__ == "__main__":
    main()
