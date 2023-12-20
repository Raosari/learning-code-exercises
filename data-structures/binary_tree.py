class Node:
    def __init__(self,value) -> None:
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self,value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            return self
        else:
            currentNode = self.root
            while True:
                if value < currentNode.value:
                    #left
                    if currentNode.left == None:
                        currentNode.left = newNode
                        return self
                    else:
                        currentNode = currentNode.left

                else:
                    #right
                    if currentNode.right == None:
                        currentNode.right = newNode
                        return self
                    else:
                        currentNode = currentNode.right

    def lookup(self,value):
        if self.root == None:
            return False
        currentNode = self.root
        while currentNode != None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            elif currentNode.value == value:
                return currentNode
        return False
    

myTree = BinaryTree()
myTree.insert(9)
myTree.insert(4)
myTree.insert(6)
myTree.insert(20)
myTree.insert(170)
myTree.insert(15)
myTree.insert(1)
a = myTree.lookup(9)
print(myTree.tree_to_string())
        
        
                    
