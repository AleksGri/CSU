#Part 1

def calculate_meal_total(food_charge):
    """Tips and gratuities are not taxable when they are left on the table
    or location where the service took place or when they are added
    to the charge receipt after the price and tax are calculated. """


    # Constants for the tip and sales tax rates
    tip_rate = 0.18
    sales_tax_rate = 0.07

    # Calculate the sales tax on the food charge
    sales_tax = food_charge * sales_tax_rate

    # Calculate the total price before tip
    total_before_tip = food_charge + sales_tax

    # Calculate the tip based on the food charge
    # Tips are calculated based on the food charge excluding tax.

    tip = food_charge * tip_rate

    # Calculate the final total price
    total_price = total_before_tip + tip

    # Display the results
    print(f"Food Charge: ${food_charge:.2f}")
    print(f"Sales Tax (7%): ${sales_tax:.2f}")
    print(f"Total Before Tip: ${total_before_tip:.2f}")
    print(f"Tip (18% of Total Before Tip): ${tip:.2f}")
    print(f"Total Price: ${total_price:.2f}")


# Prompt user to enter the charge for the food
food_charge = float(input("Enter the charge for the food: $"))

# Call the function to execute the program
calculate_meal_total(food_charge)
