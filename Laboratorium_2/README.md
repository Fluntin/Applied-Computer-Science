# Magic Trick Program

This program simulates a magic trick involving a deck of cards. The magician takes out the thirteen spades from the deck, holds them like a deck of cards with the back facing up, and lays them out in the following manner: The top card is placed at the bottom, the next card is laid face up, the next card is placed at the bottom, and so on. To the audience's amazement, the cards appear in ascending order: Ace, Two, Three...

Execution: The cards are secretly arranged as follows:

"Yes, here we break the quote from Liberg: Magic for Everyone. The lab task is to find out the secret of card magic! Therefore, you need to create a program that can simulate the card trick as follows:

What is the order of the cards?
3   1   4   2   5 
The cards come out in this order: 1 2 3 5 4

In this lab, you will implement a queue in two different ways. With the abstract data structure queue, you can perform the following operations:

- Queue(): Create an empty queue.
- enqueue(x): Add an item to the end of the queue.
- x = dequeue(): Remove and return the item at the front of the queue.
- isEmpty(): Check if the queue is empty.
- size(): Get the number of elements in the queue.

Tasks:

1. ArrayQ - a queue using Python's array:
   In the first task, you need to write your own ArrayQ class where you implement a queue using Python's array. The array data structure is an efficient variant of a list, but it has certain limitations.
   - Start by importing the array module with `from array import array`.
   - Decide the type of data you want to store.
   - Create an array and experiment with array methods like `append()`, `insert()`, `remove()`, and `pop()`. Draw diagrams illustrating what these methods do. Which methods do you want to use in your `enqueue()` and `dequeue()` functions?
   - Now you are ready to write your own ArrayQ class.
   - Attributes: An array (and any other attributes you want to include). All attributes should be private (begin with an underscore `_`).
   - Test ArrayQ: Test your queue with the provided test program.

2. Magic Trick Program:
   Write a program that simulates the card trick (refer to the video and the example at the beginning of the lab).
   Tips for input: Use `input()` to read the entire line, `split()` to split it, and `int()` to convert it to integers. Then, experiment with different input orders and try to figure out the order in which the cards should be arranged before performing the trick to get all thirteen cards in the correct order.

3. Create an ArrayQ Module:
   Cut out the ArrayQ class from your program and paste it into a new file named `arrayQFile.py`. Import the class into the main program with the line `from arrayQFile import ArrayQ`. Now you can use the class without it being visible in the program.

Tips: Use the `if __name__ == "__main__":` statement in your module to prevent running any additional code, such as test code, in ArrayQ.

4. LinkedQ - a queue of nodes (linked list):
   Now you will implement the queue as a linked list. This requires two new classes: Node and LinkedQ. Write both classes in the same file named `linkedQFile.py`. The nodes in the list are objects that each contain two attributes: a value and a reference to the next object. These two attributes do not need to be private.
  
