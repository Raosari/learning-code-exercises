class MyGenerator():
    def __init__(self,first,last) -> None:
        self.current = first
        self.last = last

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.last:
            num = self.current
            self.current += 1 
            return num
        raise StopIteration

index = 10
gen = MyGenerator(0,index)

for i in gen:
    print(i)
