import sys
#from ArrayQ import ArrayQ
from linkedQFile import LinkedQ

if __name__ == "__main__":
    
    deck=LinkedQ()
    
    indata = sys.stdin.readline()
    #indata=input()
    indata=indata.split()
    #print("\n")
    #print(indata)
    
    
    for i in range(len(indata)):
    #while deck.size()<5:
        deck.enqueue((indata[i]))

    count=0
    svar=list()
    while deck.isEmpty() == False:

        card=deck.dequeue()
        count+=1
        
        if count%2 !=0:
            deck.enqueue(card)
        else:
            svar.append(card)
            
    
    for element in svar:
        print(element, end =" ")