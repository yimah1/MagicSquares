import numpy as np


# numbers is a list of numbers to put in the 2x2 magic square
# rowsums is a list of desired sums of the 2 rows
# colsums is a list of desired sums of the 2 columns
# diagsum is the desired sum of the main diagonal
def generate2x2(numbers, rowsums, colsums, diagsum):
    listofmagicsquares = []
    for x11 in numbers:
        if (x11 < rowsums[0]) and (x11 < colsums[0]) and (x11 < diagsum):
            magicsquare = np.zeros((2, 2))
            magicsquare[0, 0] = x11  # put x11 in top left entry
            remaining = numbers.copy()
            remaining.remove(x11)
            x12 = rowsums[0] - x11  # number to put in square to finish 1st row
            if (x12 < colsums[1]) and (x12 > 0) and (x12 in remaining):
                magicsquare[0, 1] = x12
                remaining.remove(x12)
                x21 = colsums[0] - x11  # number to put in square to finish 1st column
                if (x21 < rowsums[1]) and (x21 > 0) and (x21 in remaining):
                    magicsquare[1, 0] = x21
                    remaining.remove(x21)
                    remaining = remaining[0]
                    if (remaining + x21 == rowsums[1]) and (remaining + x12 == colsums[1]) and (
                            remaining + x11 == diagsum):
                        magicsquare[1, 1] = remaining
                        listofmagicsquares.append(magicsquare)
    return listofmagicsquares
