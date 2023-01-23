
#https://www.openbookproject.net/thinkcs/python/english2e/ch18.html

class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=None
    
    def __str__(self):
        return str(self.value)

class LinkedQ:
    def __init__(self):
        self.first=None
        self.last=None
    
    
    # https://www.geeksforgeeks.org/find-length-of-a-linked-list-iterative-and-recursive/    
    
    def size(self):
        temp = self.first
        count=0
        while (temp):
            count=+1
            temp=temp.next
        return (count)
        
        
    def isEmpty(self):
        if self.last!=None:
            return False
        else:
            return True
    
    def enqueue(self, card):
        if self.first==None:
            self.first=Node(card)
            self.last=Node(card)
        else:
            new_node=Node(card)
            new_node.next = self.first
            self.first=new_node
            
    def dequeue(self):
        if self.first==self.last:
            value=self.first.value
            self.first=None
            self.last=None
            return(value)
        
        elif self.first.next==self.last:
            value=self.last.value
            self.last=self.first
            return(value)
        else:
            element=self.rekursive_last(self.first)
            return(element.value)
    
    def rekursive_last(self, node):
        if node.next.next.next==None:
            self.last=node.next
            value=node.next.next
            node.next.next=None
            return(value)
        else:
            return self.rekursive_last(node.next)
        

    
    
        
        
    

    
        
        
        
        