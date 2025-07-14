#String Manipulation :

#1. Write a program to create a new string made of an input string’s first, middle, and last character.

name = input("Enter your name :")
lenght = len(name)
first_char = name[0]
middle_char = name[len(name)//2]
last_char = name[-1]
new_name = print("first , middle , last char are :" ,first_char + middle_char + last_char)


#2. Write a program to count occurrences of all characters within a string Given. 

#occurence of name
occurence = print("occurence of all characters in string = " , len(name))


#3. Reverse a given string

reverse_str = name[::-1]
print("Reversed string : " , reverse_str)


#4. Split a string on hyphens 

str = "I-am-a-girl"
splitted_str = str.split(",")
print("Splitted string is :")
for splitted in splitted_str :
    print(splitted)


#5. Remove special symbols / punctuation from a string

text = "Muntah@"
remove_symbol = text.replace("@" , "a")
print("Removed symbol :" , remove_symbol)
