# Project: Solve Puzzle with Glucose3 - PySat

## Description Puzzle
- Given a matrix of m x n, a cell consists of a non-negative integer or it is blank.
- Each cell has 9 “adjacent” neighbors, including itself and 8 cells around. Players color cells by red or green so that the number of green cells which are “adjacent” to a cell is exactly the number inside.
- There is no constraint for blank cells.

![Example 1](/images/image1.png)

## Solution

- Use biconditional sentences to represent constraints
$$a \land b \Leftrightarrow \neg c \land \neg d \land \neg e $$
- Eliminate biconditional connectives
- Use the **itertools** module to generate clauses automatically

## Note

- If you use the Google Colab please install these modules first

```
%pip install python-sat==0.1.7.dev12
%pip install colorama
```