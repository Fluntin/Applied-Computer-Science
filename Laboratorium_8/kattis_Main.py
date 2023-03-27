from linkedQueue import LinkedQ
import string

class Syntaxfel(Exception):
    pass

#-----------------------------------------------------------------------------------------------------------------------------
#Rule 1: <molecule> ::= <atom> | <atom><num>

def readMolecule(q):
    readAtom(q)
    if q.peek() == None:
        return
    else:
        readNumber(q)
        #readMolecule(q)

#-----------------------------------------------------------------------------------------------------------------------------
#Rule 2: <atom> ::= <LETTER> | <LETTER><letter>
def readAtom(q):
    readLETTER(q)
    if q.peek() is not None and q.peek() in list(string.ascii_lowercase):
        readletter(q)
    return

#-----------------------------------------------------------------------------------------------------------------------------       
#Rule 3: <LETTER>::= A | B | C | ... | Z
def readLETTER(q):
    if q.peek() is None:
        raise Syntaxfel("Saknad stor bokstav vid radslutet")
    elemnt = q.peek()
    if elemnt in list(string.ascii_uppercase):
        elemnt = q.dequeue()
        return
    raise Syntaxfel("Saknad stor bokstav vid radslutet")
    
#-----------------------------------------------------------------------------------------------------------------------------
#Rule 4: <letter>::= a | b | c | ... | z
def readletter(q):
    elemnt = q.dequeue()
    return
    
#-----------------------------------------------------------------------------------------------------------------------------
#Rule 5: <num> ::= 2 | 3 | 4 | ...
def readNumber(q):
    element = q.dequeue()
    if element.isdigit() and int(element) == 1 and q.peek()==None: # q.peek()==None checks 1 is not the only number
        raise Syntaxfel("För litet tal vid radslutet")
    
    if element.isdigit() and int(element) >= 1: #  If its 1 and there is something after it thats ok, dont start with 0!
        return
    raise Syntaxfel("För litet tal vid radslutet")

#-----------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------
def storeMolecule(molecule):
    q = LinkedQ()
    for element in molecule:
        q.enqueue(element)
        
    q.enqueue(None)
    return q

#-----------------------------------------------------------------------------------------------------------------------------
def checkStructure(molecule):
    
    q = storeMolecule(molecule)

    try:
        readMolecule(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        rest=str(q).replace(" ", "")
        error_message = f"{fel} {rest}".rstrip("None")
        print(error_message)
#-----------------------------------------------------------------------------------------------------------------------------
def main():
    molecules_to_be_checked=list()
    
    candidate = input("")
    while candidate != "#":
        molecules_to_be_checked.append(candidate)
        candidate = input()

    for molecule in molecules_to_be_checked:
        result = checkStructure(molecule)
        
        if result is not None:
            print(result)
            
#----------------------------------------------------------------------------------------------------------------------------- 
if __name__ == "__main__":
    main()