from suudoku import fill as fill_slow
from suudoku_faster import fill as fill_fast
import matplotlib.pyplot as plt
import numpy as np
from time import time

# table = [0, 0, 5, 3, 0, 0, 0, 0, 0,
#          8, 0, 0, 0, 0, 0, 0, 2, 0,
#          0, 7, 0, 0, 1, 0, 5, 0, 0,
#          4, 0, 0, 0, 0, 5, 3, 0, 0,
#          0, 1, 0, 0, 7, 0, 0, 0, 6,
#          0, 0, 3, 2, 0, 0, 0, 8, 0,
#          0, 6, 0, 5, 0, 0, 0, 0, 9,
#          0, 0, 4, 0, 0, 0, 0, 3, 0,
#          0, 0, 0, 0, 0, 9, 7, 0, 0]

table =  [0, 0, 0, 8, 0, 1, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 4, 3, 0,
          5, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 7, 0, 8, 0, 0,
          0, 0, 0, 0, 0, 0, 1, 0, 0,
          0, 2, 0, 0, 3, 0, 0, 0, 0,
          6, 0, 0, 0, 0, 0, 0, 7, 5,
          0, 0, 3, 4, 0, 0, 0, 0, 0,
          0, 0, 0, 2, 0, 0, 6, 0, 0]

# fill_fast(np.array(table).copy())  # 時間測定用

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
