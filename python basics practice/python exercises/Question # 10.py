# Question no 10:

# Salary Calculator Input basic salary. Calculate: HRA = 20% of basic , DA = 15% of basic ,Total Salary = Basic + HRA + DA.

basic_salary = int(input("Enter basic salary :"))

HRA = (20/100) * basic_salary
DA = (15/100) * basic_salary
Total_salary = basic_salary + HRA + DA

print("HRA (20%) = " , HRA)
print("DA (15%) = " , DA)
print("Total salary = " , Total_salary)