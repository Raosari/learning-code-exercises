class Node:
    def __init__(self,value):
        self.value = value
        self.next = None    

class Queque:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.lenght = 0
        
    def __str__(self) -> str:
        pointer = self.first
        output = ""
        while pointer is not None:
            output += str(pointer.value) + " -> "
            pointer = pointer.next
        output += "None" + f"   && Last item {self.last.value}"
        return output

    def peek(self):
        if self.lenght == 0:
            raise Exception ("Trying to peek an empty queue")
        return print(f"proximo elemento: {self.first.value}")

    def enqueue(self,value):
        new_inline = Node(value)
        if self.is_empty():
            self.first = new_inline
            self.last = new_inline   
        else:
            self.last.next = new_inline
            self.last = new_inline   
        self.lenght += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Trying to deque a empty queque")
        if self.lenght == 1:
            self.last = None
        self.first = self.first.next
        self.lenght -= 1

    def is_empty(self):
        return self.lenght == 0
    
    def return_last(self):
        if self.is_empty():
            raise Exception("Empty queue")
        return print(f"ultimo elemento: {self.last.value}")

new_queue = Queque()
new_queue.enqueue("Ala")
new_queue.enqueue("Beto")
new_queue.dequeue()
new_queue.dequeue()
new_queue.return_last()

print(new_queue)
 



