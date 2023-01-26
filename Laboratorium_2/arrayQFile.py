import array as arr

class ArrayQ():
    def __init__(self):
        self.deck=arr.array('i', [])

    def isEmpty(self):
        if len (self.deck)!=0:
            return False
        else:
            return True

    def enqueue(self, card):
        self.deck.insert(0,card)

    def dequeue(self):
        return (self.deck.pop())

    def size(self):
        return len(self.deck)