import numpy as np

industry , funding_rounds , investment_amount , country , growth_rate  = np.genfromtxt("C:/Users/admin/OneDrive/Documents/GitHub/AI-Course/Python Data Science projects/Startup Growth Investment project/startup_growth_investment_data.csv" ,
                                                                                        delimiter="," , dtype=None ,
                                                                                        invalid_raise=False ,  unpack=True ,
                                                                                        usecols=(1, 2, 3, 6 , 8) , skip_header=1)

print("industry:" , industry)
print("funding rounds:" , funding_rounds)
print("investment amount:" , investment_amount)
print("country" , country)
print("growth rate" , growth_rate)

# statistics operations
print("investment amount mean" , np.mean(investment_amount))
print("investment amount average" , np.average(investment_amount))
print("investment amount std" , np.std(investment_amount))
print("investment amount mod: " , np.median(investment_amount))
print("investment amount percentile - 25: " , np.percentile(investment_amount,25))
print("investment amount percentile  - 75: " , np.percentile(investment_amount,75))
print("investment amount percentile  - 3: " , np.percentile(investment_amount,3))
print("investment amount : " , np.min(investment_amount))
print("investment amount : " , np.max(investment_amount))

# maths operations
print("investment amount square: " , np.square(investment_amount))
print("investment amount sqrt: " , np.sqrt(investment_amount))
print("investment amount pow: " , np.power(investment_amount,investment_amount))
print("investment amount abs: " , np.abs(investment_amount))



# Perform basic arithmetic operations
addition = funding_rounds + investment_amount
subtraction = funding_rounds - investment_amount
multiplication = funding_rounds * investment_amount
division = funding_rounds / investment_amount

print(" start up growth - Addition:", addition)
print(" start up growth - Subtraction:", subtraction)
print("start up growth - Multiplication:", multiplication)
print("start up growth - Division:", division)


#Trigonometric Functions

investment_amountPie = (investment_amount/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(investment_amount)
cosine_values = np.cos(investment_amount)
tangent_values = np.tan(investment_amount)

print("start up growth - pie  - Sine values:", sine_values)
print("start up growth - pie Cosine values:", cosine_values)
print("start up growth - pie Tangent values:", tangent_values)

print("start up growth - pie  - Exponential values:", np.exp(investment_amountPie))


# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(investment_amountPie)
log10_array = np.log10(investment_amountPie)

print("start up growth - pie  - Natural logarithm values:", log_array)
print("start up growth - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(investment_amountPie)
print("start up growth - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(investment_amountPie)
print("start up growth - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(investment_amountPie)
print("start up growth - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(investment_amountPie)
print("start up growth - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(investment_amountPie)
print("start up growth - pie   -Inverse Hyperbolic Cosine values:", acosh_values)


#start up growth Long Plus Lat - 2 dimentional arrary
D2investfund = np.array([investment_amount,
                  funding_rounds])

print ("start up growth - 2 dimentional arrary - " ,D2investfund )

# check the dimension of array1
print("start up growth - 2 dimentional arrary - dimension" , D2investfund.ndim) 
# Output: 2

# return total number of elements in array1
print("start up growth - 2 dimentional arrary - total number of elements" ,D2investfund.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("start up growth - 2 dimentional arrary - gives size of array in each dimension" ,D2investfund.shape)
# Output: (2,3)

# check the data type of array1
print("start up growth - 2 dimentional arrary - data type" ,D2investfund.dtype) 
# Output: int64

# Splicing array
D2investfundSlice=  D2investfund[:1,:5]
print("start up growth - 2 dimentional arrary - Splicing array - D2LongLat[:1,:5] " , D2investfundSlice)
D2investfundSlice2=  D2investfund [:1, 4:15:4]
print("start up growth - 2 dimentional arrary - Splicing array - D2LongLat[:1, 4:15:4] " , D2investfundSlice2)



# Indexing array
D2investfundSliceItemOnly=  D2investfundSlice[0,1]
print("start up growth - 2 dimentional arrary - Index array - D2LongLatSlice[1,5] " , D2investfundSliceItemOnly)
D2investfundSlice2ItemOnly=  D2investfundSlice2[0, 2]
print("start up growth - 2 dimentional arrary - index array - D2LongLatSlice2[0, 2] " , D2investfundSlice2ItemOnly)


#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2investfund):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2investfund):
    print(index, elem)

"""# for loop
rows = np.shape(D2LongLat[0])[0]
cols = np.shape(D2LongLat[1])[0]
for i in range(0, (rows + 1)):
    for j in range(0, (cols + 1)):
        print (D2LongLat[i,j])
"""


# 2 x 149 ========>>>>> 1  x 298 - reshape
D2investfund1TO10000 = np.reshape(D2investfund, (1, 10000))
print("start up growth - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : " , D2investfund1TO10000)
print("start up growth - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : Size " , D2investfund1TO10000.size)
print("start up growth - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : ndim " , D2investfund1TO10000.ndim)
print("start up growth - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : shape " , D2investfund1TO10000.shape)
print("start up growth - 2 dimentional arrary - np.reshape(D2LongLat, (1, 298)) : ndim " , D2investfund1TO10000.ndim)




print()

