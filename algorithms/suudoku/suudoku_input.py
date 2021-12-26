from time import time

import matplotlib.pyplot as plt
import numpy as np

from suudoku import fill as fill_slow
from suudoku_faster import fill as fill_fast
from quizes import table1 as table

# 時間測定用
# コンパイル時間を含めたくない場合は先に空回しする。
# fill_fast(np.array(table).copy())

print("計算開始")

start = time()
ans = fill_fast(np.array(table).copy())
finish = time()

print("解答")
print(ans)
print()
print(f"計算時間(sec): {finish - start:5.7}")


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
