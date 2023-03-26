# Din uppgift är att utföra en syntaxanalys på indata.
# Du ska läsa in en sträng från standard input och sedan tala om ifall formeln är syntaktiskt korrekt eller inte.
# Om den inte är korrekt ska du även skriva ut vad som är fel och var i formeln felet uppstod.
# Till din hjälp får du nedan en BNF-syntax för molekylformler och en lista med atomer.
# Observera att alla atomer som finns med i listan räknas som korrekta.
# Atomer som inte finns med i periodiska systemet räknas som inkorrekta men du behöver inte implementera alla atomer.
# Använd lämpligen rekursiv medåkning.
# BNF-syntax
# <formel>::= <mol>
# <mol>   ::= <group> | <group><mol>
# <group> ::= <atom> |<atom><num> | (<mol>) <num>
# <atom>  ::= <LETTER> | <LETTER><letter>
# <LETTER>::= A | B | C | ... | Z
# <letter>::= a | b | c | ... | z
# <num>   ::= 2 | 3 | 4 | ...
# H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr
# Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd
# In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf
# Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm
# Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv
# Programmet ska läsa in en eller flera rader från standard input.
# Varje rad ska representera en (korrekt eller inkorrekt) formel.
# Inläsningen ska avslutas då tecknet hittas.
# Na                     Formeln är syntaktiskt korrekt
# H2O                    Formeln är syntaktiskt korrekt
# Si(C3(COOH)2)4(H2O)7   Formeln är syntaktiskt korrekt
# Na332                  Formeln är syntaktiskt korrekt
# C(Xx4)5                Okänd atom vid radslutet 4)5 -> X
# C(OH4)C                Saknad siffra vid radslutet C -> X
# C(OH4C                 Saknad högerparentes vid radslutet -> X
# H2O)Fe                 Felaktig gruppstart vid radslutet )Fe -> X
# H0                     För litet tal vid radslutet -> X
# H1C                    För litet tal vid radslutet C -> X
# H02C                   För litet tal vid radslutet 2C -> X
# Nacl                   Saknad stor bokstav vid radslutet cl -> X
# a                      Saknad stor bokstav vid radslutet a  -> X
# (Cl)2)3                Felaktig gruppstart vid radslutet )3  -> X
# )                      Felaktig gruppstart vid radslutet )  -> X
# 2                      Felaktig gruppstart vid radslutet 2  -> X
#Ditt program ska läsa formeln tecken för tecken och med rekursiv medåkning kolla syntaxen.
#Rekursiv medåkning innebär att huvudprogrammet först gör anropet
#readformel(), varefter readformel() anropar readmol() som anropar readgroup() och sedan eventuellt sej själv
#(men inte om inmatningen är slut eller om den just kommit tillbaka från ett parentesuttryck).
#Funktionen readgroup() anropar antingen readatom() eller läser en parentes och anropar readmol() etc - allt enligt grammatiken.
#När ett syntaxbrott upptäcks genereras en exception (raise Syntaxfel("Saknad högerparentes")) som fångas i huvudprogrammet och där skrivs hela resten av indataraden ut.
#Man måste ofta tjuvtitta på nästa tecken i kön (med peek()) för att veta vilken gren man ska följa i syntaxträdet
from LinkedQueue import LinkedQ
import string
#------------------------------------------------------------------------
class Syntaxfel(Exception):
    pass
#------------------------------------------------------------------------
def main():
    molecule_list = []
    molecule = input()
    while molecule != "#":
        molecule_list.append(molecule)
        molecule = input()
    for molecule in molecule_list:
        result = check_structure(molecule)
        if result is not None:
            print(result)
