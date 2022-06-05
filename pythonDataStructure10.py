# Linked List
# - 데이터를 노드의 형태로 저장
# - 노드 = 데이터 + 다음 노드를 가리키는 포인터
# - 선형 데이터 자료 구조
# - Python의 List보다 데이터의 삽입, 삭제가 빠르다
# - 데이터 탐색에 있어서는 List, Tree보다 느리다
# (1) 장정
# - 길이를 동적으로 조절 가능
# - 데이터의 삽입과 삭제가 쉬움
# (2) 단점
# - 임의의 노드에 바로 접근할 수 없음
# - 다음 노드의 위치를 저장하기 위한 추가 공간 필요
# - Cache Locality를 활용해 근접 데이터를 사전에 캐시에 저장하기 어려움
# - 거꾸로 탐색하기 어려움
# 1) Singly Linked List(단일 연결 리스트)
# 삽입
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
    
    # Add new node at the given index
    def insertNodeAtIndex(self, idx, node):
        """
        A node can be added in three ways
        1) At the front of the linked list
        2) At a given index
        3) At the end of the linked list
        """
        curn = self.head
        prevn = None
        cur_i = 0
        
        # (1) Add 0 index
        if idx == 0:
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn
            else:
                self.head = node
