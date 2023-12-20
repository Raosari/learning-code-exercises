def fibonacci(index):
    arr = [0,1]
    for i in range(2,index+1):
        arr.append(arr[i-1] + arr[i-2])
    return arr[index]

a = fibonacci(0)
print(a)