# class MyGenerator():
#     def __init__(self,last) -> None:
#         self.before = 0
#         self.current = 1
#         self.last = last
#         self.counter = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.counter <= self.last:
#             holder = self.current
#             self.current += self.before
#             self.before = holder
#             self.counter += 1
#             return holder
#         raise StopIteration
# index = 10
# gen = MyGenerator(index)

# for i in gen:
#     print(i)

def fibbonacci_gen(index):
    a = 0
    b = 1
    for _ in range(index):
        yield a
        temp = a
        a = b
        b = temp + b

for i in fibbonacci_gen(10):
    print(i)