# List manipulation

student_data = [5 , 40 , 15 , 75.5 ]

# Reverse a list
reverse_data = student_data[::-1]
print("Reverse of list :" , reverse_data)

# square of every member of list
square_of_list = [x**2 for x in student_data]
print("Square of every member:" , square_of_list)

# Remove empty string from list
Name_of_students = ["Amna" , "Muntaha" , "" , "Tuba" , ""]
string_removed = list(filter(None , Name_of_students))
print("Remaove empty string:" , string_removed)

# Add new item to the string after specified item
new_list = Name_of_students.append("Aniqa")
print("Add new item:" , Name_of_students)

# Replace list item with new item 
replaced_list = Name_of_students.insert(3 , "Hina")
print("Replaced value" , Name_of_students)