import numpy as np

price , bed , street , zipcode= np.genfromtxt('Numpy Pandas Practice/RealEstate-USA.csv',delimiter=',', usecols=[2,3,7,9],unpack=True,dtype=None,skip_header=1,invalid_raise=False)

print(price)
print(bed)
print(street)
print(zipcode)

#Statistics Operation

print('RealEstate USA price mean: ', np.mean(price))
print('RealEstate USA price std: ', np.std(price))
print('RealEstate USA price Average:', np.average(price))
print('RealEstate USA price median:', np.median(price))
print("RealEstate USA Price percentile - 25: " , np.percentile(price,25))
print("RealEstate USA Price percentile  - 75: " , np.percentile(price,75))
print("RealEstate USA Price percentile  - 3: " , np.percentile(price,3))
print("RealEstate USA Price min : " , np.min(price))
print("RealEstate USA Price max : " , np.max(price))

#Maths Operation

print('RealEstate USA price square:', np.square(price))
print('RealEstate USA price sqrt:', np.sqrt(price))
print('RealEstate USA price power:',np.power(price,zipcode))
print('RealEstate USA price abs:',np.abs(price))


addition = zipcode + price
subtraction = zipcode - price
multiplication = zipcode * price
division = zipcode / price

print(" RealEstate USA zipcode - price - Addition:", addition)
print(" RealEstate USA zipcode - price - Subtraction:", subtraction)
print(" RealEstate USA zipcode - price - Multiplication:", multiplication)
print(" RealEstate USA zipcode - price - Division:", division)

pricePie = (price/np.pi) +1

sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)

print("RealEstate USA Price - div - pie  - Sine values:", sine_values)
print("RealEstate USA Price - div - pie Cosine values:", cosine_values)
print("RealEstate USA Price - div - pie Tangent values:", tangent_values)

print("RealEstate USA Price - div - pie  - Exponential values:", np.exp(pricePie))

log_array = np.log(pricePie)
log10_array = np.log10(pricePie)

print("RealEstate USA Price - div - pie  - Natural logarithm values:", log_array)
print("RealEstate USA Price - div - pie  = Base-10 logarithm values:", log10_array)

sinh_values = np.sinh(pricePie)
print("RealEstate USA Price - div - pie   - Hyperbolic Sine values:", sinh_values)

cosh_values = np.cosh(pricePie)
print("USA RealEstate Price - div - pie   - Hyperbolic Cosine values:", cosh_values)

tanh_values = np.tanh(pricePie)
print("USA RealEstate Price - div - pie   -Hyperbolic Tangent values:", tanh_values)

asinh_values = np.arcsinh(pricePie)
print("USA RealEstate Price - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

acosh_values = np.arccosh(pricePie)
print("USA RealEstate Price - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)

Dimension = np.array([price,
            zipcode  ])

print ("USA RealEstate Long Plus Lat - 2 dimentional arrary - " ,Dimension)

print("USA RealEstate Long Plus Lat - 2 dimentional arrary - dimension" , Dimension)
print("USA RealEstate long Plus Lat - 2 dimentional arrary - dimension" , Dimension.ndim) 
# Output: 2

# return total number of elements in array1
print("USA RealEstate long Plus Lat - 2 dimentional arrary - total number of elements" ,Dimension.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("USA RealEstate long Plus Lat - 2 dimentional arrary - gives size of array in each dimension" ,Dimension.shape)
# Output: (2,3)

# check the data type of array1
print("USA RealEstate long Plus Lat - 2 dimentional arrary - data type" ,Dimension.dtype) 
# Output: int64

# Splicing array
DimensionSlice=  Dimension[:1,:5]
print("USA RealEstate long Plus Lat - 2 dimentional arrary - Splicing array - Dimension[:1,:5] " , DimensionSlice)
DimensionSlice2=  Dimension[:1, 4:15:4]
print("USA RealEstate long Plus Lat - 2 dimentional arrary - Splicing array - Dimension[:1, 4:15:4] " , DimensionSlice2)



# Indexing array
DimensionSliceItemOnly=  DimensionSlice[0,1]
print("USA RealEstate long Plus Lat - 2 dimentional arrary - Index array - DimensionSlice[1,5] " , DimensionSliceItemOnly)
DimensionSlice2ItemOnly=  DimensionSlice2[0, 2]
print("USA RealEstate long Plus Lat - 2 dimentional arrary - index array - DimensionSlice2[0, 2] " , DimensionSlice2ItemOnly)


for elem in np.nditer(Dimension):
    print(elem)

for index, elem in np.ndenumerate(Dimension):
    print(index, elem)

# 2 x 149 ========>>>>> 1  x 298 - reshape

Dimension1TO298 = np.reshape(Dimension, (2,200 ))
print("USA RealEstate long Plus Lat - 2 dimentional arrary - np.reshape(Dimension, (1,200)) : Size " ,Dimension1TO298.size)
print("USA RealEstate long Plus Lat - 2 dimentional arrary - np.reshape(Dimension, (1,200)) : " , Dimension1TO298)
print("USA RealEstate long Plus Lat - 2 dimentional arrary - np.reshape(Dimension, (1,200)) : shape " , Dimension1TO298.shape)
print("USA RealEstate long Plus Lat - 2 dimentional arrary - np.reshape(Dimension, (1,200)) : ndim " , Dimension1TO298.ndim)




print()