import numpy as np
from time import sleep

# 問題設定
table = [[0, 1, 0, 0, 0, 6, 0, 0, 4],
         [0, 0, 6, 0, 0, 0, 2, 5, 0],
         [3, 0, 0, 8, 0, 0, 0, 0, 0],
         [9, 0, 0, 7, 0, 0, 0, 3, 0],
         [0, 0, 8, 0, 0, 0, 4, 0, 0],
         [0, 2, 0, 0, 0, 9, 0, 0, 7],
         [0, 0, 0, 0, 0, 2, 0, 0, 8],
         [0, 4, 5, 0, 0, 0, 6, 0, 0],
         [7, 0, 0, 3, 0, 0, 0, 9, 0]]

ans =   [[2, 1, 7, 5, 9, 6, 3, 8, 4],
         [8, 9, 6, 4, 3, 7, 2, 5, 1],
         [3, 5, 4, 8, 2, 1, 9, 7, 6],
         [9, 6, 1, 7, 4, 5, 8, 3, 2],
         [5, 7, 8, 2, 1, 3, 4, 6, 9],
         [4, 2, 3, 6, 8, 9, 5, 1, 7],
         [6, 3, 9, 1, 5, 2, 7, 4, 8],
         [1, 4, 5, 9, 7, 8, 6, 2, 3],
         [7, 8, 2, 3, 6, 4, 1, 9, 5]]


# table =    [[0, 0, 5, 4, 0, 7, 8, 1, 0],
#             [0, 0, 0, 1, 0, 2, 7, 0, 0],
#             [0, 0, 1, 0, 5, 6, 0, 0, 2],
#             [1, 0, 7, 0, 0, 0, 4, 0, 8],
#             [4, 0, 2, 0, 0, 1, 0, 0, 9],
#             [8, 0, 6, 0, 0, 0, 2, 0, 1],
#             [6, 0, 0, 0, 1, 0, 0, 0, 0],
#             [0, 1, 3, 9, 0, 8, 0, 0, 0],
#             [0, 0, 4, 7, 0, 3, 1, 0, 0]]

table = np.array(table)
ans = np.array(ans)


def fill(table_flat):
    """未入力の要素に仮定を代入する,

    Parameters
    -------
        table_flat : np.ndarray of int
            計算中の行列。1D-array

    Returns
    -------
        np.ndarray of int
            仮定がが代入された行列。shape = (9, 9)
    """

    for tmp_i, tmp_val in enumerate(table_flat):

        if tmp_val == 0:

            fillable_vals = [val
                             for val in range(tmp_val + 1, 10)
                             if fillable(table_flat.reshape(9, 9), tmp_i, val)]

            for new_val in fillable_vals:

                table_flat[tmp_i] = new_val
                print(f"\033[9A\r{table_flat.reshape(9, 9)}")

                if table_flat.all():
                    return table_flat.reshape(9, 9)
                else:
                    if fill(table_flat) is None:
                        continue

            table_flat[tmp_i] = 0
            break


def fillable(table, index, value):
    row = index // 9
    col = index % 9

    fillable_in_row = value not in table[row, :]
    fillable_in_col = value not in table[:, col]
    fillable_in_block = value not in table[
                                     (row // 3) * 3: (row // 3 + 1) * 3,
                                     (col // 3) * 3: (col // 3 + 1) * 3,
                                     ]

    return fillable_in_row and fillable_in_col and fillable_in_block


# print(table)
print("\n"*9)
print(fill(table.flatten()))
