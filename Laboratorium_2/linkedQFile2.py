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
            x = self.tail
            while x.next != None:
                counter += 1
                x= x.next 
            return counter
       # temp = self.head
       # count=0
       # while (temp):
           # count+=1
            #temp=temp.next
       # return (count)
        
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
            y = self.tail
            while y.next != self.head:
                y = y.next

            self.head = y 
            y.next == None
            return data
        #data=self.head.data
        #self.head=self.head.next
        #return(data)