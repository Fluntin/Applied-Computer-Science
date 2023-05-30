## Molecular Formula Structure and Weight Calculator

This program reads molecular formulas, performs syntax checking, and then builds a tree structure representing the formula. It also calculates the weight of the molecule and displays the molecular structure using a graphical representation.

### Preparation: Drawing Syntax Trees
Refer to the syntax from the previous lab and draw syntax trees for the following molecules:

- O
- CO2
- (CH3)2(CH2)4

### Task
This program extends the functionality of the previous lab. It performs formula checking as before and then constructs a tree structure representing the formula. The program displays the molecule and its structure. On the screen, it may look like this (user input in bold):

Molecule: Si(C3(COOH)2)4(H2O)7
Molecule:

In the molecule window, the program draws the formula structure, similar to a molecular tree diagram.

Let your program build a molecular tree
You need to complete the formula checking program to simultaneously build a tree structure as described above. Note that this is not a binary tree with left and right pointers, but a general tree with next and down pointers.

Each box in the tree corresponds to an object:

```python
class Node:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None
```

The `read_group()` function first creates an empty node with:

```python
node = Node()
```

It then calls `read_atom()` and `read_num()` to set the correct values for `atom` and `num`. If it is a group within parentheses, the `read_group()` call to `read_mol()` should return a sub-molecule that is assigned to `node.down`.

When `read_group()` is done, it returns the `node` to the `mol = read_group()` call, which is the first call in `read_mol()`. You need to determine what to do with `mol.next`. Finally, `read_mol()` returns the complete structure to `read_formula()`, which returns it to the main program's call:

```python
mol = read_formula()
```

where `mol` points to the top-left of the syntax tree.

Drawing the Molecular Structure
The main program should now draw the completed molecule structure. Use the `MolGraphics` class from `molgraphics.py`. Create an object of the `MolGraphics` class:

```python
mg = MolGraphics()
```

Then, use:

```python
mg.show(mol)
```

to display the molecular structure in a separate window. The drawing should be recursive, and you need to come up with the recursive logic yourself. If you're stuck, you can refer to the `molgraphics.py` code. To prevent the program from closing immediately, use a loop for entering multiple formulas.

Test program for MolGraphics: `labb10exempel.py`

Molecular Weight Calculation
The molecular weight should be calculated recursively using the `weight(mol)` function. First, formulate a recursive approach for calculating the weight and then implement it. The program should display the weight of the molecule in the terminal window.

Tip: The `hashtest.py` test program from the previous hashtable lab contains all atomic weights.
