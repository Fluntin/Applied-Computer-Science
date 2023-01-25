from linkedQFile import LinkedQ

deck=LinkedQ()
    
while deck.size()<5:
    deck.enqueue(int(input()))

deck.dequeue