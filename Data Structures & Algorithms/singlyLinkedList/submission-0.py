class LinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.n = None
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        node = self.head
        if (node == None):
            return -1
        for i in range(index):
            node = node.n
            if (node == None):
                return -1
        return node.val
            

    def insertHead(self, val: int) -> None:
        nodey = self.head
        self.head = self.Node(val)
        self.head.n = nodey


    def insertTail(self, val: int) -> None:
        node = self.head
        if (node == None):
            self.insertHead(val)
            return
        while node.n:
            node = node.n
        node.n = self.Node(val)

    def remove(self, index: int) -> bool:
        node = self.head
        oldNode = None
        if (node == None):
            return False
        for i in range(index):
            oldNode = node
            node = node.n
            if (node == None):
                return False
        if node.n and node != self.head:
            oldNode.n = node.n
        elif node == self.head:
            self.head = node.n
        return True

    def getValues(self) -> List[int]:
        a = []
        node = self.head
        if (node == None):
            return a
        a.append(node.val)
        while node.n:
            node = node.n
            a.append(node.val)
        return a
        
