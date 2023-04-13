from pygame import *


w = 700
h = 500
window = display.set_mode((w,h))
window.fill((201, 248, 247))
clock = time.Clock()
FPS = 60

font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, speed_x, speed_y, wight, height):
        super().__init__(player_image, player_x, player_y, speed_x, wight, height)
        self.speed_2 = speed_y
    
    def update(self, racket1, racket2):
        self.rect.x += self.speed
        self.rect.y += self.speed_2
        if sprite.collide_rect(self, racket1):
            self.speed *= -1
        if sprite.collide_rect(self, racket2):
            self.speed *= -1
        if self.rect.y < 0:
            self.speed_2 *= -1
        if self.rect.y > 470:
            self.speed_2 *= -1

racket1 = Player('racket.jpg', 50, 215, 10, 10, 70)
racket2 = Player('racket.jpg', 650, 215, 10, 10, 70)
ball = Ball('racket.jpg', 350, 250, 5, 5, 30, 30)
game = True
start = False

font = font.SysFont('Arial', 30)
starttext = font.render("PRESS SPACE TO START", font, (0,0,0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN and e.key == K_SPACE:
            start = True
    window.fill((201, 248, 247))
    if start == False:
        window.blit(starttext, (200,200))

    if start:
        racket1.update_l()
        racket1.reset()
        racket2.update_r()
        racket2.reset()
        ball.reset()
        ball.update(racket1, racket2)
        if ball.rect.x > 700 or ball.rect.x < 0:
            start = False
            ball.rect.x = 350
            ball.rect.y = 250

    display.update()
    clock.tick(FPS)