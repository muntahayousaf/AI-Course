my_save_data = {'Integer':7.666 , 'Marks':320 , 'Name':"Muntaha" , 'Father name':"M.Yousaf" }
print(my_save_data)
print(type(my_save_data))
print(my_save_data['Integer'])
print(my_save_data['Marks'])
my_save_data['CGPA'] = 3.6
print(my_save_data)
del my_save_data['Integer']
print(my_save_data)