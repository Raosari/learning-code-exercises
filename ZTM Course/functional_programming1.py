from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capitalize_func(li):
    return li.capitalize()     

print(list(map(capitalize_func,my_pets)))
print(my_pets)

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
sorted_numbers = my_numbers.copy()
sorted_numbers.sort()

print(list(zip(sorted_numbers,my_strings)))
#after seeing solution is better using sorted() function, i forget about sorted and sort

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def filter_scores(score):
    return score >= 50
print(list(filter(filter_scores,scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
combinated_numbers = my_numbers.copy()
combinated_numbers.extend(scores)

def sum1(acc,item):
    return acc + item

print(reduce(sum1,combinated_numbers,0))
#my comment: after seeing resolution video, is better apply reduce function (my_numbers + scores)