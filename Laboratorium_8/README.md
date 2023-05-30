## Molecular Formulas Checker

This program checks whether an input molecule follows a specific syntax. The syntax rules are as follows:

```
<molecule> ::= <atom> | <atom><number>
<atom>     ::= <LETTER> | <LETTER><letter>
<LETTER>   ::= A | B | C | ... | Z
<letter>   ::= a | b | c | ... | z
<number>   ::= 2 | 3 | 4 | ...
```

For each input line, the program will print a verdict: either "Formula is syntactically correct" or one of the error messages: "Missing uppercase letter at the end of the line" or "Too small number at the end of the line." It will also print the remaining part of the input after the error position.

Valid input examples:

```
H2                      Formula is syntactically correct
P21                     Formula is syntactically correct
Ag3                     Formula is syntactically correct
Fe12                    Formula is syntactically correct
Xx5                     Formula is syntactically correct
H10100                  Formula is syntactically correct
```

Invalid input examples:

```
a                       Missing uppercase letter at the end of the line: a
cr12                    Missing uppercase letter at the end of the line: cr12
8                       Missing uppercase letter at the end of the line: 8
Cr0                     Too small number at the end of the line: Cr0
Pb1                     Too small number at the end of the line: Pb1
H01011                  Too small number at the end of the line: H01011
```

The implementation should include the following steps:

1. Write function headers for five functions, each corresponding to a syntax rule mentioned above. The function bodies will be filled in later.
2. Create a copy of the LinkedQueue class from lab 2 and add a `peek()` method that looks at the next value in the queue without removing it.
3. Define a custom exception class called `SyntaxError`, which subclasses from the built-in `Exception`.
4. Write a test program using `unittest` to ensure that your functions work as intended. The test cases can include checking if the queue contains a syntactically correct molecule, such as A -> a -> 5.
5. Implement the five functions to check the syntax. If a function detects an error, such as a missing uppercase letter or a too small number, it should raise a `SyntaxError` with an appropriate error message. If everything is fine, the function does nothing.
6. Test your program with the test program you created.
7. Go to Kattis and make sure your program passes all the test cases.
