import numpy as np

addressV1 , keysV1 , nameV1 , latV1 , lonV1  = np.genfromtxt("C:\\Users\\admin\\OneDrive\\Documents\\GitHub\\AI-Course\\Pandas-Numpy-Seaborn practice\\FastFood Restaurant Project\\FastFoodRestaurantsV2.csv" ,
                                                                 delimiter="," , dtype=None ,
                                                                invalid_raise=False ,  unpack=True ,
                                                                 usecols=(0, 3, 6, 4 , 5) , skip_header=1)

print("address:" , addressV1[:10])
print("keys:" , keysV1[:10])
print("name:" , nameV1[:10])
print("lat" , latV1[:10])
print("longitude" , lonV1[:10])

# statistics operations
print("Fast food latitude mean" , np.mean(latV1))
print("Fast food latitude average" , np.average(latV1))
print("Fast food latitude std" , np.std(latV1))
print("Fast food latitude mod: " , np.median(latV1))
print("Fast food latitude percentile - 25: " , np.percentile(latV1,25))
print("Fast food latitude percentile  - 75: " , np.percentile(latV1,75))
print("Fast food latitude percentile  - 3: " , np.percentile(latV1,3))
print("Fast food latitude : " , np.min(latV1))
print("Fast food latitude max : " , np.max(latV1))

# maths operations
print("Fast food latitude square: " , np.square(latV1))
print("Fast food latitude sqrt: " , np.sqrt(latV1))
print("Fast food latitude pow: " , np.power(latV1,latV1))
print("Fast food latitude abs: " , np.abs(latV1))



# Perform basic arithmetic operations
addition = lonV1 + latV1
subtraction = lonV1 - latV1
multiplication = lonV1 * latV1
division = lonV1 / latV1

print(" Fast food latitude - lat - Addition:", addition)
print(" Fast food latitude - lat - Subtraction:", subtraction)
print("Fast food latitude - lat - Multiplication:", multiplication)
print(" Fast food latitude- lat - Division:", division)


#Trigonometric Functions

latitutePie = (latV1/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(latitutePie)
cosine_values = np.cos(latitutePie)
tangent_values = np.tan(latitutePie)

print("Fast food latitude- lat - pie  - Sine values:", sine_values)
print("Fast food latitude- lat - pie Cosine values:", cosine_values)
print("Fast food latitude- lat - pie Tangent values:", tangent_values)

print("Fast food latitude- lat - pie  - Exponential values:", np.exp(latitutePie))


# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(latitutePie)
log10_array = np.log10(latitutePie)

print("Fast food latitude- lat - pie  - Natural logarithm values:", log_array)
print("Fast food latitude- lat - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(latitutePie)
print("Fast food latitude- lat - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(latitutePie)
print("Fast food - lat - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(latitutePie)
print("Fast food - lat - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(latitutePie)
print("Fast food - lat - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(latitutePie)
print("Zameen.com Price - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)


#fast food Long Plus Lat - 2 dimentional arrary
D2LongLat = np.array([lonV1,
                  latV1])

print ("Fast food - lat - 2 dimentional arrary - " ,D2LongLat)

# check the dimension of array1
print("Fast food - lat - 2 dimentional arrary - dimension" , D2LongLat.ndim) 
# Output: 2

# return total number of elements in array1
print("Fast food - lat - 2 dimentional arrary - total number of elements" ,D2LongLat.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("Fast food - lat - 2 dimentional arrary - gives size of array in each dimension" ,D2LongLat.shape)
# Output: (2,3)

# check the data type of array1
print("Fast food - lat - 2 dimentional arrary - data type" ,D2LongLat.dtype) 
# Output: int64

# Splicing array
D2LongLatSlice=  D2LongLat[:1,:5]
print("Fast food - lat - 2 dimentional arrary - Splicing array - D2LongLat[:1,:5] " , D2LongLatSlice)
D2LongLatSlice2=  D2LongLat[:1, 4:15:4]
print("Fast food - lat - 2 dimentional arrary - Splicing array - D2LongLat[:1, 4:15:4] " , D2LongLatSlice2)



# Indexing array
D2LongLatSliceItemOnly=  D2LongLatSlice[0,1]
print("Fast food - lat - 2 dimentional arrary - Index array - D2LongLatSlice[1,5] " , D2LongLatSliceItemOnly)
D2LongLatSlice2ItemOnly=  D2LongLatSlice2[0, 2]
print("Fast food - lat - 2 dimentional arrary - index array - D2LongLatSlice2[0, 2] " , D2LongLatSlice2ItemOnly)


#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2LongLat):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2LongLat):
    print(index, elem)

"""# for loop
rows = np.shape(D2LongLat[0])[0]
cols = np.shape(D2LongLat[1])[0]
for i in range(0, (rows + 1)):
    for j in range(0, (cols + 1)):
        print (D2LongLat[i,j])
"""


# 2 x 149 ========>>>>> 1  x 298 - reshape
D2LongLat1TO298 = np.reshape(D2LongLat, (1, 42))
print("Fast food - lat - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : " , D2LongLat1TO298)
print("Fast food - lat - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : Size " , D2LongLat1TO298.size)
print("Fast food - lat - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : ndim " , D2LongLat1TO298.ndim)
print("Fast food - lat - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : shape " , D2LongLat1TO298.shape)
print("Fast food - lat - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : ndim " , D2LongLat1TO298.ndim)




print()


