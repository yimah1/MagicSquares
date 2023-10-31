# MagicSquares

This project is an algorithm for finding magic squares of different sizes.

An n by n magic square is an n by n array of numbers from 1 to n^2. In this array, each row, column, and diagonal must sum up to the same number.

In the algorithm for finding n by n magic squares, we plug in numbers in the first row and column, then call on the algorithm for finding (n-1) by (n-1) magic squares, all the while making sure all rows, columns, and diagonals add up to the same number.
