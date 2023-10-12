class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class SinglyLinkList:
    def __init__(self):
        self.head = None

    def insert(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node

        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next

            last_node.next = new_node

    def printdef(self):
        current_node = self.head
        while True:
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next


singly = SinglyLinkList()
singly.insert('a')
singly.insert('b')
singly.insert('c')
singly.insert('d')
singly.insert('e')
singly.insert('f')

singly.printdef()

