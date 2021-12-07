# linked lists:
# good at insertions and deletions, not the best at reading
# each element in a linked list is called a node
# a node has data, and a pointer (which points to mem address of next node)
# last pointer needs to point to None

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
    def addNode(self):

        pass 

if __name__ =='__main__':
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printList()

