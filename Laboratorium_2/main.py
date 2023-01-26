import sys
#from arrayQFile import ArrayQ
from linkedQFile import LinkedQ

if __name__ == "__main__":
    
    deck=LinkedQ()
    
    indata = sys.stdin.readline()
    indata=indata.split()

    
    for i in range(len(indata)):
        deck.enqueue((indata[i]))

    count=0
    while deck.isEmpty() == False:

        card=deck.dequeue()
        count+=1
        
        if count%2 !=0:
            deck.enqueue(card)
        else:
            print(card, end =" ")