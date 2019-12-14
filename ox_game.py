class Mark:

    def __init__(self, owner, coords):
        self.owner = owner
        self.coords = coords


class Board:

    def __init__(self):
        self.board = [[" "] * 3 for _ in range(3)]

    def write(self, mark):
        row, col = mark.coords
        if self.board[row][col] != " ":
            raise Exception
        self.board[row][col] = "o" if mark.owner else "x"

    def isfinish(self):
        rows = [self.board[i] for i in range(3)]
        cols = [[self.board[i][j] for i in range(3)] for j in range(3)]
        diag = [[self.board[i][i] for i in range(3)], [self.board[i][-i-1] for i in range(3)]]

        for part in rows + cols + diag:
            if (len(set(part)) == 1) and (" " not in part):
                return True
        return False

    def __repr__(self):
        board = '\n'.join(
            ['|'.join(row) + f'|{i}' for i, row in enumerate(self.board, 1)]
        )
        return '=' * 8 + '\nA|B|C|\n' + board + '\n' + '=' * 8


board = Board()
turn = 0
while True:
    print(board)

    player = turn % 2
    print(f"player{player}: ", end="")

    try:
        row, col = input("行(123)と列(ABC)を入力してください。(1Aなど)\n")
        row = '123'.find(row)
        col = 'ABC'.find(col)
        coords = (row, col)
        if -1 in coords:
            continue
        board.write(Mark(player, coords))

    except (ValueError, Exception):
        print("無効な入力です")
        continue
    
    if board.isfinish():
        print(board)
        print(f"player{player}の勝ちです")
        break

    turn += 1