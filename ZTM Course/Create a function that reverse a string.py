#Create a function that reverse a string
#Hi mi name is andrew
#Should be: werdna si eman im ih
def checkForString(str1):
    if type(str1) != str:
        return "Eleme"
    elif len(str1) < 2:
        return "Element is one letter, cannot be reversed"
    

def Reverse1(str1):        
        string_array = []
        reversed_array = []

        for i in range(len(str1)):
            caracter = str1[i]
            string_array.append(caracter)
        
        for j in string_array:
            reversed_array.insert(0,j)
            answer = "".join(reversed_array)
        return answer

def Reverse2(str1): 
    reversed_array = []
    for i in range(len(str1),0,-1):
        reversed_array.append(str1[i-1])
    return "".join(reversed_array)

def Reverse3(str1):  
    return str1[::-1]

string1 = "Hello my name is Rao"
print(Reverse2(string1))