#------------------------------------------------------------------------
def check_structure(molecule):
    q = LinkedQ()
    for element in molecule:
        q.enqueue(element)
    q.enqueue(None)
    try:
        check_formula(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        rest = str(q).replace(" ", "")
        error_message = f"{fel} {rest}".replace("None","").rstrip(" ")
        #error_message = f"{fel} {str(q).replace(" ", "")}".rstrip("None")
        return error_message
#------------------------------------------------------------------------
# Rule 1: <formel>::= <mol>
def check_formula(q):
    if q.peek() is None:
        raise Syntaxfel("Saknad stor bokstav vid radslutet")
    check_mol(q)
    if q.peek() is not None:
        raise Syntaxfel("Felaktig gruppstart vid radslutet")
#------------------------------------------------------------------------X
# Rule 2:  <mol> ::= <group> | <group><mol>
def check_mol(q):
    #"Everything should be treated as a group!"-> philosophy of H.
    if the_golden_rule(q):
        check_group(q)
        check_mol(q)
    return
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def the_golden_rule(q):
    #Since everything is a group this is how you recotnise one...
    # or (q.peek() is not None and  q.peek() in string.ascii_lowercase) or (q.peek() is not None and q.peek() in string.digits)
    #if q.peek() == "(" or (q.peek() is not None and  q.peek() in string.ascii_uppercase)or (q.peek() is not None and  q.peek() in string.ascii_lowercase) or (q.peek() is not None and q.peek() in string.digits):
    if q.peek() != ")" and q.peek() is not None:  #Fail om ")" eller None
        return True
    else:
        return False
 #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#------------------------------------------------------------------------
# Rule 3:  <group> ::= <atom> |<atom><num> | (<mol>) <num>
def check_group(q):
    if q.peek() is None:
        return
    #--------------------------------------------------------------
    # Condition 1:
    # group> ::= (<mol>) <num>
    if q.peek() == "(":
        q.dequeue() # We enter a group.
        if q.peek() == ")":
            raise Syntaxfel("Saknad högerparentes vid radslutet") # Because it's incorrect to have just one element within parenthesis.
        check_mol(q) # If we know that we have more than one element in parentheses, we treat it like a group because everything is a group.
        if q.peek() != ")":
            raise Syntaxfel("Saknad högerparentes vid radslutet") # Because every group that begins with "(" needs to be closed with ")"
        q.dequeue() # Now we know it ended with ")" so we just remove it.
        if not (q.peek() in string.digits):
            raise Syntaxfel("Saknad siffra vid radslutet") # Next, there is no point in having a group within parentheses if we don't have a number after the closing ")".
        check_number(q)
        # If it satisfies all of these conditions, we know that the syntax of the group is correct.
        return
    #--------------------------------------------------------------
    # Condition 2:
    # Again, because everything is treated as a group, we also have to check the case when we don't have parentheses. i.e
    # <group> ::= <atom>
    check_atom(q)
    #--------------------------------------------------------------
    # Condition 3:
    # <group> ::= <atom><number>
    check_number(q)
    return
#------------------------------------------------------------------------
# Rule 3:  <atom>  ::= <LETTER> | <LETTER><letter>
def check_atom(q):
    ATOMS = [ "H", "He", "Li", "Be", "B", "C", "N","F", "O",  "Ne", "Na", "Mg",
            "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr",
            "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br",
            "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd",
            "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La",
            "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er",
            "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au",
            "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
            "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md",
            "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn",
            "Fl", "Lv" ]
    # First we need to clear all of the initial conditions:
    # Condition 1: Atom never starts with a number
    if (q.peek() in string.digits) and (q.peek() is not None):
        raise Syntaxfel("Felaktig gruppstart vid radslutet")
    # Condition 2: Atom has to start with a capital letter
    # <atom>  ::= <LETTER>
    if (not (q.peek() in string.ascii_uppercase)) and (q.peek() is not None):
        raise Syntaxfel("Saknad stor bokstav vid radslutet")
    # Condition 3: Assuming we have a starting capital letter, we have to check if the atom is in the list.
    # <atom>  ::= <LETTER> | <LETTER><letter> has to be in ATOMS
    # Good news, there exist only two-letter atoms so no loops are needed!
    candidate=q.dequeue()
    if ((q.peek() is not None) and (q.peek() in string.ascii_lowercase)):
        next_letter=q.dequeue()
        candidate+=next_letter
    if candidate in ATOMS:
        return
    else:
        raise Syntaxfel("Okänd atom vid radslutet")
#------------------------------------------------------------------------
# Rule 4:  <LETTER>::= A | B | C | ... | Z
def LETTER(candidate):
    if candidate != None and candidate in string.ascii_uppercase :
        return True
    else:
        return False
#------------------------------------------------------------------------
# Rule 5:  <letter>::= a | b | c | ... | z
def letter(candidate):
    if candidate != None and candidate in string.ascii_lowercase:
        return True
    else:
        return False
#------------------------------------------------------------------------
# Rule 6: <num>   ::= 2 | 3 | 4 | ...
def check_number(q):
    if (q.peek() is not None) and (q.peek() in string.digits):
        number = q.dequeue()
        number_digits=number
        if number == "0":
            raise Syntaxfel("För litet tal vid radslutet")
        # Now we  know its not 0
        number=q.peek()
        if q.peek() is not None:
            while number is not None and number in string.digits:
                number_digits += q.dequeue()
                if q.isEmpty() is True:
                    break
                number=q.peek()
        #print(number_digits)
        if number_digits == "1":
            raise Syntaxfel("För litet tal vid radslutet")
#------------------------------------------------------------------------
if __name__ == "__main__":
    main()