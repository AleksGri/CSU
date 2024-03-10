from module_4_project_milestone import ItemToPurchase
from module_6_project_milestone import ShoppingCart

class ExtendedItemToPurchase(ItemToPurchase):
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        super().__init__(item_name, item_price, item_quantity)
        self.item_description = item_description

class ExtendedShoppingCart(ShoppingCart):
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description if hasattr(item, 'item_description') else 'No description available.'}")

def add_item_to_cart(shopping_cart):
    item_name = input("Enter the item name:\n")
    item_price = float(input("Enter the item price:\n"))
    item_quantity = int(input("Enter the item quantity:\n"))
    item_description = input("Enter the item description:\n")
    item_to_purchase = ExtendedItemToPurchase(item_name, item_price, item_quantity, item_description)
    shopping_cart.add_item(item_to_purchase)

def remove_item_from_cart(shopping_cart):
    item_name = input("Enter name of item to remove:\n")
    shopping_cart.remove_item(item_name)

def change_item_quantity(shopping_cart):
    item_name = input("Enter the item name:\n")
    item_quantity = int(input("Enter the new quantity:\n"))
    shopping_cart.modify_item(ExtendedItemToPurchase(item_name, item_quantity=item_quantity))

def print_menu(shopping_cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )
    command = ''
    while command != 'q':
        print(menu)
        command = input("Choose an option:\n")
        if command == 'a':
            add_item_to_cart(shopping_cart)
        elif command == 'r':
            remove_item_from_cart(shopping_cart)
        elif command == 'c':
            change_item_quantity(shopping_cart)
        elif command == 'i':
            shopping_cart.print_descriptions()
        elif command == 'o':
            shopping_cart.print_total()

def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    new_cart = ExtendedShoppingCart(customer_name, current_date)
    print_menu(new_cart)

if __name__ == "__main__":
    main()
