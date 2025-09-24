import numpy as np

address , country , long , lat =np.genfromtxt('Fastfood Restaurant/FastFoodRestaurants.csv',delimiter=',',dtype=None,usecols=[0,2,4,5],unpack=True,skip_header=1,invalid_raise=False)

print(address)
print(country)
print(long)
print(lat)

# basic arithmetic operations
addition = long + lat

print(" FastFood Restaurant long - lat - Addition:", addition)


# long Plus Lat - 2 dimentional arrary
D2longLat = np.array([long,
                  lat])

print ("FastFood Restaurant long Plus Lat - 2 dimentional arrary - " ,D2longLat)

# check the dimension of array1
print("FastFood Restaurant long Plus Lat - 2 dimentional arrary - dimension" , D2longLat.ndim) 
# Output: 2

# return total number of elements in array1
print("FastFood Restaurant long Plus Lat - 2 dimentional arrary - total number of elements" ,D2longLat.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("FastFood Restaurant long Plus Lat - 2 dimentional arrary - gives size of array in each dimension" ,D2longLat.shape)
# Output: (2,3)

# check the data type of array1
print("FastFood Restaurant long Plus Lat - 2 dimentional arrary - data type" ,D2longLat.dtype) 
# Output: int64

# Splicing array
D2longLatSlice=  D2longLat[:1,:5]
print("FastFood Restaurant long Plus Lat - 2 dimentional arrary - Splicing array - D2longLat[:1,:5] " , D2longLatSlice)
D2longLatSlice2=  D2longLat[:1, 4:15:4]
print("FastFood Restaurant long Plus Lat - 2 dimentional arrary - Splicing array - D2longLat[:1, 4:15:4] " , D2longLatSlice2)



# Indexing array
D2longLatSliceItemOnly=  D2longLatSlice[0,1]
print("FastFood Restaurant long Plus Lat - 2 dimentional arrary - Index array - D2longLatSlice[1,5] " , D2longLatSliceItemOnly)
D2longLatSlice2ItemOnly=  D2longLatSlice2[0, 2]
print("FastFood Restaurant long Plus Lat - 2 dimentional arrary - index array - D2longLatSlice2[0, 2] " , D2longLatSlice2ItemOnly)


#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2longLat):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2longLat):
    print(index, elem)
