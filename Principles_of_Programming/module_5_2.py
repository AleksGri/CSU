# Get the number of books purchased
books_purchased = int(input("Enter the number of books purchased this month: "))

# Determine points awarded
if books_purchased == 0:
    points = 0
elif books_purchased == 2:
    points = 5
elif books_purchased == 4:
    points = 15
elif books_purchased == 6:
    points = 30
elif books_purchased >= 8:
    points = 60

# Display the points
print(f"Points awarded: {points}")
