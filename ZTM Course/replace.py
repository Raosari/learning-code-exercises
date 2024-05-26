N = 100
next_value = {
    "aa":"b","bb":"c","cc":"d",
    "dd":"e","ee":"f","ff":"g",
    "gg":"h","hh":"i","ii":"j",
    "jj":"k","kk":"l","ll":"m",
    "mm":"n","nn":"o","oo":"p",
    "pp":"q","qq":"r","rr":"s",
    "ss":"t","tt":"u","uu":"v",
    "vv":"w","ww":"x","xx":"y",
    "yy":"z"
}
string = "a" * N
for el in next_value:
    string = string.replace(el, next_value[el])
print(string)
