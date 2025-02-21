'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=None

current=node1
while current is not None:
    print(current.data,end="->")
    current=current.next
print("none")



#inserting a new node at the beginning of the node



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=None

head = node1
new_node = Node(0)
new_node.next = head
head = new_node

current= head
while current is not None:
    print(current.data,end="->")
    current=current.next
print("none")



#seaching in the single linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1 = Node(10)
node2 = Node(20)
node3 = Node(40)
node4 = Node(50)


node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=None

head = node1
def search_element(head,target):
    while head is not None:
        if head.data == target:
            return True
    return False
    head=head.next
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1 = Node(10)
node2 = Node(20)
node3 = Node(40)
node4 = Node(50)


node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=None

head = node1
def search_element(head,target):
    while head is not None:
        if head.data == target:
          return True
        head.next=head
    return False
   



p = search_element(head,50)
print(p)

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(40)
node4 = Node(50)
node5 = Node(60)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Set head of the linked list
head = node1

# Search function to find a target in the linked list
def search_element(head, target):
    while head is not None:
        if head.data == target:
            return True
        head = head.next  # Move to the next node
    return False  # If target not found after traversing the entire list

# Example usage
p = search_element(head, 50)
print(p)  # Output: True
