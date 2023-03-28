import matplotlib.pyplot as plt

#Redovisning

#Vid redovisningen ska du kunna

#motivera ditt val av hashfunktion, krockhantering och tabellstorlek,
#skissa hashtabellen,
#förklara varför hashning ger snabb sökning,
#berätta hur en unittest-fil är upplagd


class Node:
#Noder till klassen Hashtable
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.next = None

class Hashtable:

   def __init__(self, size=800):
      self.size = size
      self.table = [None]*2*size #0.5
#---------------------------------------------------------------------    
    #  TU SI PROBO IZVIDITI  
   def average_list_length(self):
        total_length = 0
        count = 0
        for node in self.table:
            if node is not None:
                count += 1
            while node is not None:
                total_length += 1
                node = node.next
        return total_length / count
    
   def visualize(self):
        y=list()
        for node in self.table:
            total_length = 0
            while node is not None:
                total_length += 1
                node = node.next
            y.append(total_length)
        
        plt.plot(list(range(1,len(y)+1)), y)
#---------------------------------------------------------------------
   def exists(self, startslot):
        if self.hashlist[startslot] == None:
            return False
        else:
            return True
#---------------------------------------------------------------------

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
        hash_value = (hash_value * 31 + ord(char)) % self.size*2
    return hash_value

#djb2 (also known as DJBX2) is a simple non-cryptographic hash function created by Daniel J. Bernstein. 
#It is widely used because of its simplicity, high performance, and low collision rate. 
#The function takes a string as input and produces a 32-bit unsigned integer as output.