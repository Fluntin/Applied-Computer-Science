from bintreeFile import Bintree
from linkedQFile import LinkedQ
import string

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
# Referens => gamla, svenska
def makechildren(nod, q, slutord, svenska, gamla):

    gamla.put(startord)
    temporary=list(nod)
    alphabeth=create_alphabeth()
    
    index = 0
    for letter in temporary:
        #print(letter)
        #print(temporary)
        
        for alphabeth_letter in alphabeth:
            temporary.remove(letter)
            temporary.insert(index,alphabeth_letter)
            
            candidate=create_candidate_word(temporary)
            
            if (candidate in svenska) and (candidate not in gamla):
                new_word=candidate
                q.enqueue(new_word)
                gamla.put(new_word)
                #gamla.write()
                if new_word == slutord:
                    return new_word
                        
            temporary = list(nod)
        index += 1

#----------------------------------------------------------------------
if __name__ == "__main__":

    q = LinkedQ()
    gamla=Bintree()
    svenska=läsa_in_ordlistan()
    startord,slutord = user_input()
    
    trigger=True

    q.enqueue(startord)
    existance_of_path = None
    
    while not q.isEmpty() and startord in svenska:
        nod = q.dequeue()
        existance_of_path = makechildren(nod, q, slutord, svenska, gamla)
        if existance_of_path != None:
            break
    
    if existance_of_path == None:
        print("Det finns inte en väg till ", slutord)
    else:
        print("Det finns en väg till ", slutord)