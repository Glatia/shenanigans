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

    pygame.draw.line(surface, (56, 80, 117), (0, y), (width, y), 8)
    pygame.draw.line(surface, (56, 80, 117), (x, 0), (x, width), 8)

# Updates the window
def updateWindow(surface):
  
  color = (145, 171, 255)
  font = pygame.font.SysFont('Arial', 75)
  # Draws the Grid
  drawGrid(surface, rows, width, dist)
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

  font = pygame.font.SysFont("Arial", 100)
  text = font.render(xo, True, (29, 52, 99))
  
  textRect = text.get_rect()
  
  textRect.center = gridSquare.center
  
  surface.blit(text, textRect)
  # Makes sure that you cannot click on a square that is already in use
  usedSquares.append(gridSquare)

# Updates the grid variable based on which square was clicked and whose turn it was
def updateGrid(grid, gridSquare, xo):

  # The grid row keys are " 'X','Y' ", so splitting on the comma gives you the x and y values
  x = gridSquare.split(",")
  grid[int(x[1])][int(x[0])] = xo

  # Checks to see if someone won / there was a draw
  checkGrid(grid)

# Checks the grid for a winner / draw
def checkGrid(grid):
  global drawWinner, xo
  diagArray = []

  # Loops through the three rows and checks to see if any of them have only one value (either 3 X's or 3 O's)
  for i in range(len(grid)):
    if len(set(grid[i])) == 1 and not set(grid[i]) == {0}:
      drawWinner = True
      return

  # Gets the same index values from each row (ie, a column)
  if len(set([i[0] for i in grid])) == 1 and not set([i[0] for i in grid]) == {0}:
    drawWinner = True
    return
  if len(set([i[1] for i in grid])) == 1 and not set([i[1] for i in grid]) == {0}:
    drawWinner = True
    return
  if len(set([i[2] for i in grid])) == 1 and not set([i[2] for i in grid]) == {0}:
    drawWinner = True
    return

  # Checks the 0,0 to 3,3 diagnal, if it has only one value, it is a winner
  for i in range(len(grid)):
    diagArray.append(grid[i][i])
  if len(set(diagArray)) == 1 and not set(diagArray) == {0}:
    drawWinner = True
    return

  # Checks the 3,0 to 0,3 diagnal
  diagArray.clear()
  reverseGrid = grid[::-1]
  for i in range(len(reverseGrid)):
    diagArray.append(reverseGrid[i][i])
  if len(set(diagArray)) == 1 and not set(diagArray) == {0}:
    drawWinner = True
    return

  # If none of those, check if there is no blank spaces left, if there is, then its a draw
  if 0 not in grid[0] and 0 not in grid[1] and 0 not in grid[2]:
    xo = "DRAW"
    drawWinner = True
    return

# Main
def main():
  
  # Not really necessary but for some reason the fonts don't work without this
  pygame.init()
  
  global rows, width, dist, gridRows, gridColumns, screen, grid, xo, usedSquares, drawWinner

  # Where the X and O values are stored and checked
  grid = [[0, 0, 0],
          [0, 0, 0], 
          [0, 0, 0]]

  xo = "O"
  drawWinner = False
  # Makes sure you can't click on a used square
  usedSquares = []

  # Screen stuff
  width = 300
  rows = 3
  dist = width // rows
  screen = pygame.display.set_mode((width, width))
  screen.fill((95, 136, 201))
  pygame.display.set_caption("Tic Tac Toe")
  # Row dictionary with coordinates as a key
  row1 = {'0,0': pygame.Rect(0,0,dist,dist), '1,0': pygame.Rect(dist,0,dist,dist), '2,0': pygame.Rect(2*dist,0,dist,dist)}
  row2 = {'0,1': pygame.Rect(0,dist,dist,dist), '1,1': pygame.Rect(dist,dist,dist,dist), '2,1': pygame.Rect(2*dist,dist,dist,dist)}
  row3 = {'0,2': pygame.Rect(0,2*dist,dist,dist), '1,2': pygame.Rect(dist,2*dist,dist,dist), '2,2': pygame.Rect(2*dist,2*dist,dist,dist)}
  # The three rows make up the entire grid
  gridRows = [row1, row2, row3]

  # Initialize Gameloop
  running = True

  # Gameloop
  while running:
    
    pygame.time.delay(10)
    
    # Event Loop
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit() 
      # If there is a click, check if its left click and check which square its on
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          checkClick(event)

    # Updates the window at the end of every loop
    updateWindow(screen)
main()
