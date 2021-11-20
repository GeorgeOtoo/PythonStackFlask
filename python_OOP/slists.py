# create the Node class with the data and the reference to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

# create the linked class and have the methods that will traverse, add and delete items
class TheList:

    # this method creates a nodes instance and assign it to head
    def __init__(self):
        #node = Node(data)
        self.head = None
    
    # this prints and traverse through the linked list
    def printList(self):

        #check if list is empty
        if self.head == None:
            print("Linked List is Empty")
        
        #if not, add nodes
        
        else:
            arr = []
            node = self.head 
            while node != None:
                arr.append(node.data)
                #print(node.data, "-->")
                node = node.nextNode
            print(arr)
    def addBegin(self, data):
        new_node = Node(data)
        new_node.nextNode = self.head
        self.head = new_node

    def addEnd(self, data):
        new_node = Node(data)
        n = self.head

        if self.head == None:
            self.head = new_node

        while n.nextNode != None:
            n = n.nextNode
        n.nextNode = new_node

    def addAfter(self, data, index):
        n = self.head
        while n != None:
            if index == n.data:
                break
            n = n.nextNode
        
        if n == None:
            print("Data is not in the chat")
        else:
            new_node = Node(data)
            new_node.nextNode = n.nextNode
            n.nextNode = new_node

    def addBefore(self, data, index):
        # 4 --> 6 -->9 -->11 -->5 
        # what if you are adding at the begginning 
        n = self.head
        if n.data == index:
            new_node = Node(data)
            new_node.nextNode = n
            self.head = new_node
            return

        # to add before you have to track the prev node
        while n.nextNode != None:
            if n.nextNode.data == index:
                break
            n = n.nextNode
        if n.nextNode == None:
            print("Value cannot be found")
        else:
            new_node = Node(data)
            new_node.nextNode = n.nextNode
            n.nextNode = new_node





linkedList = TheList()
linkedList.addBegin(6)
linkedList.addBegin(7)
linkedList.addBegin(8)
linkedList.addBegin(9)
linkedList.addEnd(5)
linkedList.addAfter(30, 8)
linkedList.addBefore(15, 5)
print(type(linkedList.printList()))


