
#https://www.openbookproject.net/thinkcs/python/english2e/ch18.html

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None
    
    def __str__(self):
        return str(self.data)

class LinkedQ:
    def __init__(self):
        self.first=None
        self.last=None
    
    # https://www.geeksforgeeks.org/find-length-of-a-linked-list-iterative-and-recursive/    
    
    # Probaj ovo:
    # https://stackoverflow.com/questions/22600553/python-linked-list-queue
    
    def print (self):
        temp = self.first
 
        while (temp):
            print(temp.data)
            temp=temp.next
        
        
    def size(self):
        temp = self.first
        count=0
        while (temp):
            #print("While körs")
            count+=1
            temp=temp.next
        return (count)
        
        
    def isEmpty(self):
        if self.last!=None:
            return False
        else:
            return True
    
    def enqueue(self, card):
        newNode = Node (card)
        if self.first==None:
            self.first=newNode
            self.last=newNode
        else:
            new_node=Node(card)
            new_node.next = self.first
            self.first=new_node
            
    def dequeue(self):
        if self.first==self.last:
            data=self.first.data
            self.first=None
            self.last=None
            return(data)
        
        elif self.first.next==self.last:
            data=self.last.data
            self.last=self.first
            return(data)
        else:
            element=self.rekursive_last(self.first)
            return(element.data)
    
    def rekursive_last(self, node):
        #!!! Fix
        if node.next.next.next==None:
            self.last=node.next
            data=node.next.next
            node.next.next=None
            return(data)
        else:
            return self.rekursive_last(node.next)
        

    
    
        
        
    

    
        
        
        
        