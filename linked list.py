class Node:
    def __init__(self, cargo=None, next=None):
        self.__cargo = cargo
        self.__next = next
    def __str__(self):
        return str(self.cargo)
print(Node("text"))

def AddToFront(self, data):
    if data is None:
        return None
    node = Node(data, self.head)
    self.head = node
    return node

def append(self,data):
    if data is None:
        return None
    node = Node(data)
    if self.head is None:
        self.head = node
        return node
    curr_node = self.head
    while curr_node.next is not None:
        curr_node = curr_node.next
        return node

def find(self,data):
    if data is None:
        return None
    curr_node = self.head
    while curr_node is not None:
        if curr_node.data == data:
            return curr_node
        curr_node = curr_node.next
    return None

def delete(self,data):
    if data is None:
        return None
    if self.head is None:
        return None
    if self.head.data == data:
        self.head = self.head.next
        return
    prev_node = self.head
    curr_node = self.node.next
    while curr_node is not None:
        if curr_node.data == data:
            prev_node.next = curr_node.next
        else:
            prev_node = curr_node
            curr_node = curr_node.next

Mynode = Node