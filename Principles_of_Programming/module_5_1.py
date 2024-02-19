# Initialize total rainfall
total_rainfall = 0

# Get the number of years
years = int(input("Enter the number of years: "))

# Loop through each year
for year in range(1, years + 1):
    # Loop through each month
    for month in range(1, 13):
        # Get the rainfall for the month
        rainfall = float(input(f"Enter the rainfall for year {year}, month {month} (in inches): "))
        total_rainfall += rainfall

# Calculate total months
total_months = years * 12

# Calculate average rainfall
average_rainfall = total_rainfall / total_months

# Display the results
print(f"Total number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
