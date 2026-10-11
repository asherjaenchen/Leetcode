# A linked list is a type of list. Unlike a normal list, 
# a linked list contains nodes which are interconnected 
# using links. Each node contains a piece of data and an
# address pointing to the next node. Here is a simple 
# visualization of a linked list:
#
#  [data | address] -> [data | address] -> [data | address]
#
# The first node is called the head. To find an item in the
# list, one must start at the head and traverse the whole
# list via the links.

# Node object class
class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

# Linked list class (driver for node object)
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

    def display(self):
        current = self.head
        
        while current is not None:
            print(current.value)
            current = current.next

# Create a new linked list
numbers = LinkedList()
numbers.append(10)
numbers.append(20)
numbers.append(30)
numbers.display()


