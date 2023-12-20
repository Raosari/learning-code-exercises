class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.lenght = 0
    
    def Insert(self,index,value):
        if index == 0:
            self.lenght += 1
            return self.InsertAtBegining(value)
        elif index == self.lenght:
            self.lenght += 1
            return self.Append(value)
        elif index > self.lenght:
            return print(f"No se puede insertar {value} en el index {index}, ya que supera el largo de la cadena")

        NewNode = Node(value)
        leader = self.Traverse(index-1)
        holdPointer = leader.next
        leader.next = NewNode
        NewNode.next = holdPointer
        self.lenght += 1
        return self.Imprime()

    def Traverse(self,index):
      counter = 0
      currentNode = self.head
      while counter != index:
        currentNode = currentNode.next
        counter += 1
      return currentNode

    def Imprime(self):
        elementos = []
        currentNode = self.head
        while (currentNode.next is not None):
          elementos.append(currentNode.value)
          currentNode = currentNode.next
        elementos.append(currentNode.value)
        print(elementos)
    
    def InsertAtBegining(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:   
            new_node.next = self.head
            self.head = new_node
            self.lenght += 1
        return self.Imprime()

    def Append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:  
            self.tail.next = new_node
            self.tail = new_node
            self.lenght += 1
        return self.Imprime()

    def SizeOfLinkedList(self):
        print(f"Linked list {self} contiene {self.lenght} elementos")
        return self.lenght

NewLinkedlist = LinkedList()

NewLinkedlist.InsertAtBegining(1)
NewLinkedlist.Append(2)
NewLinkedlist.InsertAtBegining(3)
NewLinkedlist.InsertAtBegining(3)
NewLinkedlist.Append(2)
