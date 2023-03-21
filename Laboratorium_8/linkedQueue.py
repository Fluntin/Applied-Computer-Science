class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedQ:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            s = ""
            temp = self.head
            while temp:
                s += str(temp.data) + " "
                temp = temp.next
            return s.strip()

    def print(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

    def size(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def isEmpty(self):
        if self.tail != None:
            return False
        else:
            return True

    def enqueue(self, item):
        newNode = Node(item)

        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def peek(self):
        if self.head == None:
            return None
        else:
            return self.head.data

    def dequeue(self):
        if self.head == None:
            return None

        val = self.head.data
        self.head = self.head.next

        if self.head == None:
            self.tail = None

        return val