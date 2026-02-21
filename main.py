import pygame
pygame.init()

WHITE = (255, 255, 255)

window = pygame.display.set_mode((0,0))
pygame.display.set_caption("NULL")

fps = pygame.time.Clock()
keys = pygame.key.get_pressed()

class Player:
    def __init__(self, x, y, width, heigt, images):
        self.images = [pygame.transform.scale(pygame.image.load(img), (width, heigt)) for img in images]
        self.walk_speed = 2
        self.ani_speed = 0.2
        self.index = 0
        self.hitbox = self.images[0].get_rect(topleft=(x,y))
        self.current_image = self.images[0]
        

    def show(self):
        window.blit(self.current_image, (self.hitbox.x, self.hitbox.y))

    def animate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.current_image = pygame.image.load(self.images[self.cycle])
            self.cycle = (self.cycle + 1) % len(self.images)
            self.hitbox.x -= self.walk_speed
            
walking_left_img = []
walking_right_img = []
images =  ["StandingStill_test.png","Walking_test1.png","Walking_test2.png"]
player = Player(50, 400, 60, 90, images)

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
    
    if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
        game = False



    
    window.fill(WHITE)
    player.show()
    player.animate()
    pygame.display.flip()
    fps.tick(60)

pygame.quit()