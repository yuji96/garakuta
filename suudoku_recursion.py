from pprint import pprint
import numpy as np

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
is_filled_array = table.flatten().astype(np.bool)


def fill(table_flat, is_filled_array):
    """未入力の要素に仮定を代入する,

    Parameters
    -------
        table_flat : np.ndarray of int
            計算中の行列。1D-array
        is_filled_array : np.ndarray of np.bool
            計算前の行列を`np.bool`に変換した行列。

    Returns
    -------
        np.ndarray of int
            仮定がが代入された行列。shape = (9, 9)
    """

    for tmp_i, (tmp_value, is_filled) in enumerate(zip(table_flat, is_filled_array)):

        if not is_filled:
            for new_value in range(tmp_value, 10):

                if fillable(table_flat.reshape(9, 9), tmp_i, new_value):
                    table_flat[tmp_i] = new_value
                    fill(table_flat, is_filled_array)

    return table_flat.reshape(9, 9)


def fillable(table, index, value):
    row = index // 9
    col = index % 9

    fillable_in_row = value not in table[row, :]
    fillable_in_col = value not in table[:, col]
    fillable_in_block = value not in table[
                                     (row // 3) * 3: (row // 3 + 1) * 3 - 1,
                                     (col // 3) * 3: (col // 3 + 1) * 3 - 1,
                                     ]

    return fillable_in_row and fillable_in_col and fillable_in_block


print(table)
# fill(table.flatten())
print(fill(table.flatten(), is_filled_array))
