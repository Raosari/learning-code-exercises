
def ReverseLinkedList(self):
    if self.head["next"] == None:
        return self.head
        
    first = self.head
    self.tail = self.head
    second = first["next"]

    while second != None:
        temporal = second["next"]
        second["next"] = first
        first = second
        second = temporal
    self.head["next"] = None
    self.head = first
    return self.head
