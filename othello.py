from dataclasses import dataclass


@dataclass
class Stone:
    color:bool
    position:tuple

    def reverse(self):
        self.color = not self.color

@dataclass
class Board:
    stones:list = []

    def set_(self, stone:Stone):
        
        self.stones.append(stone)
    def __repr__(self):
        board = [[" "] * 8 for _ in range(8)]
        for stone in self.stones:
            i, j = stone.position
            board[i][j] = "●" if stone.color else "○"
        col_index = "abcdefgh"
        col_index = " |" + "|".join(col_index) + "|\n"
        return col_index + "\n".join( [f"{i}|" + "|".join(row) + "|" for i, row in enumerate(board, 1)] )

def play():

    board = Board()
    init_stones = (Stone(1, (3, 3)), Stone(0, (3, 4)), Stone(0, (4, 3)), Stone(1, (4, 4)))
    for init_stone in init_stones:
        board.set_(init_stone)
    turn = 0

    while True:
        print(board)
        color = turn % 2

        print("{}番です".format("●" if color else "○"))
        x, y = input("石を置くマス目を入力してください(例: f4): ")
        position = ("12345678".find(y), "abcdefgh".find(x))
        stone = Stone(color, position)
        board.set_(stone)

        turn += 1

if __name__ == "__main__":
    play()