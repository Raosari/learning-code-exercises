def fibonacci(index):
    if index < 2:
        return index
    else:
        return fibonacci(index-1) + fibonacci(index-2)    

a = fibonacci(6)
print(a)

