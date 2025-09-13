# Question no 7: 

# Distribute Items Equally - You have n candies and k students. 
# Write a program to find:how many candies each student gets how many are left 

n = int(input("Enter total no of candies:"))
k = int(input("Enter total no of students:"))

each_student_gets = n // k
print("Candies each student gets =" , each_student_gets , "candies")

candies_left = n % k
print("Candies left =" , candies_left , "candies")