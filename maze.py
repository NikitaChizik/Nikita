from pygame import *

init()

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")

clock = time.Clock()
FPS = 60
bg = image.load("background.jpg")
bg = transform.scale(bg,(win_width,win_height))

run = True

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed):
        super().__init__()
        self.image = image.load(img)
        self.image = transform.scale(self.image,(55,55))

        self.speed = speed

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.naprv ="right"

    def show_s(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Hero(GameSprite):
    def dvij(self):
        key_p = key.get_pressed()
        if key_p[K_a] and self.rect.x > 10:
            self.rect.x -= self.speed
        if key_p[K_d] and self.rect.x < win_width - 60:
            self.rect.x += self.speed

        if key_p[K_s] and self.rect.y < win_height - 60:
            self.rect.y += self.speed
        if key_p[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed

class Vrag(GameSprite):
    def dvij(self): 
        if self.rect.x < 300:
            self.naprv = "right"
        elif self.rect.x > 600:
            self.naprv = "left"

        if self.naprv == "left":
            self.rect.x -= self.speed
        if self.naprv == "right":
            self.rect.x += self.speed 

class Stena(sprite.Sprite):
    def __init__(self, x,y, w,h, r,g,d):
        super().__init__()

        self.stena = Surface((w, h))
        self.stena.fill((r,g,d))
        self.stena_rect = self.stena.get_rect()
        self.stena_rect.x = x
        self.stena_rect.y = y

    def show_s(self):
        window.blit(self.stena, (self.stena_rect.x, self.stena_rect.y))
    

    

player = Hero("hero.png", 20, 400, 5)
vrag = Vrag("cyborg.png", 400,200, 3)
stena1 = Stena(594,200,100,10,100,100,100)
stena2 = Stena(304,200,100,10,100,100,100)
stena3 = Stena(394,200,100,10,100,100,100)
stena4 = Stena(494,200,10,300,100,100,100)
stena5 = Stena(600,390,100,10,100,100,100)
print(stena4.stena_rect)
while run:        
    for i in event.get():
        if i.type == QUIT:
            run = False

    window.blit(bg, (0,0))
    player.show_s()
    player.dvij()
    vrag.show_s()
    vrag.dvij()
    stena1.show_s()
    stena2.show_s()
    stena3.show_s()
    stena4.show_s()
    stena5.show_s()
    if sprite.collide_rect(player, vrag):
        player = Hero("hero.png", 20, 400, 5)
 
 
 
    if stena1.stena_rect.colliderect(player) or stena2.stena_rect.colliderect(player) or stena3.stena_rect.colliderect(player) or stena4.stena_rect.colliderect(player) or stena5.stena_rect.colliderect(player):  
        player = Hero("hero.png", 20, 400, 5)
    display.update()
    clock.tick(FPS)

