class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:

    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head =new_node
        self.tail = new_node
        self.length +=1

    
    def print_nodes(self):
        temp = self.head

        while temp:
            print(temp.value, end="--->")
            temp = temp.next
