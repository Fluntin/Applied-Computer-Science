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
            newNode.next = self.head
            self.head=newNode
            
    def dequeue(self):
        # Case 1 -> Only one node in a list.
        if self.head==self.tail:
            data=self.head.data
            self.head=None
            self.tail=None
            return(data)
        
        #Case 2 -> Two nodes is a list.
        elif self.head.next==self.tail:
            data=self.tail.data
            self.tail=self.head
            return(data)
        
        #Case 3 -> More then two nodes in a list.
        else:
            element=self.find_tail(self.head)
            return(element.data)
    
    def find_tail(self, node):

        if node.next.next.next==None:
            self.tail=node.next
            data=node.next.next
            node.next.next=None
            return(data)
        else:
            return self.find_tail(node.next)