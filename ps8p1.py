principleAmount = float(input("Enter principle amount: "))
interestRate = float(input("Enter interest rate: "))
interestEarned = 0

print("Year\tBeginning Balance\tEnding Balance")
for year in range(1, 6):
    annualInterest = principleAmount * interestRate
    interestEarned += annualInterest
    beginningBalance = principleAmount
    endingBalance = beginningBalance + annualInterest
    print(f"{year}\t${beginningBalance:,.2f}\t\t${endingBalance:,.2f}")
    principleAmount = endingBalance

print(f"Total interest earned: ${interestEarned:,.2f}")
