# Get user input and convert to float
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses
print("Your monthly savings are", monthly_savings)

# Project savings over a year with 5% interest
projected_savings = monthly_savings * 12 * 0.05  # Adds 5% interest

# Display results
print("Projected savings after one year, with interest, is:", projected_savings)
