import numpy as np


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

                if fill(table_flat) is not None:
                    break
            else:
                table_flat[tmp_i] = 0
                break
    else:
        return table_flat.reshape(9, 9)


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


if __name__ == "__main__":
    table = []
    table = np.array(table).flatten()
    print(fill(table))