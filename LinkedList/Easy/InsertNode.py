
##--------------------------------------

from typing import Optional
class createnode:
    def __init__(self,data) -> None:
        self.data = data
        self.next : Optional[createnode] = None
        # self.next  = None

class linkedlist:
    def __init__(self) -> None:
        self.head = None

    def insert_at_head(self,value):
        newnode = createnode(value)
        if self.head is None:
            self.head = newnode
        newnode.next = self.head
        self.head = newnode

    def insert_at_position(self,value,pos):
        newnode = createnode(value)

        if self.head is None and pos !=0:
            print('Empty Linkedlist and Position Does not Exist')
        elif pos == 0:
            newnode.next = self.head
            self.head = newnode
            return

        else:
            count = 0
            current = self.head
            while current is not None and count < pos -1:
                count = count + 1
                current = current.next
            
            if current is None:
                print('Position Out Of Bound')
                return
            # newnode.next = current.next
            print(current , '--',current.data ,'--', current.next)

    def insert_at_last(self,value):
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
ll.insert_at_last(10)
ll.insert_at_last(20)
ll.insert_at_last(30)
ll.insert_at_last(40)

ll.insert_at_head(0)
ll.insert_at_head(-1)

ll.insert_at_position(100,2)

ll.display()


