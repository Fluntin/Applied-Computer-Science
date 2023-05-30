# Binary Search Tree Program

The theme of this program is binary search trees.

The first task is to write a class for binary search trees.
The second task is to build a search tree from a file containing Swedish words. All duplicates should be printed.
The third task is to check the words in an English text against the Swedish search tree. If there are any apparent Swedish words, they should be printed, but only the first occurrence of each Swedish word. (To keep track of the found words, they can be stored in a search tree.)

## Experimenting with Binary Trees

Visit Liang's Binary Tree Animation [Links to an external site](https://www.cs.usfca.edu/~galles/visualization/BST.html) and perform the following steps:

1. Create a balanced binary tree with seven nodes.
2. Print the tree in inorder.
3. Print the tree in preorder.
4. Print the tree in postorder.

## First Task: Implementing a Class for Binary Search Trees

Now, you will implement a binary search tree as a class.

First, consider an abstract binary search tree. Since Python can compare words (based on alphabetical order), you can store words in the tree as follows:

```python
swedish = Bintree()               # Create a tree object
swedish.put("gurka")              # Insert "gurka" into the tree

# ...

if "gurka" in swedish:            # Check if "gurka" is in the tree
    # ...                         # (The 'in' operator calls the __contains__ method,
                                  # which you will implement in your Bintree class)
     
swedish.write()                   # Write all the words in the tree in alphabetical order
```

The Bintree class should have the following methods:

- `put(x)`: Inserts `x` into the tree.
- `__contains__(x)`: Returns `True` if `x` is in the tree, `False` otherwise.
- `write()`: Writes the tree in inorder.

Here is what the methods in the class should look like:

```python
class Bintree:
    def __init__(self):
        self.root = None

    def put(self, newvalue):
        # Inserts newvalue into the tree
        self.root = putta(self.root, newvalue)

    def __contains__(self, value):
        # Returns True if value is in the tree, False otherwise
        return finns(self.root, value)

    def write(self):
        # Writes the tree in inorder
        skriv(self.root)
        print("\n")
```

In the `bintreeFile.py` file, you should define three helper functions: `putta`, `finns`, and `skriv`. When the tree's `put("gurka")` method is called, the tree sends its root pointer and the new word to the `putta` function, which ensures that a new node is created in the correct position. The same applies to the other function calls.

The tree should store only one copy of each object that is inserted.

The `bintreeFile.py` file also includes a `Node` class that contains a value and two pointers: `left` and `right`.


## Submitting the Program to Kattis

Save the test program below as `main.py`.
Test it.
Log in to Kattis and submit both your `bintreeFile.py` class and the `main.py` test program. The problem is called "soktradi Kattis".

```python

from bintreeFile import Bintree

def makeTree():
    tree = Bintree()
    data = input().strip()
    while data != "#":
        tree.put(data)
        data = input().strip()
    return tree

def searches(tree):
    findme = input().strip()
    while findme != "#":
        if findme in tree:
            print(findme, "found")
        else:
            print(findme, "not found")
        findme = input().strip()

def main():
    tree = makeTree()
    searches(tree)

main()
```

# Second Task: Building Trees and Printing Duplicates

In this task, you will read one word at a time from the file `word3.txt` and insert it into your binary search tree. Duplicate words should be printed.

```python
from bintreeFile import Bintree

swedish = Bintree()
with open("word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # One three-letter word per line
        if ordet in swedish:
            print(ordet, end=" ") 
        else:
            swedish.put(ordet)             # Insert into the search tree
print("\n")
```

If you have implemented it correctly, the printed duplicate words will form an important message.

# Third Task: Two Binary Search Trees with Word Lists

Now that you have a search tree with all Swedish three-letter words, you can quickly check if a given word is included. Your task is to read the file `engelska.txt` word by word and insert the words into another search tree. However, you don't want to print duplicate words. First, check if the word already exists using:

```python
if word in english:
```

If the word already exists, do nothing. However, if it is a new word, also check if it happens to be a Swedish word. If it is, print it on the screen.

If you have implemented it correctly, the printed words will form another secret message!
