class StackList:
    def __init__(self) -> None:
        self.array = []

    def peek(self):
        return self.array[len(self.array)-1]

    def push(self,value):
        return self.array.append(value)

    def pop(self):
        self.array.pop()

    def printStack(self):
        List1 = [element for element in self.array]
        return List1

Stack = StackList()

