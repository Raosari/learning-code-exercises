import reverse_a_linkedList
class LinkedList:
    def __init__(self,value):
      self.head = { "value":value,"next":None}
      self.tail = self.head
      self.lenght = 1
    
    def Append(self,value):
      NewNode = {"value":value,"next":None}
      self.tail["next"] = NewNode
      self.tail = NewNode
      self.lenght += 1
    
    def Prepend(self,value):
      NewNode = {"value":value,"next":None}
      NewNode["next"] = self.head
      self.head = NewNode

    def Insert(self,index,value):
      if index == 0:
        self.lenght += 1
        return self.Prepend(value)
      elif index == self.lenght:
        self.lenght += 1
        return self.Append(value)
      elif index > self.lenght:
        return print(f"No se puede insertar {value} en el index {index}, ya que supera el largo de la cadena")

      NewNode = {"value":value,"next":None}
      leader = self.Traverse(index-1)
      holdPointer = leader["next"]
      leader["next"] = NewNode
      NewNode["next"] = holdPointer
      self.lenght += 1

    def Traverse(self,index):
      counter = 0
      currentNode = self.head
      while counter != index:
        currentNode = currentNode["next"]
        counter += 1
      return currentNode
    
    def Delete(self,index):
      beforeNode = self.Traverse(index-1)
      nodeToRemove = beforeNode["next"]
      beforeNode["next"] = nodeToRemove["next"]  
      self.lenght -= 1

    def Imprime(self):
      elementos = []
      currentNode = self.head
      while (currentNode["next"]):
        elementos.append(currentNode["value"])
        currentNode = currentNode["next"]
      elementos.append(currentNode["value"])
      print(elementos)

lista1 = LinkedList(1)
lista1.Append(2)
lista1.Append(3)
lista1.Append(4)
a= reverse_a_linkedList.ReverseLinkedList(lista1)
print(a)

