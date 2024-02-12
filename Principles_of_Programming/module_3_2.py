def alarm_time(current_time, wait_hours):
    # Calculate the alarm time
    alarm_time = (current_time + wait_hours) % 24

    # Display the time when the alarm will go off
    print(f"The alarm will go off at {alarm_time:02d}:00 hours.")


# Prompt user to enter the current time in hours on a 24-hour clock
current_time = int(input("Enter the current time (0-23 hours): "))

# Prompt user to enter the number of hours to wait for the alarm
wait_hours = int(input("Enter the number of hours to wait for the alarm: "))

# Call the function to execute the program
alarm_time(current_time, wait_hours)
