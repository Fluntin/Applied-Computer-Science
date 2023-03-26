
#-----------------------------------------------------------------------------------------------------------------------------
from linkedQueue import LinkedQ
from stackFile import Stack
import string


class Syntaxfel(Exception):
    pass

#Rule : <formel>::= <mol> \n
def readformel(q):
    readMol(q)
    if q.peek() == None:
        return
    

#-----------------------------------------------------------------------------------------------------------------------------
#Rule: <mol>   ::= <group> | <group><mol>

def readMol(q):
    readGroup(q)
    if q.peek() == None:
        return
    readMol(q)
#-----------------------------------------------------------------------------------------------------------------------------
#Rule: <group> ::= <atom> |<atom><num> | (<mol>)<num>
# behöver fixas, problemet ligger i parenteser i parenteser
def readGroup(q):

    if q.peek() is not None and q.peek() in string.ascii_letters:
        readAtom(q)
        if q.peek() is not None and q.peek() in string.digits:
            readNumber(q)
        return
    if q.peek() == '(':
        
        elemnt = q.dequeue()
        s.push(elemnt)
        readMol(q)
    if q.peek() == ')' and s.isEmpty():
        raise Syntaxfel('Felaktig gruppstart vid radslutet')
    if q.peek() == ')' and q.peek() is not s.isEmpty():
        return
    if q.peek() is not None and q.peek() in string.digits:
        readNumber(q)
        return
    raise Syntaxfel('Saknad högerparentes vid radslutet')
    


#-----------------------------------------------------------------------------------------------------------------------------
#Rule : <molecule> ::= <atom> | <atom><num>
"""
def readMolecule(q):
    readAtom(q)
    if q.peek() == None:
        return
    else:
        readNumber(q)
        """

#-----------------------------------------------------------------------------------------------------------------------------
#Rule : <atom> ::= <LETTER> | <LETTER><letter>
def readAtom(q):
    readLETTER(q)
    if q.peek() is not None and q.peek() in list(string.ascii_lowercase):
        readletter(q)
    return

#-----------------------------------------------------------------------------------------------------------------------------       
#Rule : <LETTER>::= A | B | C | ... | Z
def readLETTER(q):
    if q.peek() is None:
        raise Syntaxfel("Saknad stor bokstav vid radslutet")
    elemnt = q.peek()
    if elemnt in list(string.ascii_uppercase):
        elemnt = q.dequeue()
        return elemnt
    raise Syntaxfel("Saknad stor bokstav vid radslutet")
    
#-----------------------------------------------------------------------------------------------------------------------------
#Rule : <letter>::= a | b | c | ... | z
def readletter(q):
    elemnt = q.dequeue()
    return
    
#-----------------------------------------------------------------------------------------------------------------------------
#Rule : <num> ::= 2 | 3 | 4 | ...
def readNumber(q):   
    element = q.dequeue()
    if element.isdigit() and int(element) == 1 and q.peek()==None:
        raise Syntaxfel("För litet tal vid radslutet")
    
    if element.isdigit() and int(element) >= 1:
        return None
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
    s = Stack()
    try:
        readformel(q)
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