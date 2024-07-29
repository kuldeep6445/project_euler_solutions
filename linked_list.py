class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class klist:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

list = klist()
list.head = node(1)
second = node(5)
third = node(2)

list.head.next = second
second.next = third


list.print_list()