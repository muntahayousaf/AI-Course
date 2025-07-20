# Question no 16: 
# Calculate Body Mass Index (BMI) Input weight (kg) and height (m), then calculate: BMI = weight / (height ** 2)

weight = int(input("Enter weight (kg) :"))
height = float(input("Enter height (m) :"))
BMI = weight / (height ** 2)
print("Your Body Mass Index = " , round(BMI , 2))