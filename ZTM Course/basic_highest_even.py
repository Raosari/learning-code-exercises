
def high_even(li):
    evens = []
    for el in li:
        if el % 2 == 0:
            evens.append(el)
    return max(evens)

    # li.reduce(lambda acc,a: acc if a )

a = high_even([10,2,3,4,8,11,56])
print(a)