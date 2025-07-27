# Question no 12: 
# Currency Converter (USD to PKR) Input amount in USD. Convert using a fixed exchange rate.

amount_in_USD = int(input("Enter amount in USD :"))
exchange_rate = 285
amount_in_PKR = amount_in_USD * exchange_rate
print(amount_in_USD , "USD = " , amount_in_PKR , "PKR")