
#En enkel molekyl kan beskrivas med ett atomnamn, eventuellt följt av antalet atomer, till exempel Xe, H2 eller Cr12.
#
#      <molekyl> ::= <atom> | <atom><num>
#      <atom>  ::= <LETTER> | <LETTER><letter>
#      <LETTER>::= A | B | C | ... | Z
#      <letter>::= a | b | c | ... | z
#      <num>   ::= 2 | 3 | 4 | ...
#
#För varje inmatad rad ska programmet skriva ut ett omdöme,
#
# "Formeln är syntaktiskt korrekt"
# "Saknad stor bokstav vid radslutet"
# "För litet tal vid radslutet"  
# 
# följt av en utskrift av den del av inmatningen som är kvar efter det tecken där felet påträffades.

#-----------------------------------------------------------------------------------------------------------------------------

#Skriv funktionshuvud för fem funktioner, en för varje regel i syntaxen ovan. Funktionskroppen ska fyllas i senare, i punkt 5.

#Gör en kopia av din LinkedQueue från labb 2, och lägg till metoden peek() som tittar på nästa värde i kön utan att plocka ut det.

#Gör ett eget särfall Syntaxfel som är subklass till (ärver från) Exception.

#Skriv ett testprogram med unittest som ska kontrollera att dina funktioner fungerar som avsett. Se exempel från syntaxföreläsningen. 
#T ex kan ett test vara att kön innehåller en syntaktiskt korrekt molekyl, som A -> a -> 5 (OBS! De fem funktionerna ska skrivas i nästa punkt.)

#Lägg till kod i de fem funktionerna som kontrollerar syntaxen. 
# Om en funktion upptäcker ett fel, tex Saknad stor bokstav eller För litet tal vid radslutet ska den göra raise Syntaxfel(felmeddelande). 
# Om allt gått bra gör funktionen inget.

#Provkör med ditt testprogram.

#-----------------------------------------------------------------------------------------------------------------------------
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
    elif q.peek() == ".":
        q.dequeue()
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
    elemnt = q.dequeue()
    if elemnt in list(string.ascii_uppercase):
        return elemnt
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

    try:
        readMolecule(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        error_message = f"{fel.args[0]}"
        if "För litet tal vid radslutet" in error_message:
            print(error_message)
        else:
            error_message = f"{fel} {q}"
            print(error_message.rstrip("None"))
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