# Question no 8

# Calculate Profit or Loss Input cost price and selling price. Display either: Profit and amount, or Loss and amount, or No Profit No Loss.

CP = int(input("Enter Cost Price (CP) :"))
SP = int(input("Enter Sale Price (SP) :"))

if SP > CP :
    profit = SP - CP
    print("Profit of = " , profit)

elif SP < CP :
    loss = CP - SP
    print("Loss of = " , loss)

else:
    print("No profit no loss")