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
        temp = self.head
        count=0
        while (temp):
            count+=1
            temp=temp.next
        return (count)
        
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
            self.tail.next=newNode
            self.tail=newNode
            
    def dequeue(self):
        data=self.head.data
        self.head=self.head.next
        return(data)