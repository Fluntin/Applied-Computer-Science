# Graph Traversal and Word Path

## Preliminary Tasks

Draw a graph and write down the adjacency matrix and adjacency list for the following words: tre öre tri tro trå trä. The graph should have edges (unweighted, undirected) between words that differ by only one letter. Answer the following questions:
- How many nodes does your graph have?
- How many edges?
- What percentage of the adjacency matrix is filled?

Draw a graph with directed edges (determine the directions yourself) and write down the adjacency matrix and adjacency list for the following words: arg ärg agg alg ark arm art arv. Answer the following questions:
- How many edges does your graph have?
- What percentage of the adjacency matrix is filled?
- Are there any cycles in the graph?

## Problem Description

In lab 4 and 5, you will solve the following problem:

Find the shortest path from one word to another by changing one letter at a time. For example:

söt -> söm -> döm -> dum -> dur -> sur
(Note: The word "döm" is missing in the file `word3.txt`, but the principle should be clear.)

All intermediate words must be present in a word list (such as the `word3.txt` word list from the previous lab). Can you find a shorter path than the one with six words above?

In lab 4, you will write a program to determine if a path exists or not. The solution principle is discussed below and is often described in textbooks for the analogous problem of finding the shortest path in a graph. For example:

    Start word: söt
    End word: sur
    There is a path from söt to sur.

In lab 5, you will then print the path, i.e., the words in the solution.

## Breadth-First Search

How should we use breadth-first search in this problem? This is a graph problem, but we will not store the graph in an adjacency matrix or adjacency list. Instead, we will create the graph's vertices while the program is running, following the algorithm below.

The root of the problem tree, "söt," has children "nöt," "sot," "söm," and more.
The grandchildren include "not," "som," "döm," and so on.

According to the chain "söt -> söm -> döm -> dum -> dur -> sur," 
"sur" is a great-great-great-great-grandchild of "söt," but "sur" might already exist earlier in the problem tree. To find the first occurrence, perform a breadth-first search as follows:

1. Add the initial word as the first and only word in a queue.
2. Repeat the following as long as there are words remaining in the queue:
   - Remove the first word from the queue,
   - Create all children of that word,
   - Add them to the end of the queue.
3. The first occurrence of the desired word gives the shortest solution.
   It is possible to save time and space by avoiding the creation of children that are duplicates of previous relatives (e.g., "nöt" as a child of "söt"), known as "dumb children."

## First Version

In the `bfs.py` file, use the code from the previous lab, which already has two binary trees. We will now call them `swedish` (for the word list) and `old` (for the dumb children). The main program should:
- Read the word list.
- Ask for the start word and end word.
- Call the `makechildren(start_word)` function.
The `makechildren` function should systematically go through all possible ways to change one letter in the start word (`aöt`, `böt`, ..., `söö`), check if the new word exists in the word list but not in the `old` list, and if so, print the new word on the screen and add it to the `old` list.

Test the program! If implemented correctly, "söt" should have 10 children.

## Second Version

To continue exploring the grandchildren of "söt" and so on, we need the `LinkedQ` queue class that you wrote in lab 2, the card trick lab. Import it and create the queue `q`. Instead of printing the children on the screen, the `makechildren()` function should now add them to the queue. The main program should add the start word to the queue and then run a loop, roughly like this:

```python
while not q.isEmpty():
    node = q.dequeue()
    makechildren(node, q)
```

When `makechildren()` encounters the end word, it should print:
```python
print("There is a path to", end_word)
```
or indicate that no path was found. Test it with different start and end words, including "blå" - "röd", "ful" - "fin", and "ute" - "hit".
