from bintreeFile import Bintree
from linkedQFile import LinkedQ
import string

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

class SolutionFound(Exception):
    #def __init__(self, message):
        #self.message = message
    pass 
        
#----------------------------------------------------------------------
# 1. -> Läsa in ordlistan
def läsa_in_ordlistan():
    
    svenska = Bintree()
    
    with open("word3.txt", "r", encoding = "utf-8") as swedishfile:
        for row in swedishfile:
            word = row.strip()   
            if not(word in svenska):
                svenska.put(word)
    return(svenska)

#----------------------------------------------------------------------               
# 2. -> Fråga efter startord och slutord 
def user_input():
    startord = input("Vad är ditt startord?: ")
    slutord = input("Vad är ditt slutord?: ") 
    return (startord, slutord)

#---------------------------------------------------------------------- 
def create_alphabeth():
    alphabeth= list(string.ascii_lowercase)
    # God i love Sweden...
    viking_letters= ["å", "ä" ,"ö"]
    for element in viking_letters:
        alphabeth.append(element)
    # Now we have everything...
    return (alphabeth)

#----------------------------------------------------------------------               
def create_candidate_word(temporary):
    word=""
    for element in temporary:
        word=word+element
    return (word)

#----------------------------------------------------------------------               
# 3. -> Makechildren
# Referens => gamla,svenska 
def makechildren(node, q, slutord, svenska, gamla): #Make_connection skulle kanske vara bättre namn?

    gamla.put(node.word)
    temporary=list(node.word)
    alphabeth=create_alphabeth()
    
    index = 0
    for letter in temporary:
        
        for alphabeth_letter in alphabeth:
            temporary.remove(letter)
            temporary.insert(index,alphabeth_letter)
            
            candidate=create_candidate_word(temporary)
            
            if (candidate in svenska) and (candidate not in gamla):
                
                new_word=candidate
                newNode = ParentNode(new_word, node) #gör en breddenförst sökning
                q.enqueue(newNode)
                gamla.put(new_word)
                if new_word == slutord:
                    end_node = ParentNode(new_word, node)
                    return end_node
                        
            temporary = list(node.word)
        index += 1


def writechain(node):

    if node.parent is not None:  #!!
    
        writechain(node.parent)
        print(node.word)
    if node.parent is None:
        print(node.word)
        return(node)

#----------------------------------------------------------------------
if __name__ == "__main__":

    q = LinkedQ()
    gamla=Bintree()
    svenska=läsa_in_ordlistan()
    
    startord, slutord = user_input()
    startNode = ParentNode(startord)
    q.enqueue(startNode)
    existance_of_path = None

    if startord not in svenska:
        print('Ordet finns inte i ordlistan')
    if slutord not in svenska:
        print('Slutord finns inte i ordlistan')
    while not q.isEmpty() and startord in svenska:
        node = q.dequeue()
        end_node = makechildren(node, q, slutord, svenska, gamla)
        
        try:
            if end_node != None:
                raise SolutionFound

    
        except:
            
            writechain(end_node)