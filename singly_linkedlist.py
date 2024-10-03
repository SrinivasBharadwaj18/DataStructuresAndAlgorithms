class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def lengthOfList(self):
        count = 1
        if self.head is None:
            print(count -1)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
                count+=1
            return count
    
    def insertAtEnd(self,node):
        lastnode = self.head
        if self.head is None:
            self.head = node
        else:
            while lastnode.next:
                lastnode = lastnode.next
            lastnode.next = node

    def insertAtBegining(self,newnode):
        if self.head is None:
            self.head = node
        else:
            firstnode = self.head
            self.head = newnode
            newnode.next = firstnode

    def insertAtIndex(self,new_node,index):
        count = 0
        if index == count:
            self.insertAtBegining(new_node) 
        else:
            current_node = self.head
            while count != index:
                previouse_node = current_node
                current_node = current_node.next
                count+=1
            previouse_node.next = new_node
            new_node.next = current_node

    def deleteLastNode(self):
        if self.head is None:
            print("The list is already empty")
        else:
            lastnode = self.head
            while lastnode.next:
                previous_node = lastnode
                lastnode = lastnode.next
            previous_node.next = None
    
    def deletFirstNode(self):
        if self.head is None:
            print("The list is already empty")
        else:
            current_node = self.head
            self.head = current_node.next

    def deleteAtIndex(self,index):
        if index == 0:
            self.deletFirstNode()
        elif index == (self.lengthOfList()) -1:
            self.deleteLastNode()
        else:
            current_node = self.head
            count = 0
            while count != index:
                previous_node = current_node
                current_node = current_node.next
                count +=1
            previous_node.next = current_node.next

    
    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

node = Node("srinivas")
linkedlist = LinkedList()
linkedlist.insertAtEnd(node)
secondnode = Node("saketh")
linkedlist.insertAtEnd(secondnode)
thirdnode = Node("srikar")
linkedlist.insertAtEnd(thirdnode)
new_node = Node("meghana")
kaushik = Node("kaushik")
linkedlist.insertAtBegining(new_node)
linkedlist.insertAtIndex(kaushik,2)
linkedlist.deleteLastNode()
linkedlist.deletFirstNode()
linkedlist.deleteAtIndex(1)
linkedlist.printList()
print(linkedlist.lengthOfList())
