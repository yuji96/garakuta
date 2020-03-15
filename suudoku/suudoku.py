import numpy as np
def fillable(table, index, value):
    """計算中の行列において、正解だと仮定した値が数独の条件を満たしているか検証する。

    Parameters
    -------
        table : np.ndarray of int
            計算中の行列。2D-array。
        index : int
            仮定したマス目の場所。1行目は0~8, 2行目は9~17, ...
        value : int
            仮定した数。

    Returns
    -------
        bool
            計算中の行列において、仮定が正解である可能性があるかないか。
    """

    row = index // 9
    col = index % 9

    fillable_in_row = value not in table[row, :]
    fillable_in_col = value not in table[:, col]
    fillable_in_block = value not in table[
                                     (row // 3) * 3: (row // 3 + 1) * 3,
                                     (col // 3) * 3: (col // 3 + 1) * 3,
                                     ]

    return fillable_in_row and fillable_in_col and fillable_in_block


def fill(table_flat):
    """深さ優先探索により、数独を解く。

    Parameters
    -------
        table_flat : np.ndarray of int
            数独の問題。1D-array

    Returns
    -------
        np.ndarray of int
            仮定が代入された行列。shape = (9, 9)
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
