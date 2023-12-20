
class MyArray():
    def __init__(self):
        self.lenght = 0
        self.data = {}

    def get(self,index):
        return self.data[index]

    def push(self,item):
            self.data[self.lenght] = item
            self.lenght += 1
            return self.lenght
    
    def pop(self):
        LastItem = self.data[self.lenght-1]
        del self.data[self.lenght-1]
        self.lenght -= 1
        return LastItem
    
    def delete(self,index):
        deletedItem = self.data[index]
        self.shiftIndex(index)
        return deletedItem
    
    def shiftIndex(self,index):
        for i in range(index,self.lenght-1):
            self.data[i] = self.data[i+1]
        del self.data[self.lenght-1]
        self.lenght -= 1

    def insert():
        pass

Array1 = MyArray()
print(Array1.data)
