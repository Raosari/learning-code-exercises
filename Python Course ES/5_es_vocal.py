def is_vowel(char):
    vowels = ['A','E','I','O','U']
    return char.upper() in vowels


def is_vowel2(char):
    char = char.upper()
    if char == 'A':
        return True
    elif char == 'E':
        return True
    elif char == 'I':
        return True
    elif char == 'O':
        return True
    elif char == 'U':
        return True
    else:
        return False

print(is_vowel('a'))
print(is_vowel2('a'))


