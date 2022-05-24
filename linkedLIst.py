# Node 클래스 선언
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly linked list 클래스 선언
class SignlyLinkedList():
    def __init__(self):
        self.head = None
        self.count = 0
    
    # Add new node at the end of the linked list
    def append(self, node):
        print('head=',self.head)
        print('count=',self.count)
        print('node=',node)
        print('self.head == None :',self.head == None)
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    # Return first index of data in the linked list
    def getdataIndex(self,data):
        curn = self.head
        idx = 0
        while curn:
            if curn.data == data:
                return idx
            curn = curn.next
            idx += 1
        return -1
    

sl = SignlyLinkedList()
sl.append(Node(1))
sl.append(Node(2))
print('sl=',sl.count)