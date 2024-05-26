#crear una funcion que invierta un string
def invert_string(str):
    return str[::-1]


def invert_string2(str):
    inverted = ""
    size_of_string = len(str) - 1
    for idx in range(size_of_string,-1,-1):
        inverted += str[idx]
    return inverted


def invert_string3(str):
    inverted = ""
    for char in str:
        inverted = char + inverted
    return inverted


def invert_string4(string):
    inverted = []
    for char in string:
        inverted.insert(0,char)
    return "".join(inverted)

print(invert_string4("Hola"))