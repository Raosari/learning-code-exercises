my_list = [5,4,3]
#square
#write a annonymous function that return the list of its squares
print(list(map(lambda item:item**2,my_list)))


# List sorting
#Sort the next list based on its second element
a = [(0,2),(4,3),(10,-1),(9,9)]

a.sort(key = lambda index: index[1])
print(a)