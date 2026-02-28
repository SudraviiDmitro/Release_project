import pygame
pygame.init()

WHITE = (255, 255, 255)

window = pygame.display.set_mode((0,0))
pygame.display.set_caption("NULL")

fps = pygame.time.Clock()
keys = pygame.key.get_pressed()

class Player:
    def __init__(self, x, y, width, heigt, image, images_left, images_right):
        self.images_left = [pygame.transform.scale(pygame.image.load(img), (width, heigt)) for img in images_left]
        self.images_right = [pygame.transform.scale(pygame.image.load(img), (width, heigt)) for img in images_right]
        self.image = pygame.transform.scale(pygame.image.load(image), (width, heigt))
        self.walk_speed = 2
        self.ani_speed = 0.09
        self.index = 0
        self.hitbox = self.image.get_rect(topleft=(x,y))
        self.current_image = self.image
        

    def show(self):
        window.blit(self.current_image, (self.hitbox.x, self.hitbox.y))

    def animate_left(self):
        if  event.type == pygame.KEYDOWN and keys[pygame.K_LEFT]:
            self.index += self.ani_speed
            self.hitbox.x -= self.walk_speed
            if self.index >= len(self.images_left):
                self.index = 0
            self.current_image = self.images_left[int(self.index)]

    def animate_right(self):
        if  event.type == pygame.KEYDOWN and keys[pygame.K_RIGHT]:
            self.index += self.ani_speed
            self.hitbox.x += self.walk_speed
            if self.index >= len(self.images_right):
                self.index = 0
            self.current_image = self.images_right[int(self.index)]

    def stand(self):
        if not event.type == pygame.KEYDOWN:
            self.current_image = self.image


class Door_l:
    def __init__(self, x, y, width, heigt, image):
        self.image = pygame.transform.scale(pygame.image.load(door_left), (width, heigt))
        self.hitbox = self.image.get_rect(topleft=(x,y))
        
    def show(self):
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))


class Door_r:
    def __init__(self, x, y, width, heigt, image):
        self.image = pygame.transform.scale(pygame.image.load(door_right), (width, heigt))
        self.hitbox = self.image.get_rect(topleft=(x,y))
        
        
    def show(self):
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))




            

images_left =  ["Walking_left1.png","Walking_left2.png"]
images_right = ["Walking_right1.png","Walking_right2.png"]
image = "Standing.png"

door_left = "Door_1.png"
door_right = "Door_2.png"

bg1 = pygame.image.load("room_1.png")
bg2 = pygame.image.load("room_2.png")
bg3 = pygame.image.load("room_3.png")
current_bg = bg1
player = Player(50, 400, 60, 90, image, images_left, images_right)

door_1 = Door_l(300, 370, 80, 120, door_left)
door_2 = Door_r(800, 370, 80, 120, door_right)
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
    
    if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
        game = False



    if player.hitbox.colliderect(door_1.hitbox) and keys[pygame.K_e]:
        current_bg = bg2

    if player.hitbox.colliderect(door_2.hitbox) and keys[pygame.K_e]:
        current_bg = bg3



    
    window.blit(current_bg, (100,110))
    player.show()
    player.animate_left()
    player.animate_right()
    player.stand()
    door_1.show()
    door_2.show()
    pygame.display.flip()
    fps.tick(60)

pygame.quit()