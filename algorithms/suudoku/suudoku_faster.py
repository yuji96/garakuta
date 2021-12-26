from numba import njit, int64, bool_
import numpy as np


@njit(bool_(int64[:, :], int64, int64))
def fillable(table, index, value):

    row = index // 9
    col = index % 9
    block = lambda x: ((x // 3) * 3, (x // 3 + 1) * 3)

    same_in_areas = False
    for i in np.hstack((
            table[row, :], table[:, col],
            table[block(row)[0]:block(row)[1], block(col)[0]:block(col)[1]].flatten()
    )):
        same_in_areas |= (i == value)

    return not same_in_areas


@njit(int64[:, :](int64[::1]))
def fill(table_flat):

    for tmp_i, tmp_val in enumerate(table_flat):

        if tmp_val == 0:
            fillable_vals = [val
                             for val in range(tmp_val + 1, 10)
                             if fillable(table_flat.reshape(9, 9), tmp_i, val)]

            for new_val in fillable_vals:
                table_flat[tmp_i] = new_val

                if fill(table_flat).all():
                    break
            else:
                table_flat[tmp_i] = 0
                break
    return table_flat.reshape(9, 9)
