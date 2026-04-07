#Splits the input characters into pairs

def spiltStrings(str):

    if len(str) % 2 != 0:
        str += '_'
    
    newStr = []

    for i in range(0, len(str), 2):
        newStr.append(str[i:i+2])

    return newStr

print(spiltStrings(input('Enter a string: ')))

    
