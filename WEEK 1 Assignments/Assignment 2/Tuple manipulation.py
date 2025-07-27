# Reverse a tuple

tuple = ( 2 , 3 , 5 , 7 )
reversed_tuple = tuple[::-1]
print("Reversed tuple is:" , reversed_tuple)

# Access value 20 from tuple

values = (13 , 15 , 20 , 50)
access_val = values[2]
print("Access value 20 from tuple:" , access_val)

# Swap two tuples in python

tuple1 = (1 , 2 , 3 , 4)
tuple2 = (5 , 6 , 7 , 8)

tuple1 , tuple2 = tuple2 , tuple1
print("tuple1 :" , tuple1)
print("tuple2 :" , tuple2)