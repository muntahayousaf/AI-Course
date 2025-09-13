import numpy as np

price , bed , bath , acre_lot , house_size  = np.genfromtxt("C:\\Users\\admin\\OneDrive\\Documents\\GitHub\\AI-Course\\Pandas-Numpy-Seaborn practice\\Real Estate project\\realestateV1_data.csv" , delimiter="," , dtype=None ,
                                                                       invalid_raise=False ,  unpack=True ,
                                                                         usecols=(2, 3, 4, 5 , 10) , skip_header=1)

print("price:" , price)
print("bed:" , bed)
print("bath" , bath)
print("acre_lot:" , acre_lot)
print("house_size" , house_size)

# statistics operations
print("price of real estate mean : " , np.mean(price))
print("price of real estate average : " , np.average(price))
print("price of real estate std : " , np.std(price))
print("price of real estate median : " , np.median(price))
print("price of real estate percentile - 25: " , np.percentile(price,25))
print("price of real estate percentile  - 75: " , np.percentile(price,75))
print("price of real estate percentile  - 3: " , np.percentile(price,3))
print("price of real estate min value : " , np.min(price))
print("price of real estate max value : " , np.max(price))

# maths operations
print("price of real estate square: " , np.square(price))
print("price of real estate sqrt: " , np.sqrt(price))
print("price of real estate pow: " , np.power(price,price))
print("price of real estate abs: " , np.abs(price))



# Perform basic arithmetic operations
addition = acre_lot + price
subtraction = acre_lot - price
multiplication = acre_lot * price
division = acre_lot / price

print(" start up growth - Addition:", addition)
print(" start up growth - Subtraction:", subtraction)
print("start up growth - Multiplication:", multiplication)
print("start up growth - Division:", division)


#Trigonometric Functions

pricePie = (price/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(price)
cosine_values = np.cos(price)
tangent_values = np.tan(price)

print("real estate - pie - Sine values:", sine_values)
print("real estate - pie - Cosine values:", cosine_values)
print("real estate - pie - Tangent values:", tangent_values)

print("real estate - pie  - Exponential values:", np.exp(pricePie))


# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(pricePie)
log10_array = np.log10(pricePie)

print("real estate - pie  - Natural logarithm values:", log_array)
print("real estate - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(pricePie)
print("real estate - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(pricePie)
print("real estate - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(pricePie)
print("real estate - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(pricePie)
print("real estate - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(pricePie)
print("real estate - pie   -Inverse Hyperbolic Cosine values:", acosh_values)


#start up growth Long Plus Lat - 2 dimentional arrary
D2priceacre = np.array([price , acre_lot])

print ("real estate - 2 dimentional arrary - " ,D2priceacre )

# check the dimension of array1
print("real estate - 2 dimentional arrary - dimension" , D2priceacre.ndim) 
# Output: 2

# return total number of elements in array1
print("real estate - 2 dimentional arrary - total number of elements" ,D2priceacre.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("real estate - 2 dimentional arrary - gives size of array in each dimension" ,D2priceacre.shape)
# Output: (2,3)

# check the data type of array1
print("real estate - 2 dimentional arrary - data type" ,D2priceacre.dtype) 
# Output: int64

# Splicing array
D2priceacreSlice=  D2priceacre[:1,:5]
print("real estate - 2 dimentional arrary - Splicing array - D2LongLat[:1,:5] " , D2priceacreSlice)
D2priceacreSlice2= D2priceacre[:1, 4:15:4]
print("real estate - 2 dimentional arrary - Splicing array - D2LongLat[:1, 4:15:4] " , D2priceacreSlice2)



# Indexing array
D2priceacreSliceItemOnly=  D2priceacreSlice[0,1]
print("start up growth - 2 dimentional arrary - Index array - D2LongLatSlice[1,5] " , D2priceacreSliceItemOnly)
D2priceacreSlice2ItemOnly=  D2priceacreSlice2[0, 2]
print("start up growth - 2 dimentional arrary - index array - D2LongLatSlice2[0, 2] " , D2priceacreSlice2ItemOnly)


#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2priceacre):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2priceacre):
    print(index, elem)

"""# for loop
rows = np.shape(D2LongLat[0])[0]
cols = np.shape(D2LongLat[1])[0]
for i in range(0, (rows + 1)):
    for j in range(0, (cols + 1)):
        print (D2LongLat[i,j])
"""


# 2 x 149 ========>>>>> 1  x 298 - reshape
D2priceacre1TO10000 = np.reshape(D2priceacre, (1, 400))
print("real estate - 2 dimentional arrary - np.reshape(D2priceacre, (1, 400)) : " , D2priceacre1TO10000)
print("real estate - 2 dimentional arrary - np.reshape(D2priceacre, (1, 400)) : Size " , D2priceacre1TO10000.size)
print("real estate - 2 dimentional arrary - np.reshape(D2priceacre, (1, 400)) : ndim " , D2priceacre1TO10000.ndim)
print("real estate - 2 dimentional arrary - np.reshape(D2priceacre, (1, 400)) : shape " , D2priceacre1TO10000.shape)
print("real estate - 2 dimentional arrary - np.reshape(D2priceacre, (1, 400)) : ndim " , D2priceacre1TO10000.ndim)




print()

