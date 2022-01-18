# CMPE 493 Introduction to Information Retrieval Homework 1

In this project, [edit distance](https://en.wikipedia.org/wiki/Edit_distance) between two strings are calculated.

Edit distance is the minimum operations needed to transform one string to another. For example, if we have "book" and "box" then the edit distance is 2 (book -> boox -> box). 
This distance can be used for automatic spelling correction in search engines.

Both [Damerau-Levensthein](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance) and [Levensthein](https://en.wikipedia.org/wiki/Levenshtein_distance) edit distance
are available.

Example:

```
> python3 hw1.py
Enter the first string: book
Enter the second string: box

Levensthein edit distance:
2

The table:
[0, 1, 2, 3]
[1, 0, 1, 2]
[2, 1, 0, 1]
[3, 2, 1, 1]
[4, 3, 2, 2]

Sequence of operations:
['copy b', 'delete o', 'copy o', 'replace k with x']

Damerau Levensthein edit distance:
2

The table:
[0, 1, 2, 3]
[1, 0, 1, 2]
[2, 1, 0, 1]
[3, 2, 1, 1]
[4, 3, 2, 2]

Sequence of operations:
['copy b', 'delete o', 'copy o', 'replace k with x']
```
