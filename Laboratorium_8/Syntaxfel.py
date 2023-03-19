
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
        raise Syntaxfel("Saknad stor bokstav")
    letter = q.dequeue()
    if letter in list(string.ascii_uppercase):
        return letter
    raise Syntaxfel("Saknad stor bokstav")
    
#-----------------------------------------------------------------------------------------------------------------------------
#Rule 4: <letter>::= a | b | c | ... | z
def readletter(q):
    letter = q.dequeue()
    return
    
#-----------------------------------------------------------------------------------------------------------------------------
#Rule 5: <num> ::= 2 | 3 | 4 | ...
def readNumber(q):
    number = q.dequeue()
    if int(number) > 1:
        return
    raise Syntaxfel("För litet tal")

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
        return "Formeln är syntatiskt korrekt"
    except Syntaxfel as fel:
        return str(fel)

#-----------------------------------------------------------------------------------------------------------------------------
def main():
    molecule = input("Skriv en molekyl: ")
    result = checkStructure(molecule)
    print(result)

#----------------------------------------------------------------------------------------------------------------------------- 
if __name__ == "__main__":
    main()