# Open the file for reading
with open("ps8p3file.txt", "r") as file:

    # Initialize the total bonus payout
    total_bonus = 0

    # Loop through each line in the file
    for line in file:

        # Split the line into last name and salary
        last_name, salary = line.strip().split()

        # Convert salary to float
        salary = float(salary)

        # Determine the bonus rate based on the salary
        if salary >= 100000.00:
            bonus_rate = 0.2
        elif salary == 50000.00:
            bonus_rate = 0.15
        else:
            bonus_rate = 0.1

        # Calculate the bonus based on the salary and bonus rate
        bonus = salary * bonus_rate

        # Add the bonus to the total bonus payout
        total_bonus += bonus

        # Display the employee's last name, salary, and bonus
        print(f"{last_name}: {salary:.2f} - Bonus: {bonus:.2f}")

    # Display the total bonus payout
    print(f"Total Bonus Paid Out: {total_bonus:.2f}")