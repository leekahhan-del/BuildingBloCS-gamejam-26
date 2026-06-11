import pygame

pygame.init()

sw = 800
sh = 600
size = sw, sh

s = pygame.display.set_mode(size)

clock = pygame.time.Clock()

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xvel = 0
        self.yvel = 0
        self.inventory = []
    
    def move(self, key):
        ix = False
        iy = False
        if key[pygame.K_UP] or key[pygame.K_w]:
            self.yvel -= 3
            iy = True
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.yvel += 3
            iy = True
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.xvel -= 3
            ix = True
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.xvel += 3
            ix = True

        if not ix:
            self.xvel *= 0.5
        if not iy:
            self.yvel *= 0.5
        
        self.xvel = max(-10, min(10, self.xvel))
        self.yvel = max(-10, min(10, self.yvel))

        self.x += self.xvel
        self.y += self.yvel
    
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, 50, 50))
        
p1 = Player(sw/2 - 50, sh/2 - 50)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    s.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    p1.move(keys)
    p1.draw(s)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
