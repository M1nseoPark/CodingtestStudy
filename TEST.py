# 노드 구현
class Node:
    def __init__(self, data, prev=None, next=None):
	self.prev = prev
	self.next = next
	self.data = data


# 이중 연결 리스트 구현
class DoubleLinkedList:
    def __init__(self):
	self.head = None
	self.tail = self.head

    # 연결 리스트가 비어있는 경우 True 리턴
    def empty(self):
	return not bool(self.head)  # head가 None이 아닐 경우 False

    def append(self, data):
	# 연결 리스트가 비어있는 경우
	if self.head is None:
	    self.head = Node(data)
	    self.tail = self.head
	else:
	    node = self.tail  # 연결 리스트의 마지막
	    new_node = Node(data, prev=node)  # node 뒤에 노드 추가
	    node.next = new_node
	    self.tail = new_node

    def appendleft(self, data):
	# 연결 리스트가 비어있는 경우 = append
	if self.head is None:
	    self.head = Node(data)
	    self.tail = self.head
	else:
	    node = self.head  # 연결 리스트의 처음
	    new_node = Node(data, next=node)
	    node.prev = new_node
	    self.head = new_node

    # 임의의 위치의 왼쪽에 노드 추가
    def insertleft(self, next_data, new_data):
	if self.head is None:
	    self.head = Node(new_data)
	    self.tail = self.head
	else:
	    node = self.tail
	    while node.data != next_data:
		node = node.prev
		if node is None:
		    return False

	    prev_node = node.prev
	    new_node = Node(new_data, prev=prev_node, next=node)

	    if prev_node:
		prev_node.next = new_node
	    else:
		self.head = new_node
			
	    node.prev = new_node
	    return True
	
    # 임의의 위치의 오른쪽에 노드 추가
    def insert(self, prev_data, new_data):
	if self.head is None:
	    self.head = Node(new_data)
	    self.tail = self.head
	else:
	    node = self.head
	    while node.data != prev_data:
		node = node.next
		if node is None:
		    return False
			
	    next_node = node.next
	    new_node = Node(new_data, prev=node, next=next_node)
			
	    if next_node:
		next_node.prev = node
	    else:
		self.tail = new_node
			
	    node.next = new_node
	
    def pop(self):
	item = self.tail.data
	self.tail = self.tail.prev
	self.tail.next = None
	return item

    def popleft(self):
	item = self.head.data
	self.head = self.head.next
	self.head.prev = None
	return item

    def __len__(self):
	node = self.head
	cnt = 0
	while node is not None:
	    cnt += 1
	    node = node.next
	return cnt

	    
data = input()
DL = DoubleLinkedList()
idx = len(data)
for i in data:
    DL.append(i)
    
m = int(input())
for _ in range(n):
    command = input().split(' ')

    if command[0] == 'P':
        
    
    
