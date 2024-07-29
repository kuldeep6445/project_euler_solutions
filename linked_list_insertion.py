class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class klist:
    def __init__(self):
        self.head = None
        self.counter = 0
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    def push(self,new_data):
        temp = node(new_data)
        temp.next = self.head
        self.head = temp
    def append(self,new_data):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node(new_data)
    def insert(self,index,new_data):
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        new = temp.next
        temp.next = node(new_data)
        temp = temp.next
        temp.next = new
    def search(self,num):
        temp = self.head
        count = 0
        while temp:
            if temp.data==num:
                return count
            count+=1
            temp = temp.next
        return -1
    def count(self,temp,to_find):
        if not temp:
            return self.counter
        if temp.data == to_find:
            self.counter+=1
        return self.count(temp.next,to_find)

        
        

        
list = klist()
list.head = node(1)
second = node(2)
third = node(3)
list.head.next = second
second.next = third
list.push(0)
list.append(4)
list.insert(2,4)
list.print_list()
print(list.count(list.head,4))
