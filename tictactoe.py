grid = [["#", "#", "#"],
        ["#", "#", "#"], 
        ["#", "#", "#"]]

running = True

def turn(whos_turn):
    
    print("Choose a coordinate ( 'x,y' )")
    coord = input()
    
    coordsplit = coord.split(",")
    
    x = int(coordsplit[0]) - 1
    y = int(coordsplit[1]) - 1
    
    if grid[y][x] == '#':
        grid[y][x] = whos_turn
    else:
        print("Space already taken")
        returnGrid(grid)
        turn(whos_turn)
    
    if whos_turn == "X":
        return "O"
    else:
        return "X"
    
def returnGrid(grid):
    
    for y in grid:
        print("|".join(y))

def checkGrid(grid, running):
    for y in range(len(grid)):
        
        if len(set(grid[y])) == 1 and not set(grid[y]) == {'#'}:
            running = False
            
    for x in range(len(grid)):        
        if len(set(i[x] for i in grid)) == 1 and not set(i[x] for i in grid) == {'#'}:
            running = False
    
    if len(set(grid[i][i] for i in range(len(grid)))) == 1 and not set(grid[i][i] for i in range(len(grid))) == {'#'}:
        running = False
    
    inverted_grid = grid[::-1]
    if len(set(inverted_grid[i][i] for i in range(len(inverted_grid)))) == 1 and not set(inverted_grid[i][i] for i in range(len(inverted_grid))) == {'#'}:
        running = False
    
    return running
        
def play(whos_turn, running):
    
    while running:
        
        whos_turn = turn(whos_turn)
    
        returnGrid(grid)
        
        running = checkGrid(grid, running)

play("X", running)
    
