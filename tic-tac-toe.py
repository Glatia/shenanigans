import pygame

# Draws Grid
def drawGrid(surface, rows, width, dist):
  x = 0
  y = 0

  # For every row
  for i in range(rows-1):
    # Increase the x and y by the space between each row
    x = dist + x
    y = dist + y

    pygame.draw.line(surface, (17, 15, 15, 1), (0, y), (width, y), 8)
    pygame.draw.line(surface, (17, 15, 15, 1), (x, 0), (x, width), 8)

# Updates the window
def updateWindow(surface):
  
  color = (163, 161, 161, 1)
  font = pygame.font.SysFont('Arial', 2 * dist // 3)
  
  # Draws the Grid
  drawGrid(surface, rows, width, dist)
  drawLine(surface, winningLine[0], winningLine[1], gridRows)
  
  if drawWinner:
    
    if xo == "DRAW":
      
     text = font.render(xo, True, color)
    else:
      
      text = font.render(f"{xo} WINS", True, color)

    
    textRect = text.get_rect()
    textRect.center = width // 2, width // 2
    screen.blit(text, textRect)
    
  # Updates the Screen
  pygame.display.update()

def drawLine(surface, start, end, gridRows):
  
  if start is not None and end is not None:
    x = start.split(",")
    y = end.split(",")
    pygame.draw.line(surface, "black", (gridRows[int(x[1])].get(start).center), (gridRows[int(y[1])].get(end).center), 10)

# Checks to see which grid square was clicked
def checkClick(e):

  global xo
  
  for i in range(len(gridRows)):
    keys = gridRows[i].keys()
    
    for k in keys:
      
      if gridRows[i][k].collidepoint(e.pos):
        
        if gridRows[i][k] not in usedSquares:
          
          if xo == "X":
            xo = "O"
          else:
            xo = "X"
            
          fillSquare(screen, gridRows[i][k])
          updateGrid(grid, k, xo)
        else:
          
          continue

# Writes either an X or an O in the grid square
def fillSquare(surface, gridSquare):

  img = pygame.image.load(f"{xo}.png")
  img = pygame.transform.scale(img, (dist, dist))

  imgRect = img.get_rect()
  imgRect = gridSquare.topleft
  surface.blit(img, imgRect)
  
  # Makes sure that you cannot click on a square that is already in use
  usedSquares.append(gridSquare)

# Updates the grid variable based on which square was clicked and whose turn it was
def updateGrid(grid, gridSquare, xo):

  # The grid row keys are " 'X','Y' ", so splitting on the comma gives you the x and y values
  x = gridSquare.split(",")
  # Y (which row) | X (Which element in the row)
  grid[int(x[1])][int(x[0])] = xo
  print(grid)
  # Checks to see if someone won / there was a draw
  checkGrid(grid)


# Checks the grid for a winner / draw
def checkGrid(grid):

  
  global drawWinner, xo, winningLine

  # Loops through the three rows and checks to see if any of them have only one value (either 3 X's or 3 O's)
  for i in range(len(grid)):
    if len(set(grid[i])) == 1 and set(grid[i]) != {None}:
      winningLine = [f"0,{i}", f"2,{i}"]
      print(winningLine)
      drawWinner = True
      return

  # Gets the same index values from each row (ie, a column)
  for x in range(len(grid[0])):
    if len({grid[i][x] for i in range(len(grid))}) == 1 and {grid[i][x]} != {None}:
      drawWinner = True
      winningLine = [f"{x},0", f"{x},2"]
      print(winningLine)
    
      return

  # Checks the 2,0 to 0,2 diagnal by reversing grid and using the same algorithm
  reverseGrid = grid[::-1]
  if len({reverseGrid[i][i] for i in range(len(reverseGrid))}) == 1 and {reverseGrid[i][i] for i in range(len(reverseGrid))} != {None}:
    drawWinner = True
    winningLine = ["2,0", "0,2"]
    print(winningLine)
    
    return
    
  # If none of those, check if there is no blank spaces left, if there is, then its a draw
  gridCheck = 0
  for i in grid:
    if None not in i:
      gridCheck += 1
  else:
    if gridCheck == 3:
      xo = "DRAW"
      drawWinner = True
      
      return

# Main
def main():
  
  # Not really necessary but for some reason the fonts don't work without this
  pygame.init()
  
  global rows, width, dist, gridRows, screen, grid, xo, usedSquares, drawWinner, winningLine

  # Where the X and O values are stored and checked
  grid = [3*[None],
          3*[None], 
          3*[None]]

  xo = "O"
  drawWinner = False
  # Makes sure you can't click on a used square
  usedSquares = []

  # Screen stuff
  width = 369
  rows = 3
  dist = width // rows
  screen = pygame.display.set_mode((width, width))
  screen.fill((246, 23, 23, 1))
  pygame.display.set_caption("Tic Tac Toe")
  # Row dictionary with coordinates as a key
  row1 = {'0,0': pygame.Rect(0,0,dist,dist), '1,0': pygame.Rect(dist,0,dist,dist), '2,0': pygame.Rect(2*dist,0,dist,dist)}
  row2 = {'0,1': pygame.Rect(0,dist,dist,dist), '1,1': pygame.Rect(dist,dist,dist,dist), '2,1': pygame.Rect(2*dist,dist,dist,dist)}
  row3 = {'0,2': pygame.Rect(0,2*dist,dist,dist), '1,2': pygame.Rect(dist,2*dist,dist,dist), '2,2': pygame.Rect(2*dist,2*dist,dist,dist)}
  # The three rows make up the entire grid
  gridRows = [row1, row2, row3]
  # Creates an empty line
  winningLine = [None, None]
  
  # Initialize Gameloop
  running = True

  # Gameloop
  while running:
    
    # Event Loop
    for event in pygame.event.get():
      
      if event.type == pygame.QUIT:
        
        pygame.quit() 
      # If there is a click, check if its left click and check which square its on
      if event.type == pygame.MOUSEBUTTONDOWN:
        
        if drawWinner == False:
          
          if event.button == 1:
            checkClick(event)

      # Restart when R is pressed
      keys = pygame.key.get_pressed()
      if keys[pygame.K_r]:
        main()

    # Updates the window at the end of every loop
    updateWindow(screen)

# You guessed it, it starts the program
main()
