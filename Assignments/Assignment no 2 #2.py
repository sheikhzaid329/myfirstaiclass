#Mark: List Manipulation

# Reverse a list in Python

rev= [12,34,56]

rev.reverse()

print(list)

#Turn every item of a list into its square

square= ["hello, world"]

turned= [list(s) for s in square ]

print(turned)




# Remove empty strings from the list of strings

strings= ["apple", "", "banana", "", "cherry"]

List= (filter(None,strings))

print(strings)


#Add new item to list after a specified item

add= ["apple","mango","banana"]

add.insert(2,"oranges")

#replace list’s item with new value if found

add[1]= "cherry"

print(add)




