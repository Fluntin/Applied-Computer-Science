class Node:

    def __init__(self, data, next = None):

        self.data = data
        self.next = next
        
class Stack:
    def __init__(self):
        self.top = None
        
    def enqueue(self, data):
        if self.top == None:
            new = Node(data)
            self.top = new
        else:
            new = Node(data)
            new.next = self.top
            self.top = new
            
    def dequeue(self):
        top = self.top
        self.top = self.top.next
        return top.data
    
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
        
    def peek(self):
        return self.top.data
    
    def overflow(self):
        print_list = []
        current = self.peek()
        while current.data != ".":
            print_list.append(current.data)
            current = current.next
            output_text = "".join(print_list)
        return output_text