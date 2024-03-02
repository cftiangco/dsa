class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_nodes(self):
        current = self.head
        for _ in range(self.length):
            print(current.value)
            current = current.next
    
    def add_node(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
    
    def pop_node(self):

        if self.length == 0:
            raise IndexError("pop from empty linked list")
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:           
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
            self.length -= 1
    



link = LinkedList(1)

link.add_node(2)
link.add_node(3)
link.add_node(4)
link.add_node(5)

link.pop_node()
link.pop_node()

link.print_nodes()