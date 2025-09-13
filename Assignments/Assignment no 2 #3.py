#Mark: Dictionary Manipulation 

# Check if a value exists in a dictionary

dict= {
    'Pakistan':'Islamabad',
    'America':'Washington',
    'Gemany':'Berlin'
}

print(dict['Pakistan'])

# Get the key of a minimum value from the following dictionary

thisdict={
    'a':12,
    'b':34,
    'c':76
}    
print(min(thisdict))

#Delete a list of keys from a dictionary

thisdict1={
    'A':'B',
    'C': 'D',
    'E':'F'
}

thisdict1.pop('A')

print(thisdict1)
