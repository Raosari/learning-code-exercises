class LinkedList:
    def __init__(self,value):
        self.head = { "value":value,
                   "next":None,
                   "prev":None
        }
      
        self.tail = self.head
        self.lenght = 1
    
    def Append(self,value):
        NewNode = {"value":value,
                 "next":None,
                 "prev":None
        }
        NewNode["prev"] = self.tail
        self.tail["next"] = NewNode
        self.tail = NewNode
        self.lenght += 1
    
    def Prepend(self,value):
        NewNode = {"value":value,
                   "next":None,
                   "prev":None
        }
        
        NewNode["next"] = self.head
        self.head["prev"] = NewNode
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

        NewNode = {"value":value,
                   "next":None,
                   "prev":None}
        
        leader = self.Traverse(index-1)
        follower = leader["next"]
        leader["next"] = NewNode
        NewNode["prev"] = leader
        NewNode["next"] = follower
        follower["prev"] = NewNode     
        self.lenght += 1

    def Traverse(self,index):
        counter = 0
        currentNode = self.head
        while counter != index:
            currentNode = currentNode["next"]
            counter += 1
        return currentNode
    
    def Delete(self,index):
        if index > self.lenght:
            return "No se puede eliminar un index superior al largo de la linkedlist"
        beforeNode = self.Traverse(index - 1)
        afterNode = self.Traverse(index + 1)

        nodeToRemoveNext = beforeNode["next"]
        nodeToRemovePrev = afterNode["prev"]
        
        beforeNode["next"] = nodeToRemoveNext["next"]
        afterNode["prev"] = nodeToRemovePrev["prev"]
        print(self.head)
        print("beforenode", beforeNode)
        print("\nbeforenode next", beforeNode["next"])
        print("\nafter node next", afterNode["next"])
        print("\nafter node prev",afterNode["prev"])
        print("cola", self.tail)
        
        self.lenght -= 1

    def Imprime(self):
        elementos = []
        currentNode = self.head
        while (currentNode["next"]):
            elementos.append(currentNode["value"])
            currentNode = currentNode["next"]
        elementos.append(currentNode["value"])
        print(elementos)




Lista1 = LinkedList(1)
Lista1.Append(2)
Lista1.Append(3)
Lista1.Append(4)

Lista1.Delete(2)


Lista1.Imprime()