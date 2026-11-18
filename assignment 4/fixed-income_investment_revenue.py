
# Fixed-income Investment Revenue

# Get and validate monthly investment
while (monthly_input := input("Enter monthly investment amount: ")):
    try:
        monthly_investment = float(monthly_input)
        if monthly_investment > 0:
            break
        print("Error: Please enter a positive number.")
    except ValueError:
        print("Error: Please enter a valid number.")

# Get and validate yearly interest rate
while (rate_input := input("Enter yearly interest rate (e.g., 5 for 5%): ")):
    try:
        yearly_interest_rate = float(rate_input)
        if yearly_interest_rate > 0:
            break
        print("Error: Please enter a positive number.")
    except ValueError:
        print("Error: Please enter a valid number.")

# Get and validate investment years
while (years_input := input("Enter investment years: ")):
    try:
        investment_years = int(years_input)
        if investment_years > 0:
            break
        print("Error: Please enter a positive integer.")
    except ValueError:
        print("Error: Please enter a valid integer.")

# Calculate monthly compound investment revenue
monthly_interest_rate = yearly_interest_rate / 100 / 12
total_investment = 0.0
total_deposits = 0.0

for month in range(investment_years * 12):
    total_investment *= (1 + monthly_interest_rate)
    total_investment += monthly_investment
    total_deposits += monthly_investment

# Calculate investment revenue
investment_revenue = total_investment - total_deposits
monthly_revenue = investment_revenue / (investment_years * 12)

# Display results
print(f"Total investment value: ${total_investment:,.2f}")
print(f"Total investment revenue: ${investment_revenue:,.2f}")
print(f"Monthly revenue (average): ${monthly_revenue:,.2f}")
