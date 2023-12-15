import pygame

pygame.init()

width = 400

paddleWidth = 10
paddleHeight = 50

ballSize = 15

font = pygame.font.Font("pong/Pixel.ttf", width // 10)

screen = pygame.display.set_mode((width, width))

screen.fill("black")

class Players(pygame.sprite.Sprite):

  def __init__(self, x, y):

    self.pos = pygame.Rect(x, y, paddleWidth, paddleHeight)

  def move(self, u, d):
    
    if u and self.pos.y <= 0 or d and self.pos.y >= width - paddleHeight:
      pass
    else:
      self.pos.y += (d - u) * 10

  def draw(self, surface):
    
    pygame.draw.rect(surface, "white", self.pos)


class Ball(pygame.sprite.Sprite):

  def __init__(self, x, y):
    
    self.pos = pygame.Rect(x - ballSize, y - ballSize, ballSize, ballSize)
    self.vel = pygame.math.Vector2((5, 5))
    self.ballSize = ballSize

  def move(self):
        
    self.pos.x += int(self.vel[0])
    self.pos.y += int(self.vel[1])

  def update(self, players, width, surface):
    
    p1 = players[0]
    p2 = players[1]
    
    if p1.pos.colliderect(self.pos) or p2.pos.colliderect(self.pos):
      self.vel.x = -self.vel.x
    elif self.pos.y < 0 or self.pos.y > width - self.ballSize:
      self.vel.y = -self.vel.y
      
    if self.pos.x < 0:
      win("Player 1", surface)
    elif self.pos.x > width - self.ballSize:
      win("Player 2", surface)

  def draw(self, surface):

    pygame.draw.rect(surface, "white", self.pos)

def win(who, surface):
  
  text = font.render(f"{who} Wins", True, "White")
  textRect = text.get_rect()
  textRect.center = (width // 2, width // 2)
  surface.blit(text, textRect)



def main():
  settings = {"Difficulty" : "", "Mode" : ""}
  menu = True
  
  pygame.init()

  player1 = Players(0, width // 2)
  player2 = Players(width - paddleWidth, width // 2)
  players = [player1, player2]
  ball = Ball(width//2, 0 + ballSize)

  menubtns = {"Hard" : pygame.Rect(width // 9, width // 5, 100, 50), "Medium" : pygame.Rect(width // 9, 2 * width // 5, 100, 50), "Easy" : pygame.Rect(width // 9, 3 * width // 5, 100, 50)}
  
  clock = pygame.time.Clock()
  
  running = True
  
  while running:
    
    clock.tick(30)
    screen.fill("black")
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        running = False
        
    if not menu:
      
  
      keys = pygame.key.get_pressed()
      if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
        player2.move(keys[pygame.K_UP], keys[pygame.K_DOWN])
  
      if keys[pygame.K_w] or keys[pygame.K_s]:
        player1.move(keys[pygame.K_w], keys[pygame.K_s])
  
      if keys[pygame.K_r]:
        main()
      
      pygame.draw.line(screen, "gray", (width // 2, 0), (width // 2, width), 5)
  
      ball.update(players, width, screen)
      ball.move()
      ball.draw(screen)
      player1.draw(screen)
      player2.draw(screen)
      
    elif menu:
      
      keys = pygame.key.get_pressed()
      if keys[pygame.K_SPACE]:
        menu = False
      for key,btn in menubtns.items():
        pygame.draw.rect(screen, "gray", btn, 2, 9)
        font2 = pygame.font.Font("pong/Pixel.ttf", 20)
        text = font2.render(key, True, "White")
        textRect = text.get_rect()
        textRect.center = btn.center
        
        screen.blit(text, textRect)
      
    pygame.display.flip()

main()

pygame.quit()
