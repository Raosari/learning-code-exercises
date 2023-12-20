class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
    
class StackLL:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.lenght = 0
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking a empty stack")
        return self.top.value
    
    def push(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.top = new_node
            self.bottom = new_node
        else:
            holder = self.top
            self.top = new_node
            self.top.next = holder
        self.lenght += 1
        return self.top
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Trying to pop a empty stack")
        
        elif self.lenght == 1:
            self.bottom = None

        self.top = self.top.next
        self.lenght -= 1

    def __str__(self):
        out = ""
        pointer = self.top
        while pointer is not None:
            out += str(pointer.value) + " -> "
            pointer = pointer.next
        return out
    
    def lenghtStack(self):
        return self.lenght
    
    def isEmpty(self):
        return self.lenght == 0
            
stack = StackLL()
stack.push("udemy")
stack.push("youtube")
stack.push("Halo")

print(stack)

