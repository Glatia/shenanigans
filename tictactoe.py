import numpy as np

grid = np.array (
    [["#", "#", "#"],
     ["#", "#", "#"], 
     ["#", "#", "#"]]
    )

running = True

def turn(whos_turn, running):

    print("Choose a coordinate ('x,y')")
    coord = input()

    coordsplit = coord.split(",")

    x = int(coordsplit[0]) - 1
    y = int(coordsplit[1]) - 1

    if grid[y, x] == '#':
        grid[y, x] = whos_turn
    else:
        
        print("Space already taken")
        returnGrid(grid)
        turn(whos_turn, running)


def returnGrid(grid):

    for y in range(len(grid)):
        print("|".join(grid[y]))
        
        if y < 2:
            print("-+-+-")

def checkGrid(grid, running):

    for y in range(len(grid)):
        row_check = np.unique (
            np.array (
                [grid[y]]
            )
        )

        if row_check.size == 1 and row_check != '#':
            running = False

    for x in range(len(grid)):
        col_check = np.unique (
            np.array (
                [i[x] for i in grid]
            )
        )
        
        if col_check.size == 1 and col_check != '#':
            running = False

    diag_check = np.unique (
        np.array(
            [grid[i,i] for i in range(len(grid))]
        )
    )
    
    if diag_check.size == 1 and diag_check != '#':
        running = False

    inverted_grid = grid[::-1]
    inverted_diag_check = np.unique(
                                    np.array (
                                        [inverted_grid[i, i] for i in range(len(grid))]
                                    )
                                  )
    
    if inverted_diag_check.size == 1 and inverted_diag_check != '#':
        running = False

    return running

def play(whos_turn, running):

    while running:

        turn(whos_turn, running)
        
        running = checkGrid(grid, running)
        
        returnGrid(grid)
        
        if running:
            
            whos_turn = "O" if whos_turn == "X" else "X"

    print(f"{whos_turn} Wins!")

play("X", running)
