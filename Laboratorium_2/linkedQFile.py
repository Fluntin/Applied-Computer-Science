class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None
    
    def __str__(self):
        return str(self.data)

class LinkedQ:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def print (self):
        temp = self.head
 
        while (temp):
            print(temp.data)
            temp=temp.next
         
    def size(self):
        if self.isEmpty():
            return 0
        else:
            counter = 1
            temp = self.tail
            while temp.next != None:
                counter += 1
                temp= temp.next 
            return counter
        
    def isEmpty(self):
        if self.tail!=None:
            return False
        else:
            return True
    
    def enqueue(self, card):
        newNode = Node (card)
        
        if self.head==None:
            self.head=newNode
            self.tail=newNode
            
        else:
            newNode.next=self.tail
            self.tail=newNode
            
            
    def dequeue(self):
        if self.isEmpty():
            return None
        elif self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            return data
        else:
            data = self.head.data
            temp = self.tail
            while temp.next != self.head:
                temp = temp.next

            self.head = temp
            temp.next == None
            return data