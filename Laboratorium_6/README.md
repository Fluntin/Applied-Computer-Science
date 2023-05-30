# Searching and Sorting

In this lab, you will work with larger datasets. The file `unique_tracks.txt` (84MB) is obtained from the Million Song Dataset and contains data about one million songs. Each line in the file has the following format:

```
trackid<SEP>songid<SEP>artistname<SEP>songtitle
```

Download the file by right-clicking and selecting "Save link as...".

If you are using the school's Ubuntu computers, the file is located at: `/info/tilda/unique_tracks.txt`

## List with Objects

Write a class that represents a song as described above. In addition to the usual methods, implement `__lt__(self, other)` that compares whether the `self` object is less than the `other` object based on the artist name.

Read the songs from the file, create an object for each line, and store the objects in a list. Test that the reading process has been successful.

## The `timeit` Module

Read the documentation for Python's `timeit` module and answer the following questions:

1. What does the `stmt` parameter represent?
2. What does the `number` parameter represent?
3. What does `timeit` measure the time for?
4. What is printed by a call to `timeit`?

## Timing

### Searching

Here, you will compare searching using three different methods:

1. Linear search in an unsorted list.
2. Binary search in a sorted list. Sort the list first using Python's `sort` method.
3. Hash table search. You can use either Python's `dict` or your own hash table implementation.

Write a program that times each variant of the search methods above.

To get started, here is an example (you need to implement the *italicized* functions yourself). When timing a function with parameters, you can use `lambda`.

```python
def main():
    filename = "/info/tilda/unique_tracks.txt"

    song_list = readfile(filename)
    n = len(song_list)
    print("Number of elements =", n)

    last_song = song_list[n-1]
    test_artist = last_song.artist

    linear_time = timeit.timeit(stmt=lambda: linear_search(song_list, test_artist), number=10000)
    print("Linear search took", round(linear_time, 4), "seconds")
```

You can choose what to search for (song title or artist name). You can also choose which element to search for. The example above searches for the last artist. Is it a good idea?

Fill in the times in the following table:

| n           | 250,000     | 500,000     | 1,000,000   |
|-------------|-------------|-------------|-------------|
| Linear search        |             |             |             |
| Binary search        |             |             |             |
| Hash table search    |             |             |             |

To create a smaller list, you can use slicing:

```python
smaller_list = larger_list[0:250000]
```

### Sorting

Here, you will compare two different sorting methods. You can choose which methods you want to use (as long as you can explain them). Choose one slower method and one faster method. You can use code (for sorting) from lectures, the textbook, or other sources, but be sure to indicate where the code comes from.

You can choose to sort by song title or artist name. Modify your timing code from the previous search to include sorting (sorting 1000 times might take a long time).

Fill in the times in the following table:

| n           | 1,000       | 10,000      | 100,000     | 1,000,000   |
|-------------|-------------|-------------|-------------|-------------|
| Slower Sorting Method   |             |             |             |             |
| Faster Sorting Method   |             |             |             |             |

### Analysis

Write down the time complexity of the algorithms you timed above. Do your results match the theory? If not, what could be the reason?

Write a comment at the end of your program where you analyze your results. Explain the difference in time between the different operations.
