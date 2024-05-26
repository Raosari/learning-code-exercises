def factorial_recursive(num):
    if num < 2:
        return 1
    return num * factorial_recursive(num-1)
a = factorial_recursive(1)
print(a)