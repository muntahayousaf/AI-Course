# Print first 10 numbers using while

i = 1
while i <= 10:
    print('First 10 numbers is :' , i)
    i += 1

# Take input from user, and print even number till that even number

num = int(input("Enter any number:"))

if num % 2 != 0:
    print("Please enter an even number.")
else:
    i = 2
    while i <= num:
        print(i)
        i += 2

# Take input from user, and print odd number till that even number

num1 = int(input("Enter any number:"))

if num1 % 2 != 0:
    print("Please enter an odd number.")
else:
    i = 1
    while i <= num:
        print(i)
        i += 2

# Take input from user, and print prime number till that even number

num = int(input("Enter any number: "))

if num % 2 != 0:
    print("Please enter an even number.")
else:
    print("Prime numbers up to", num, "are:")
    for i in range(2, num + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)

#Print multiplication of given number

num = int(input("Enter any number :"))
print('Multiplication of number :')
for i in range(1 , 11):
    print(f"{num} x {i} = {num * i}")