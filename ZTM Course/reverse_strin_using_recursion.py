def reverse_string(string):
    if string == "":
        return ""
    else:
        return reverse_string(string[1:]) + string[0]

a = reverse_string("Raosari")
print(a)
    