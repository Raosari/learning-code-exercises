
def Solution(N):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #next_value will create a dic 'aa':'b', 'cc':'d','ee':'f'...'yy':'z' to replace the next char
    next_value = { alphabet[i]*2: alphabet[i+1] for i in range(len(alphabet)-1)}
    string = "a" * N
    for chars in next_value.keys():
        string = string.replace(chars, next_value[chars])
    return string
