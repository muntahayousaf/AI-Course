# Question no 9:

# Total Marks and Percentage Input marks of 5 subjects. Print:  Total marks , Percentage , Average

phy = int(input("Enter marks of phy :"))
chem = int(input("Enter marks of chem :"))
maths = int(input("Enter marks of maths :"))
eng = int(input("Enter marks of eng :"))
urdu = int(input("Enter marks of urdu :"))

Total_marks = phy + chem + maths + eng + urdu
print("Total marks obtain = " , Total_marks)
max_total = 500

Average = (Total_marks)/5
print("Average = " , Average)

Percentage = (Total_marks / max_total) * 100
print("Percentage = " , Percentage , "%")