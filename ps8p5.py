# Open the file for reading
with open('ps8p5file.txt', 'r') as file:

    # Initialize variables for the total tuition and number of students
    totalTuition = 0
    numStudents = 0

    # Loop through each line in the file
    for line in file:

        # Split the line into the last name, district code, and credits taken
        parts = line.strip().split()
        lastName = parts[0]
        districtCode = parts[1]
        creditsTaken = int(parts[2])

        # Calculate the tuition owed based on the district code and credits taken
        if districtCode == "I":
            tuitionOwed = creditsTaken * 250.00
        else:
            tuitionOwed = creditsTaken * 500.00

        # Add the tuition owed to the total and increment the number of students
        totalTuition += tuitionOwed
        numStudents += 1

        # Display the student's last name, credits taken, and tuition owed
        print(f"{lastName}: {creditsTaken} credits, ${tuitionOwed:,.2f} tuition owed")

    # Display the total tuition owed and the number of students
    print(f"\nTotal tuition owed: ${totalTuition:,.2f}")
    print(f"Number of students: {numStudents}")
