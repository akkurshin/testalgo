from pygame import *


w = 700
h = 500
window = display.set_mode((w,h))
window.fill((201, 248, 247))
clock = time.Clock()
FPS = 60


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
        if keys[K_DOWN] and self.rect.y < w - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < w - 80:
            self.rect.y += self.speed

racket1 = Player('racket.jpg', 50, 215, 10, 10, 70)
racket2 = Player('racket.jpg', 650, 215, 10, 10, 70)

while True:
    for e in event.get():
        if e.type == QUIT:
            break
    window.fill((201, 248, 247))
    racket1.update()
    racket1.reset()
    racket2.update()
    racket2.reset()

    display.update()
    clock.tick(FPS)