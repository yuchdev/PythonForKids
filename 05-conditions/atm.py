account = 0
print("Your current balance is: VND " + str(account))
print("Welcome to the ATM!")
account += 1000000
print("Your current balance is: VND " + str(account))

# Let's convert 1000000 to USD
exchange_rate = 23000
usd = account / exchange_rate
print("Your current balance is: $" + str(usd))
