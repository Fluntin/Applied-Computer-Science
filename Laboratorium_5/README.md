# Recursive Function and Improved "söt-sur"

## Preliminary Tasks

Here is a recursive function for printing a list:

```python
def print_list(lst):
    if len(lst) > 0:
        print(lst[0])
        print_list(lst[1:])
```

Test the function with the list `[1, 2, 3, 4, 5]`.
Draw stack frames (according to the book, chapter 5.5 and 5.6) to show how recursion works.
Swap the print statement and the recursive call (so that the print statement comes last in the function).
Test it again.
Draw stack frames and explain the result.

## Improve "söt-sur"

The problem with the program from the previous lab is that it only indicates whether a solution exists or not. In order for the program to print all the words on the path between "söt" and "sur", each word needs to be able to point to its parent. We introduce a `ParentNode` class to keep track of both the word and its parent.

```python
class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent
```

The main program should create a `ParentNode` object and add the start word (as the `word` attribute). What is inserted into and removed from the queue is no longer just words but `ParentNode` objects. This means you need to make some changes to the `makechildren` function from the previous lab.

When `makechildren` finds the end word, it should print the entire chain by calling `writechain(end_node)`. The `writechain()` method should be written recursively to output the chain with the end word at the end.

If the queue is emptied without finding a solution, the program should indicate that it is impossible. And when a solution is printed, the program should stop running. One way to achieve this is to define a custom `Exception`:

```python
class SolutionFound(Exception):
    pass
```

and raise `SolutionFound` when the solution is found.
