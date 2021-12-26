from time import time

import matplotlib.pyplot as plt
import numpy as np

from with_numpy import fill as fill_slow
from with_numba import fill as fill_fast
from quizes import table1 as table


def main(with_plt=False, ignore_compile_time=False):
    """数独を得関数を呼び出す。

    Parameters
    ----------
    with_plt : bool, default False
        matplotlib で描画するかを指定する。
    ignore_compile_time : bool, default False
        計算時間のみを測りたい場合は、コンパイル時間を含めないために先に空回しする。

    """

    if ignore_compile_time:
        fill_fast(np.array(table).copy())

    print("計算開始")
    start = time()
    ans = fill_fast(np.array(table).copy())
    finish = time()
    print(f"計算時間(sec): {finish - start:5.7}")

    print("\n解答")
    print(ans)
    
    if with_plt:
        visualize_with_plt(ans)    


def visualize_with_plt(ans):
    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_visible(False)
    ax.axis("off")

    colors = np.where(table, "#F5A9BC", "#ffffff").reshape(9, 9)
    picture = ax.table(cellText=ans, cellColours=colors, loc='center')
    picture.set_fontsize(25)
    picture.scale(1, 3)

    ax.axhline(y=0.340, color="b")
    ax.axhline(y=0.665, color="b")
    ax.axvline(x=0.335, color="b")
    ax.axvline(x=0.665, color="b")

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
