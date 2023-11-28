import pygame

def drawGrid(surface):
  x = 0
  y = 0
  
  for i in range(rows-1):
    x = dist + x
    y = dist + y

    pygame.draw.line(surface, "white", (x, 0), (x, width))
    pygame.draw.line(surface, "white", (0, y), (width, y))
  
def checkClick(e, grid, surface):
  keys = grid.keys()
  for k in keys:
    if grid[k].collidepoint(e.pos):
      drawnSquares.append(grid[k])
      
def updateWindow(surface):
  surface.fill('black')
  
  drawGrid(surface)
  for s in drawnSquares:
    pygame.draw.rect(surface, "white", s)
    
  pygame.display.flip()

def main():
  
  global width, rows, dist, xo, grid, drawnSquares
  width = 300
  rows = 3
  dist = width // rows
  xo = 0
  drawnSquares = []
  grid = dict(topLeft = pygame.Rect(0, 0, dist, dist), topMid = pygame.Rect(dist, 0, dist, dist), topRight = pygame.Rect(2 * dist, 0, dist, dist), midLeft = pygame.Rect(0, dist, dist, dist), midMid = pygame.Rect(dist, dist, dist, dist), midRight = pygame.Rect(2 * dist, dist, dist, dist), bottomLeft = pygame.Rect(0, 2 * dist, dist, dist), bottomMid = pygame.Rect(dist, 2 * dist, dist, dist), bottomRight = pygame.Rect(2 * dist, 2 * dist, dist, dist))
  screen = pygame.display.set_mode((width, width))
  pygame.init()
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          checkClick(event, grid, screen)
          
      updateWindow(screen)
    
main()
