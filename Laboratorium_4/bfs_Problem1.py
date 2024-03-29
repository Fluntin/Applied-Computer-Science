from bintreeFile import Bintree
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
# 2.5 -> Create makechildren(startord) function             
def makechildren(startord, svenska, gamla):
    
    #Funktionen makechildren ska systematiskt gå igenom alla sätt att byta ut en bokstav 
    # i startordet (aöt, böt, ..., söö) 
    
    gamla.put(startord)
    temporary=list(startord)
    #Note: Saves as a list of characters...
    
    alphabeth=create_alphabeth()
    
    # Big O -> O(n^2) ???
    index=0   
    for letter in temporary:
        
        for alphabeth_letter in alphabeth:
            temporary.remove(letter)
            temporary.insert(index,alphabeth_letter)
            
            candidate=create_candidate_word(temporary)
 
            #Kolla att det nya ordet finns i ordlistan men inte finns i gamla
            #och i så fall skriva ut det nya ordet på skärmen och lägga in det i gamla.
            
            if (candidate in svenska) and (candidate not in gamla):
                new_word=candidate
                print(new_word)
                gamla.put(new_word)
                
            temporary = list (startord)
        index+=1

#----------------------------------------------------------------------             
def create_candidate_word(temporary):
    word=""
    for element in temporary:
        word=word+element
    return (word)

#---------------------------------------------------------------------- 
def create_alphabeth():
    alphabeth= list(string.ascii_lowercase)
    # God i love Sweden...
    viking_letters= ["å", "ä" ,"ö"]
    for element in viking_letters:
        alphabeth.append(element)
    # Now we have everything...
    return (alphabeth)
                                  
if __name__ == '__main__':
    
    # 1. -> svenska (ordlistan)
    # 2. -> gamla (dumbarnen)
    
    gamla=Bintree()
    svenska=läsa_in_ordlistan()
    
    
    startord, slutord = user_input()
    makechildren (startord, svenska, gamla)

     
