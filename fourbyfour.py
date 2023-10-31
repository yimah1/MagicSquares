import numpy as np
from threebythree import *
import time


# numbers is a list of numbers to put in the 4x4 magic square
# rowsums is a list of desired sums of the 4 rows
# colsums is a list of desired sums of the 4 columns
# diagsum is the desired sum of the main diagonal
def generate4x4(numbers, rowsums, colsums, diagsum):
    listofmagicsquares = []
    for x11 in numbers:
        if (x11 < rowsums[0]) and (x11 < colsums[0]) and (x11 < diagsum):
            firstrow = np.zeros((1, 4))
            firstrow[0, 0] = x11
            remaining1 = numbers.copy()
            remaining1.remove(x11)
            for x12 in remaining1:
                if (x12 < colsums[1]) and (x11 + x12 < rowsums[0]):
                    firstrow[0, 1] = x12
                    remaining2 = remaining1.copy()
                    remaining2.remove(x12)
                    for x13 in remaining2:
                        x14 = rowsums[0] - x11 - x12 - x13
                        remaining3 = remaining2.copy()
                        remaining3.remove(x13)
                        if (x13 < colsums[2]) and (x14 < colsums[3]) and (x14 > 0) and (x14 in remaining3):
                            firstrow[0, 2] = x13
                            firstrow[0, 3] = x14
                            remaining3.remove(x14)
                            firstcolumn = np.zeros((3, 1))
                            for x21 in remaining3:
                                if (x21 < rowsums[1]) and (x11 + x21 < colsums[0]):
                                    firstcolumn[0, 0] = x21
                                    remaining4 = remaining3.copy()
                                    remaining4.remove(x21)
                                    for x31 in remaining4:
                                        x41 = colsums[0] - x11 - x21 - x31
                                        remaining5 = remaining4.copy()
                                        remaining5.remove(x31)
                                        if (x31 < rowsums[2]) and (x41 < rowsums[3]) and (x41 > 0) and (
                                                x41 in remaining5):
                                            firstcolumn[1, 0] = x31
                                            firstcolumn[2, 0] = x41
                                            remaining5.remove(x41)
                                            rowsums3x3 = [rowsums[1] - x21, rowsums[2] - x31, rowsums[3] - x41]
                                            colsums3x3 = [colsums[1] - x12, colsums[2] - x13, colsums[3] - x14]
                                            diagsum3x3 = diagsum - x11
                                            listof3x3 = generate3x3(remaining5, rowsums3x3, colsums3x3, diagsum3x3)
                                            for square in listof3x3:
                                                magicsquare = np.hstack((firstcolumn, square))
                                                magicsquare = np.vstack((firstrow, magicsquare))
                                                listofmagicsquares.append(magicsquare)
    return listofmagicsquares


'''
numbers = list(range(1, 17))
rowsums = [34, 34, 34, 34]
colsums = rowsums
diagsum = 34
start = time.time()
list1 = generate4x4(numbers, rowsums, colsums, diagsum)
finallist = []
for x in list1:
    if (np.sum(np.fliplr(x).diagonal()) == 34):
        finallist.append(x)
f = open("4x4magicsquares.txt", "w")
for x in finallist:
    f.write(f"{x}\n\n")
f.close()
end = time.time()
elapsed = end - start
print("It took", elapsed, "seconds")
'''
