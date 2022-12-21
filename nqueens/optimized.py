# ---------------------------------------------------------- libraries ---------------------------------------------------------- #

import rich

# ---------------------------------------------------------- constants ---------------------------------------------------------- #

DIM = 8

# ------------------------------------------------------------ utils ------------------------------------------------------------ #

def blue(x, end = '\n'):
    if x == 1:
        rich.print(f"[bold cyan]+[/bold cyan]", end=end)
    else:
        rich.print(f"[bold cyan]{x}[/bold cyan]", end=end)


def red(x, end = '\n'):
    if x == 0:
        rich.print(f"[bold red]x[/bold red]", end=end)
    else:
        rich.print(f"[bold red]{x}[/bold red]", end=end)

def bprint(arr, b = None, r = None):
    for row in arr:
        for ele in row:
            if ele == b:
                blue(ele, end="  ")
            elif ele == r:
                red(ele, end="  ")
            else:
                print(ele, end="  ")
        print()

# ---------------------------------------------------------- driver code ---------------------------------------------------------- #

board = [[0 for _ in range(DIM)] for _ in range(DIM)]

def available(board, x, y):
    if board[x][y] == 1:
        return False
    
    for i in range(DIM):
        if board[i][y] == 1:
            return False

    for j in range(DIM):
        if board[x][j] == 1:
            return False

    # top right
    i, j = x + 1, y + 1
    while i < DIM and i > -1 and j < DIM and j > -1:
        if board[i][j] == 1:
            return False
        i += 1
        j += 1

    # top left
    i, j = x - 1, y + 1
    while i < DIM and i > -1 and j < DIM and j > -1:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    # bottom left
    i, j = x - 1, y - 1
    while i < DIM and i > -1 and j < DIM and j > -1:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # bottom right
    i, j = x + 1, y - 1
    while i < DIM and i > -1 and j < DIM and j > -1:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

# ---------------------------------------------------------- n-queen ---------------------------------------------------------- #

def nqueen(board):
    queens = sum([sum(p) for p in board])
    if queens == DIM:
        bprint(board, 1, 0)
        print()
        return True
    else:
        for i in range(DIM):
            for j in range(DIM):
                if available(board, i, j):
                    board[i][j] = 1
                    if nqueen(board):
                        return True

                    board[i][j] = 0
        
        return False

# ---------------------------------------------------------- main ---------------------------------------------------------- #

if __name__ == "__main__":
    nqueen(board)

# -------------------------------------------------------------------------------------------------------------------------- #
