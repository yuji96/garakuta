import numpy as np
from numba import njit, int64


@njit(int64[:, :](int64[::1]))
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

    def fillable(table, index, value):

        row = index // 9
        col = index % 9
        block = lambda x: ((x // 3) * 3, (x // 3 + 1) * 3)

        same_in_areas = False
        for area in [
            table[row, :], table[:, col],
            table[block(row)[0]:block(row)[1], block(col)[0]:block(col)[1]].flatten()
        ]:
            for i in area:
                same_in_areas += (i == value)

        return not same_in_areas

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


if __name__ == "__main__":
    table = [0, 0, 5, 3, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 2, 0, 0, 7, 0, 0, 1, 0, 5, 0, 0, 4, 0, 0, 0, 0, 5, 3, 0, 0,
             0, 1, 0, 0, 7, 0, 0, 0, 6, 0, 0, 3, 2, 0, 0,
             0, 8, 0, 0, 6, 0, 5, 0, 0, 0, 0, 9, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 9, 7, 0, 0]
    # table = [0, 0, 0, 8, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 8, 0, 0,
    #          0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 3, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 7, 5, 0, 0, 3, 4, 0, 0, 0, 0, 0,
    #          0, 0, 0, 2, 0, 0, 6, 0, 0]
    table = np.array(table).flatten()
    print(fill(table))
