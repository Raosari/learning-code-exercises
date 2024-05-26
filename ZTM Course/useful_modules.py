from collections import Counter,defaultdict,OrderedDict
import datetime

li = [1,2,3,4,5,6,5,6,3]
sentence = 'Hi my name is Raosari, and you are awesome'


# print(Counter(li))
# print(Counter(sentence))

dictionary = defaultdict(lambda:"Does not exist",{'a':1,'b':2})
# print(dictionary['c'])

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1


# print(d1 == d2)

d3 = {'c':3}
d3['a'] = 1
d3['b'] = 2

d4 = {'c':3}
d4['b'] = 2
d4['a'] = 1

# print(d3 == d4)


print(datetime.time(11,43,0))
print(datetime.date.today())
