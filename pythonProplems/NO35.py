# Get input from user
loan_amount = float(input("Loan Amount: "))
num_years = int(input("Number of Years: "))

# Define the interest rates to be calculated
interest_rates = [0.05, 0.05125, 0.0525, 0.05375, 0.055, 0.05625, 0.0575, 0.05875, 0.06, 0.06125, 0.0625, 0.06375, 0.065, 0.06625, 0.0675, 0.06875, 0.07, 0.07125, 0.0725, 0.07375, 0.075, 0.07625, 0.0775, 0.07875, 0.08]

# Calculate and print monthly payment and total payment for each interest rate
print("Interest rate\tMonthly Payment\tTotal Payment")
for rate in interest_rates:
    monthly_rate = rate / 12
    num_payments = num_years * 12
    monthly_payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate)**(-num_payments))
    total_payment = monthly_payment * num_payments
    print(f"{rate:.3%}\t\t{monthly_payment:.2f}\t\t{total_payment:.2f}")