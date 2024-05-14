import numpy as np

grid = np.array([["#", "#", "#"],
                 ["#", "#", "#"], 
                 ["#", "#", "#"]])

running = True

def turn(whos_turn):
    
    print("Choose a coordinate ( 'x,y' )")
    coord = input()
    
    coordsplit = coord.split(",")
    
    x = int(coordsplit[0]) - 1
    y = int(coordsplit[1]) - 1
    
    if grid[y, x] == '#':
        grid[y, x] = whos_turn
    else:
        print("Space already taken")
        returnGrid(grid)
        turn(whos_turn)
    
    if whos_turn == "X":
        return "O"
    else:
        return "X"
    
def returnGrid(grid):
    
    for y in range(len(grid)):
        print("|".join(grid[y]))
        if y < 2:
            print("-+-+-")

def checkGrid(grid, running):
    
    for y in range(len(grid)):
        row_check = np.unique(np.array([grid[y]]))
        
        if row_check.size == 1 and not row_check == '#':
            running = False

    for x in range(len(grid)):
        col_check = np.unique(np.array([i[x] for i in grid]))
        if col_check.size == 1 and not col_check == '#':
            running = False
    
    diag_check = np.unique(np.array([i[i] for i in range(grid.size)]))
    if diag_check.size == 1 and not diag_check == '#':
        running = False
    
    inverted_grid = grid[::-1]
    inverted_diag_check = np.unique(np.array([i][i] for i in range(inverted_grid.size)))
    if inverted_diag_check.size == 1 and not inverted_diag_check == '#':
        running = False
    
    return running
        
def play(whos_turn, running):
    
    while running:
        
        whos_turn = turn(whos_turn)
    
        returnGrid(grid)
        
        running = checkGrid(grid, running)

play("X", running)
    
