# Dictionary manipulation

# Check if a value exist in dictionary

Data = {'Name': 'Muntaha' , 'Age' : 22 , 'City' : 'Lahore' , 'Country' : 'Pakistan' , 'Phy' : 56 , 'Chem' : 45}

if 'City' in Data:
    print("Yes Exist")
else:
    print("No, not Exist")

# Get the keys of a minimum values from dictionary

numeric_val = {'Phy': 55 , 'Chem' : 35 , 'Maths' : 75 , 'Urdu' : 35 , 'Eng' : 50 }
min_val = min(numeric_val.values())
min_keys = []
for key, value in numeric_val.items():
    if value == min_val:
        min_keys.append(key)
        print("Keys with min value is :" , min_keys)


# Delete a list of keys from dictionary

keys_to_del = ['City' , 'Phy' , 'Chem']
for key in keys_to_del:
    if key in Data:
        del Data[key]
        print(Data)