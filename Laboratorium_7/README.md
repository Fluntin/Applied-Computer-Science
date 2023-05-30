### Hashing with Python's Built-in Dictionary

1. Create a class called `DictHash` that utilizes Python's built-in `dict` for implementing the hash table.
2. Implement the following methods in the `DictHash` class:
   - `store(nyckel, data)`: Store the given `data` as the `value` in the dictionary with `nyckel` as the `key`.
   - `search(nyckel)`: Look up the `nyckel` in the dictionary and return the corresponding value.
   - Optionally, you can add the following methods:
     - `__getitem__(self, nyckel)`: Allow accessing elements using square brackets, e.g., `d[nyckel]`.
     - `__contains__(self, nyckel)`: Allow checking if a key exists using the `in` operator, e.g., `if nyckel in d`.

3. Test your `DictHash` class with the provided data file "Armands pokedex." Create Pokémon objects as in the first lab, store them in the hash table using their names as keys, and perform searches to test the functionality.

### Custom Implementation of Hash Table

1. Define a class called `HashNode` to represent the nodes in the hash table. Each node should contain both a `key` and a `value`.
2. Implement the `Hashtable` class with the desired functionality and interface, similar to `DictHash`, but with your custom implementation.
3. Consider the following requirements for your custom hash table implementation:
   - Determine an appropriate size for the hash table.
   - Implement a suitable hash function that provides good distribution across the table.
   - Handle collisions, such as using collision lists or probing.
   - Use `KeyError` to indicate when a key is not found.

### Testing

1. Test your custom hash table implementation using the provided data file "Armands pokedex" as well as the "hashtest.py" program.
2. Modify the "hashtest.py" program to check if your hash table implementation is functioning correctly.
3. Optionally, you can test your hash table on the Kattis platform using the provided main program.

Remember to analyze your results, discuss the time complexity of the operations, and explain any differences in performance between different approaches or data sizes.

I hope this helps you progress with your tasks! Let me know if you have any further questions.
