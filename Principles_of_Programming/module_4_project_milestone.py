class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")


def get_item_details(order_number):
    print(f"\nItem {order_number}")
    name = input("Enter the item name:\n")
    price = float(input("Enter the item price:\n"))
    quantity = int(input("Enter the item quantity:\n"))
    return ItemToPurchase(name, price, quantity)


def print_total_cost(item1, item2):
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print(f"Total: ${total}")


def main():
    # Create two ItemToPurchase objects based on user input
    item1 = get_item_details(1)
    item2 = get_item_details(2)

    # Calculate and output the total cost
    print_total_cost(item1, item2)


if __name__ == "__main__":
    main()
