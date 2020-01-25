from pprint import pprint
import numpy as np
from collections import deque



# 問題設定
table =    [[0, 1, 0, 0, 0, 6, 0, 0, 4],
            [0, 0, 6, 0, 0, 0, 2, 5, 0],
            [3, 0, 0, 8, 0, 0, 0, 0, 0],
            [9, 0, 0, 7, 0, 0, 0, 3, 0],
            [0, 0, 8, 0, 0, 0, 4, 0, 0],
            [0, 2, 0, 0, 0, 9, 0, 0, 7],
            [0, 0, 0, 0, 0, 2, 0, 0, 8],
            [0, 4, 5, 0, 0, 0, 6, 0, 0],
            [7, 0, 0, 3, 0, 0, 0, 9, 0]]

# table =    [[0, 0, 5, 4, 0, 7, 8, 1, 0],
#             [0, 0, 0, 1, 0, 2, 7, 0, 0],
#             [0, 0, 1, 0, 5, 6, 0, 0, 2],
#             [1, 0, 7, 0, 0, 0, 4, 0, 8],
#             [4, 0, 2, 0, 0, 1, 0, 0, 9],
#             [8, 0, 6, 0, 0, 0, 2, 0, 1],
#             [6, 0, 0, 0, 1, 0, 0, 0, 0],
#             [0, 1, 3, 9, 0, 8, 0, 0, 0],
#             [0, 0, 4, 7, 0, 3, 1, 0, 0]]


table_array = np.array(table)

for row in range(9):
    for col in range(9):
        temp = table[row][col]
        table[row][col] = [temp] if temp else [i for i in range(1, 10)]




def dedupe():
    for row in range(9):
        for col in range(9):
            f = lambda x:x // 3 * 3
            horizon  = table_array[row]
            vertical = table_array[:, col]
            block    = table_array[f(row) : f(row) + 3, f(col) : f(col) + 3]
            default = np.hstack((horizon, vertical, block.reshape(1, 9)[0]))
            temp = table[row][col]
            if len(temp) > 1:
                table[row][col] = [i for i in range(1, 10) if i not in default]
            temp = table[row][col]
            if len(temp) == 1:
                table_array[row][col] = temp[0]

def filling():
    while True:
        before = np.copy(table_array)
        dedupe()
        if np.array_equal(before, table_array):
            break

filling()


def fill_single_in_low():

    def single_in_row(row):
        """ Return : list """
        elems = []
        for inner_list in np.array(table)[row, :]:
            elems += inner_list
        for fixed in table_array[row, :]:
            if fixed in elems:
                elems.remove(fixed)
        return [num for num in elems if elems.count(num) == 1]

    for row in range(9):
        queue = deque(single_in_row(row))
        for col, elems in enumerate(np.array(table)[row, :]):
            for single in list(queue):
                if single in elems:
                    temp = queue.popleft()
                    table_array[row][col] = temp
                    table[row][col] = [temp]
                    filling()



def single_in_col(col):
    """ Return : list """
    elems = []
    for inner_list in np.array(table)[:, col]:
        elems += inner_list
    for fixed in table_array[:, col]:
        if fixed in elems:
            elems.remove(fixed)
    return [num for num in elems if elems.count(num) == 1]

fill_single_in_low()

for col in range(9):
    queue = deque(single_in_col(col))
    for row, elems in enumerate(np.array(table)[:, col]):
        for single in list(queue):
            if single in elems:
                temp = queue.popleft()
                table_array[row][col] = temp
                table[row][col] = [temp]
                filling()

fill_single_in_low()


print(table_array)
print(table)