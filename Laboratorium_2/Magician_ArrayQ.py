from ArrayQ import ArrayQ

def test_function():
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("OK")
    else:
        print("FAILED")

if __name__ == '__main__':
    
    test_function()
    
    deck=ArrayQ()
    
    while deck.size()<13:
        deck.enqueue(int(input()))

    
    count=0
    while deck.isEmpty() == False:

        card=deck.dequeue()
        count+=1
        
        if count%2 !=0:
            deck.enqueue(card)
        else:
            print(card)
        
    