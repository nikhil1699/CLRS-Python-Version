class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(4)
head.next = Node(6)
head.next.next = Node(11)
head.next.next.next = Node(2)

def traverse(head):
    current = head
    while current != None:
        print(current.data)
        current = current.next

def search_element(head,target):
    pos = 0
    if head.data == target:
        return pos
    else:
        current = head
        while current != None:
            if current.data==target:
                return pos
            pos+=1
            current = current.next

def insert_front(head,data):
    new_node = Node(data)
    if head == None:
        head = new_node
        return head
    else:
        new_node.next = head
        return new_node


def insert_at_end(head,data):
    new_node = Node(data)
    if head==None:
        return new_node
    else:
        current = head
        while current.next != None:
            current = current.next
        current.next = new_node
    return head

def insert_at_given(head,data,position):
    current = head
    pos = 1
    while pos != position:
        current = current.next
        pos+=1
    temp = current.next
    new_node = Node(data)
    current.next = new_node
    new_node.next = temp
    return head

def delete_front(head):
    if head.next:
        head = head.next
    return head
def delete_end(head):
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head

def delete_at_pos(head,data,position):
    current = head
    pos = 1
    while pos != position-1:
        current = current.next
        pos+=1
    temp = current.next.next
    current.next = None
    current.next = temp
    return head


def reverse_linked_list(head):
    current = head
    prev = None
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev


traverse(head)
print(search_element(head,11))