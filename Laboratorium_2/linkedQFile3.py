# Habil Anwari 1/25/2023

class Node:
    
    def __init__(self, value, next_p=None):
        self.value=value
        self.next=next_p
        
class LinkedQ:
    
    def __init__(self):
        self.__first=None
        self.__last=None
        self.__size=0
        
    def enqueue (self,value):
        
        if self.__first==None:
            self.__first=Node(value)
            self.__last=self.__first
            self.__size+=1
            return()
        
        else:
            self.__last.next=Node(value)
            self.__last=self.__last.next
            self.__size+=1
        
    def dequeue (self):
        
        if self.isEmpty():
            print("There is nothing to deque!")
            return()
        
        else:
            temp=self.__first
            self.__first=self.__first.next
            self.__size -=1
            return (temp.value)
    
    def isEmpty(self):
        if self.__first==None:
            return (True)
        else:
            return (False)
        
    def size (self):
        return (self.size)
    
            
        
        