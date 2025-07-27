# Question no 17: 
# Convert Minutes to Hours and Minutes 
# Input number of minutes and convert to hours and remaining minutes. 
# Example: 130 minutes → 2 hours 10 minutes 
 
total_mins = int(input("Enter total no of mins :"))
hours = total_mins // 60
mins = total_mins % 60

print(total_mins , "minutes =" , hours , "hours and ", mins , "minutes")