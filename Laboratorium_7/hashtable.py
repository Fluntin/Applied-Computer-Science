
class Node:
#Noder till klassen Hashtable
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.next = None

class Hashtable:

   def __init__(self, size=1000):
      self.size = size
      self.table = [None]*2*size #0.5

   def store(self, key, data):
    #Stoppar in "data" med nyckeln "key" i tabellen."
        hash = self.hashfunction(key)
        if self.table[hash] is None:
            self.table[hash] = Node(key, data)
        else:
            node = self.table[hash]
            while node is not None:
                if node.key == key:
                    node.data = data
                    return
                elif node.next is None:
                    node.next = Node(key, data)
                    return
                else:
                    node = node.next

   def search(self, key):
    #Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        #If "key" inte finns ska vi få en Exception, KeyError
        #else:raise KeyError
        hash = self.hashfunction(key)
        node = self.table[hash]
        
        if node is not None:
            #switch= False
            if node.key == key:
                return node.data
            else:
                #while switch is not True and hash is not None:
                while node is not None:
                    node = node.next
                    if node.key == key:
                        return node.data
        else:
            raise KeyError()

        #while node is not None:
        #    if node.key == key:
        #        return node.data
        #    else:
        #        node = node.next
        #return None

        
   def hashfunction(self, key):
    #key: nyckeln
    #Beräknar hashfunktionen för key"""
    hash_value = 0
    for char in key:
        hash_value = (hash_value * 31 + ord(char)) % self.size
    return hash_value

#djb2 (also known as DJBX2) is a simple non-cryptographic hash function created by Daniel J. Bernstein. 
#It is widely used because of its simplicity, high performance, and low collision rate. 
#The function takes a string as input and produces a 32-bit unsigned integer as output.