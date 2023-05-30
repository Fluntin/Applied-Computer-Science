## Molecular Formula Syntax Checker

This program reads molecular formulas and checks if they are syntactically correct using recursive descent parsing.

### Preparation
1. Read the instructions on Kattis for the problem "Formelkoll".
2. Write a test program using `unittest` for the first set of test data (Sample Input 1/Sample Output 1).
3. Write a test program for the second set of test data (Sample Input 2/Sample Output 2).

### Introduction
Molecular formulas describe the composition of molecules. They can include atoms, parentheses, and numbers, for example, H2O (water) or Ba(NO3)2 (barium nitrate).

### Task
Your task is to perform syntax analysis on the input. You should read a string from standard input and determine whether the formula is syntactically correct or not. If it is incorrect, you should also indicate the specific error and its position within the formula.

You are provided with a BNF syntax for molecular formulas and a list of valid atoms. Note that all atoms in the list are considered correct. (Atoms not included in the periodic table are considered incorrect, but you don't need to implement all atoms). Use recursive descent parsing to implement the solution.

### BNF Syntax
```
<formula>  ::= <mol> \n
<mol>      ::= <group> | <group><mol>
<group>    ::= <atom> | <atom><num> | (<mol>) <num>
<atom>     ::= <LETTER> | <LETTER><letter>
<LETTER>   ::= A | B | C | ... | Z
<letter>   ::= a | b | c | ... | z
<num>      ::= 2 | 3 | 4 | ...
```

Here is a list of atoms:

H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr
Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd
In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf
Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm
Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Fl Lv

### Input
The program reads one or more lines from standard input. Each line represents a (correct or incorrect) formula. The input should be terminated with the '#' character.

### Output
For each line, except the line with '#', the program should indicate whether the formula is syntactically correct or report the encountered error and its position within the formula. If the formula contains multiple errors, only the first error should be reported. Ensure that the output format matches the provided examples.

### Sample Input 1/Sample Output 1
```
Na                     Formula is syntactically correct 
H2O                    Formula is syntactically correct 
Si(C3(COOH)2)4(H2O)7   Formula is syntactically correct 
Na332                  Formula is syntactically correct 
```

### Sample Input 2/Sample Output 2
```
C(Xx4)5    Unknown atom at the end: 4)5
C(OH4)C    Missing number at the end: C
C(OH4C     Missing right parenthesis at the end
H2O)Fe     Invalid group start at the end: )Fe
H0         Too small number at the end
H1C        Too small number at the end: C
H02C       Too small number at the end: 2C
Nacl       Missing uppercase letter at the end: cl
a          Missing uppercase letter at the end: a
(Cl)2)3    Invalid group start at the end: )3
)          Invalid group start at the end: )
2          Invalid group start at the end: 2
```

Your program should read the formula character by character and use recursive descent parsing to check the syntax. Recursive descent parsing means that the main program first calls `read_formula()`, which then calls `read_mol()`, which calls `read_group()`, and potentially calls itself (but not when the input is empty or after returning from a parenthesis expression).

The `read_group()` function either calls `read_atom()` or reads an opening parenthesis and calls `read_mol()` accordingly. When a syntax error is detected, an exception is raised (`raise SyntaxError("Missing right parenthesis")`) and caught in the main program, where the remaining part of the input line is printed.

You may need to peek at the next character in the queue using `peek()` to determine which branch to follow in the syntax tree.

### Testing
Kattis may provide additional test cases, so you should create your own tests to ensure that your program is robust enough to pass them. Add your new tests to the unittest program you created earlier.
