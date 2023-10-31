import numpy as np
from twobytwo import *
import time


# numbers is a list of numbers to put in the 3x3 magic square
# rowsums is a list of desired sums of the 3 rows
# colsums is a list of desired sums of the 3 columns
# diagsum is the desired sum of the main diagonal
def generate3x3(numbers, rowsums, colsums, diagsum):
    listofmagicsquares = []
    for x11 in numbers:  # x11 is the top left entry
        if (x11 < rowsums[0]) and (x11 < colsums[0]) and (x11 < diagsum):
            firstrow = np.zeros((1, 3))
            firstrow[0, 0] = x11
            remaining1 = numbers.copy()
            remaining1.remove(x11)
            for x12 in remaining1:  # x12 is the top middle entry
                x13 = rowsums[0] - x11 - x12  # x13 is the top right entry
                remaining2 = remaining1.copy()
                remaining2.remove(x12)
                if (x12 < colsums[1]) and (x13 < colsums[2]) and (x13 > 0) and (x13 in remaining2):
                    firstrow[0, 1] = x12
                    firstrow[0, 2] = x13
                    remaining2.remove(x13)
                    firstcolumn = np.zeros((2, 1))
                    for x21 in remaining2:  # x21 is the middle left entry
                        x31 = colsums[0] - x11 - x21  # x31 is the bottom left entry
                        remaining3 = remaining2.copy()
                        remaining3.remove(x21)
                        if (x21 < rowsums[1]) and (x31 < rowsums[2]) and (x31 > 0) and (x31 in remaining3):
                            firstcolumn[0, 0] = x21
                            firstcolumn[1, 0] = x31
                            remaining3.remove(x31)
                            rowsums2x2 = [rowsums[1] - x21, rowsums[2] - x31]
                            colsums2x2 = [colsums[1] - x12, colsums[2] - x13]
                            diagsum2x2 = diagsum - x11
                            listof2x2 = generate2x2(remaining3, rowsums2x2, colsums2x2, diagsum2x2)
                            for square in listof2x2:
                                magicsquare = np.hstack((firstcolumn, square))
                                magicsquare = np.vstack((firstrow, magicsquare))
                                listofmagicsquares.append(magicsquare)
    return listofmagicsquares


'''
numbers = list(range(1, 10))
rowsums = [15, 15, 15]
colsums = rowsums
diagsum = 15
start = time.time()
list1 = generate3x3(numbers, rowsums, colsums, diagsum)
finallist = []
for x in list1:
    if (np.sum(np.fliplr(x).diagonal()) == 15):
        finallist.append(x)
f = open("3x3magicsquares.txt", "w")
for x in finallist:
    f.write(x, "\n")
f.close()
end = time.time()
elapsed = end - start
print("It took", elapsed, "seconds")
'''