import re


string = 'this time Im gonna search in this string as a test searching this'


a = re.search('search',string)
print(a)
print(a.span())
print(a.start())
print(a.end())
print(a.group())

pattern = re.compile('this')

b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(b)
print(c)
print(d)


