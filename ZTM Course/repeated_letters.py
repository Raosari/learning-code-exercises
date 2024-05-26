some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

frecuency = {}
rep = []
for element in some_list:
    if not element in frecuency:
        frecuency[element] = 1
    else:
        frecuency[element] += 1

# for k,v in frecuency.items():
#     if v > 1:
#         rep.append(k)

rep1 = [k for k,v in frecuency.items() if v>1]

# print(rep)
print(rep1)  

# Now try to solve it in one line of code, notice that its not as readable as we wish, but practice list comprehension
some_list1 = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([item for item in some_list1 if some_list1.count(item)>1]))
print(duplicates)