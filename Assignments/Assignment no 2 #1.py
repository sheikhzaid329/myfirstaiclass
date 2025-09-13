#Mark: String Malipulation

#Write a program to create a new string made of an input string’s 
# first, middle, and last character.

User_Input =(input("type a String:"))

lenth =len(User_Input)

if lenth == 0:
    print(" ")

First =User_Input[0]

Last =User_Input[-1]

M =lenth//2

Middle =User_Input[M]

print(First+Middle+Last)

#Write a program to count occurrences of all 
# characters within a string Given

User_Input= str(input("Enter a string: "))

Lenth= len(User_Input) 

print('Lenth: '+str(Lenth))

#Reverse a given string

User_input=(input("Enter a String: "))

print(User_input [: :-1])

#Split a string on hyphens

list=('Java-Python-C++')

split= list.split('-')

print(split)

#Remove special symbols / punctuation from a string

strings= "hello?, pakistan!"

removed= ""

for i in strings:
   
   if i.isalnum():

    removed= removed + i

print(removed)




