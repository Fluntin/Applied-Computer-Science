from LinkedQueue import LinkedQ
import string
#-------------------------------------
#New things for lab 10
#-------------------------------------
#By Proff
from molgrafik import *
#-------------------------------------
#By us
from hashtable import *
from Stack_datastructure import *
from Atom_hashed import *
#------------------------------------------------------------------------
# TO DO:

# Read in the chemical formula -> check syntax -> calculate weight.
# I need: LinkedQ, Molgrafik, and ???Hashtable???

# Use class Molgrafik
# ???Make hashtabell in check_structure???
# Create and Atom list to calculate weight
# Create a Weight function
#...

# NOTES:
# We need to save everything we deque -> eqch time we deque it should be saved in a sting?
# To do this i need to add peek_next to LinkedQ

#WHAT I DID:
# Added a peek_next to LinkedQ.
#
#------------------------------------------------------------------------
class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None
# The purpose of the Ruta class is to construct a recursive data structure called a linked list. 
# Each instance of the class represents an atom or a group of atoms in a molecule, 
# and the next and down attributes are used to link these instances together to form a tree-like structure 
# that represents the entire molecule.
#------------------------------------------------------------------------        
class Syntaxfel(Exception):
    pass
#------------------------------------------------------------------------
#def chach_deque(q):
#    formula=str()
#    if q.peek() is None:
#        return 
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
    s = Stack()
    q = LinkedQ()
    for element in molecule:
        q.enqueue(element)
    q.enqueue(None)
    try:
        ruta=check_formula(q) # => Lab 10
        visualize = Molgrafik() # => Lab 10
        visualize.show(ruta) # => Lab 10
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
        raise Syntaxfel("Felaktig gruppstart vid radslutet")
    ruta=check_mol(q) # => Lab 10
    if q.peek() is not None:
        raise Syntaxfel("Felaktig gruppstart vid radslutet")
    return ruta # => Lab 10
#------------------------------------------------------------------------X
# Rule 2:  <mol> ::= <group> | <group><mol>
def check_mol(q):
    ruta = Ruta() # => Lab 10
    #"Everything should be treated as a group!"-> philosophy of H.
    if the_golden_rule(q):
        ruta=check_group(q) # => Lab 10
        ruta.next=check_mol(q) # => Lab 10
    return ruta
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
    ruta = Ruta() # => Lab 10
    if q.peek() is None:
        return
    #--------------------------------------------------------------
    # Condition 1:
    # group> ::= (<mol>) <num>
    if q.peek() == "(":
        q.dequeue() # We enter a group.
        if q.peek() == ")":
            raise Syntaxfel("Felaktig gruppstart vid radslutet") # Because it's incorrect to have just one element within parenthesis.
        # If we know that we have more than one element in parentheses, we treat it like a group because everything is a group.
        ruta.down=check_mol(q)  # => Lab 10
        if q.peek() != ")":
            raise Syntaxfel("Saknad högerparentes vid radslutet") # Because every group that begins with "(" needs to be closed with ")"
        q.dequeue() # Now we know it ended with ")" so we just remove it.
        
        if q.peek() is None: 
            raise Syntaxfel("Saknad siffra vid radslutet") 
            
        if not (q.peek() in string.digits):
            raise Syntaxfel("Saknad siffra vid radslutet") # Next, there is no point in having a group within parentheses if we don't have a number after the closing ")".
        ruta.num=check_number(q) # => Lab 10
        # If it satisfies all of these conditions, we know that the syntax of the group is correct.
        return ruta
    #--------------------------------------------------------------
    # Condition 2:
    # Again, because everything is treated as a group, we also have to check the case when we don't have parentheses. i.e
    # <group> ::= <atom>
    ruta.atom=check_atom(q)
    #--------------------------------------------------------------
    # Condition 3:
    # <group> ::= <atom><number>
    ruta.num=check_number(q)
    return ruta
#------------------------------------------------------------------------
# Rule 3:  <atom>  ::= <LETTER> | <LETTER><letter>
def check_atom(q):
    ruta = Ruta() # => Lab 10
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
        ruta.atom=candidate
        return ruta
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
        if number_digits is not None:# => Lab 10
            return number_digits # => Lab 10
#------------------------------------------------------------------------
if __name__ == "__main__":
    main()