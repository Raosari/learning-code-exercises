import functools

def palindromo(string):
    cleaned_txt = string.replace(" ","")
    reversed_string = cleaned_txt[::-1]

    if cleaned_txt.lower() == reversed_string.lower():
        return f'el texto: "{string}", es un palindromo'
    else:
        return -1

def palindromo2(string):
    cleaned_text = string.replace(" ","")
    reversed_string = functools.reduce(lambda acc, char: char + acc,cleaned_text)
    return cleaned_text.lower() == reversed_string.lower() 
                
a = palindromo2("amo la paloma")
print(a)

