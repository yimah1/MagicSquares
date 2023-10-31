import numpy as np
from fourbyfour import *
import time


# numbers is a list of numbers to put in the 4x4 magic square
# rowsums is a list of desired sums of the 4 rows
# colsums is a list of desired sums of the 4 columns
# diagsum is the desired sum of the main diagonal
def generate5x5(numbers, rowsums, colsums, diagsum):
    listofmagicsquares = []
    for x11 in numbers:
        if (x11 < rowsums[0]) and (x11 < colsums[0]) and (x11 < diagsum):
            firstrow = np.zeros((1, 5))
            firstrow[0, 0] = x11
            remaining1 = numbers.copy()
            remaining1.remove(x11)
            for x12 in remaining1:
                if (x12 < colsums[1]) and (x11 + x12 < rowsums[0]):
                    firstrow[0, 1] = x12
                    remaining2 = remaining1.copy()
                    remaining2.remove(x12)
                    for x13 in remaining2:
                        if (x13 < colsums[2]) and (x11 + x12 + x13 < rowsums[0]):
                            firstrow[0, 2] = x13
                            remaining3 = remaining2.copy()
                            remaining3.remove(x13)
                            for x14 in remaining3:
                                x15 = rowsums[0] - x11 - x12 - x13 - x14
                                remaining4 = remaining3.copy()
                                remaining4.remove(x14)
                                if (x14 < colsums[3]) and (x15 < colsums[4]) and (x15 > 0) and (x15 in remaining4):
                                    firstrow[0, 3] = x14
                                    firstrow[0, 4] = x15
                                    remaining4.remove(x15)
                                    firstcolumn = np.zeros((4, 1))
                                    for x21 in remaining4:
                                        if (x21 < rowsums[1]) and (x11 + x21 < colsums[0]):
                                            firstcolumn[0, 0] = x21
                                            remaining5 = remaining4.copy()
                                            remaining5.remove(x21)
                                            for x31 in remaining5:
                                                if (x31 < rowsums[2]) and (x11 + x21 + x31 < colsums[0]):
                                                    firstcolumn[1, 0] = x31
                                                    remaining6 = remaining5.copy()
                                                    remaining6.remove(x31)
                                                    for x41 in remaining6:
                                                        x51 = colsums[0] - x11 - x21 - x31 - x41
                                                        remaining7 = remaining6.copy()
                                                        remaining7.remove(x41)
                                                        if (x41 < rowsums[3]) and (x51 < rowsums[4]) and (x51 > 0) and (
                                                                x51 in remaining7):
                                                            firstcolumn[2, 0] = x41
                                                            firstcolumn[3, 0] = x51
                                                            remaining7.remove(x51)
                                                            rowsums4x4 = [rowsums[1] - x21, rowsums[2] - x31,
                                                                          rowsums[3] - x41, rowsums[4] - x51]
                                                            colsums4x4 = [colsums[1] - x12, colsums[2] - x13,
                                                                          colsums[3] - x14, colsums[4] - x15]
                                                            diagsum4x4 = diagsum - x11
                                                            listof4x4 = generate4x4(remaining7, rowsums4x4, colsums4x4,
                                                                                    diagsum4x4)
                                                            for square in listof4x4:
                                                                magicsquare = np.hstack((firstcolumn, square))
                                                                magicsquare = np.vstack((firstrow, magicsquare))
                                                                if np.sum(np.fliplr(magicsquare).diagonal()) == 65:
                                                                    print(magicsquare)
                                                                    f = open("5x5magicsquares.txt", "a")
                                                                    f.write(magicsquare, "\n\n")
                                                                    f.close()
                                                                    listofmagicsquares.append(magicsquare)

    return listofmagicsquares


numbers = list(range(1, 26))
rowsums = [65, 65, 65, 65, 65]
colsums = [65, 65, 65, 65, 65]
start = time.time()
list1 = generate5x5(numbers, rowsums, colsums, 65)
'''
finallist=[]
for x in list1:
    if (np.sum(np.fliplr(x).diagonal())==365):
        finallist.append(x)
f = open("5x5magicsquares.txt","w")
for x in finallist:
    f.write(f"{x}\n")
f.close()
'''
end = time.time()
elapsed = end - start
print("It took", elapsed, "seconds")
