
# class Node:
#     def __init__(self, data):
#         self.data = data
#         from typing import Optional
#         self.next: Optional[Node] = None  # nothing after it yet


# class LinkedList:
#     def __init__(self):
#         self.head = None  # start is empty

#     # Insert at the end
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node

#     # Print the list
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# ll = LinkedList()
# ll.append(10)
# ll.append(20)
# ll.append(30)

# ll.display()


##--------------------------------------

from typing import Optional
class createnode:
    def __init__(self,data) -> None:
        self.data = data
        # self.next : Optional[createnode] = None
        self.next  = None

class linkedlist:
    def __init__(self) -> None:
        self.head = None

    def insert(self,value):
        newnode = createnode(value)

        if self.head is None:
            self.head = newnode
            return
        current = self.head

        while current.next is not None:
            current = current.next
        current.next = newnode


    def display(self):
        current = self.head
        while current is not None:
            print(current.data,end="--->")
            current = current.next
        print('None')

# Example usage
ll = linkedlist()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.display()


