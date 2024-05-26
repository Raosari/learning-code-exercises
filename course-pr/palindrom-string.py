from functools import reduce

def palindromo(string):
    cleaned_txt = string.replace(" ","").lower()
    return cleaned_txt == cleaned_txt[::-1]


def palindromo2(string):
    return string == reduce(lambda acc, char: char + acc, string.replace(" ","").lower())


def palindromo3(string):   
    string = string.replace(" ","").lower()
    reversed = []
    for char in string:
        reversed.insert(0,char)   #dudo de la eficiencia aqui
    return string == "".join(reversed)

a = palindromo3("amo la paloma")
print(a)
