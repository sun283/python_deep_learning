# [Linked List]
# Every node has 2 parts.
# data and a pointer to the next node
# first node = root node
# attributes
# - root : pointer to the beginning of the list
# - size : number of nodes in list
# operations:
# - find(data)
# - add(data)
# - remove(data)
# - print_list()

# Node Class
# Node class has a constructor that sets the data passed in, and optionally can set the next_node and prev_node
# It also has a str method to give a string representation for printing.
# Note that prev_node is only used for Doubly Linked LIsts.

# class Node:
#     def __init__(self, d, n=None, p=None):
#         self.data = d
#         self.next_node = n
#         ## in a standard linked list doesn't need previous node
#         self.prev_node = p
#     def __str__(self):
#         return ('('+str(self.data)+')')

# LinkedList Class
# A LinkedList object has two attributes : a root node that defaults to None, 
# and 
# Add: method receives a piece of data, creates a new Node, setting the root a
# changes the LL's root pointer to the new node, and increments size.
# Find: iterates through the nodes until it finds the data passed in. 
# If it finds the data, it will return it, otherwise return None.
# Remove: needs pointers to this_node and prev_node.
# If it finds the data, it needs to check if it is in the root node(prev_node is None)
# before deciding how to bypass the deleted node.
# Print_list: iterates the list and prints each node.

class LinkedListNotWorking:
    def __init__(self, r=None):
        self.roof = r
        self.size = 0
    # set new node as the root, previous root node will be the next node of the new node
    # inserting node at the very beginning of the list
    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None
    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None: # data is in non-root
                    prev_node.next_node = this_node.next_node
                else: # data is in root node
                    self.root = this_node.next_node
                self.size -= 1
                return True # data removed
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False # data not found
    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end ='->')
            this_node = this_node.next_node
        print('None')

# Test code
myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.print_list()
# (12)->(8)->(5)->None
# print('size='+str(myList.size))
# size=3
myList.remove(8)
# print('size='+str(myList.size))
# size=2
# print(myList.find(5))
# 5
# print(myList.root)
# (12)
#---------------------------------------------
# Singly Linked List 
class Node:
    def __init__(self, data, next=None):
        self.data = data # 데이터 값
        self.next = next # 다음 노드를 가리키는 포인터

class LinkedList:
    def __init__(self, data):
        self.head = Node(data) # 첫 번째 노드 지정
    
    def add(self, data):
        if self.head == '': # 첫 번째 노드가 없을 경우
            self.head = Node(data)
        else:
            node = self.head
            while node.next: # 다음 노드가 있으면 node를 계속 갱신
                node = node.next
            node.next = Node(data) # 다음 node가 없어서 while문을 빠져나오면 node 추가
    
    def describe(self): # LinkedList에 존재하는 요소들을 print
        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    def delete(self, data):
        if self.head == '': # 첫 번째 node가 없을 경우
            print('there is no existing node')
            return
        if self.head.data == data: # 삭제할 data가 첫 번째 노드의 데이터
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next: # 삭제할 data를 찾지 못하면 다음 node로 넘어감
                if node.next.data == data: # 삭제할 data를 찾았을 때
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return 
                else: # 일치하는 data를 찾지 못하면 다음 노드를 가리킴
                    node = node.next
    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data: # 검색한 node와 일치하면 반환
                return node
            else:
                node = node.next # 검색한 node와 다르면 다음 노드를 가리킴
            
# Doubly List
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        
    def insert(self, data):
        if self.head == None: # 첫 번째 노드가 없을 경우 생성
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next: # 가장 마지막 노드를 찾아 연결
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new
            
    def describe(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    def search_from_head(self, data): #첫 번째 노드부터 순차적으로 탐색
        if self.head == None:
            return False
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False
    def search_from_tail(self, data): # 마지막 노드부터 순차적으로 탐색
        if self.head == None:
            return False
        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False
    def insert_before(self, data, before_data): #data를 before_data 앞에 삽입
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.tail # 마지막 노드부터 탐색
            while node.data != before_data:
                node = node.prev
                if node == None: # 찾는 노드가 없을 경우 False
                    return False
            new = Node(data) #입력 받은 값으로 새 노드 생성
            if node.prev != None: # 찾은 노드가 첫 번쨰 노드가 아닐 경우
                before_new = node.prev # 찾은 노드의 앞에 있는 노드(before_new)
                before_new.next = new # before_new <> new <> node 순으로 연결
                new.prev = before_new
                new.next = node
                node.prev = new
            else: # 찾은 노드가 첫번째 노드일 경우, 양방향 연결 후 head도 번경
                new.next = node
                node.prev = new
                self.head = new
            return True
        
    def insert_after(self, data, after_data): # 데이터를 after_data다음에 삽입
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.head # 첫 번째 노드부터 탐색
            while node.data != after_data:
                node = node.next
                if node == None: # 찾는 노드가 없을 경우 False
                    return False
            new = Node(data) #입력 받은 값(data)으로 새 노드 생성
            if node.next != None: # 찾은 노드가 마지막 노드가 아닐 경우
                after_new = node.next # 찾은 노드의 뒤에 있는 노드
                after_new.prev = new # node <> new <> after_new순으로 연결
                new.next = after_new
                new.prev = node
                node.next = new
            else: # 찾은 노드가 마지막 노드일 경우, 양방향 연결 후 tail도 변경
                new.prev = node
                node.next = new
                self.tail = new
            return True


            
                
            
                    
            
        
            