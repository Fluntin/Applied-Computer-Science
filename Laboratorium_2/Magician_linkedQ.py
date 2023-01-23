from linkedQFile import LinkedQ

if __name__ == "__main__":
    
    deck=LinkedQ()
    
    while deck.size()<5:
        deck.enqueue(int(input()))
        print(deck.size())

    
    count=0
    while deck.isEmpty() == False:

        card=deck.dequeue()
        count+=1
        
        if count%2 !=0:
            deck.enqueue(card)
        else:
            print(card)