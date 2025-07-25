# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 3500,
    "MSFT": 300
}

portfolio = {}
total_value = 0

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Get number of stocks user wants to input
num_stocks = int(input("How many different stocks do you want to add? "))

for _ in range(num_stocks):
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    
    if stock not in stock_prices:
        print(f"Stock '{stock}' not found in database. Try again.")
        continue
    
    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = quantity
    total_value += stock_prices[stock] * quantity

# Display results
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# (Optional) Save to file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Your Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print("Portfolio saved to 'portfolio_summary.txt'")