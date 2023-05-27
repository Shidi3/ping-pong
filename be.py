import pygame
pygame.init()
from random import randint

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, img, speed_x, speed_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        a = randint(0, 1)
        if a == 1:
            self.speed_y = speed_y
        elif a == 0:
            self.speed_y = speed_y * -1
        b = randint(0, 1)
        if b == 1:
            self.speed_x = speed_x
        elif b == 0:
            self.speed_x = speed_x * -1


    def draw(self, win):
        win.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1
        is_catch = pygame.sprite.collide_rect(self, player1)
        if is_catch:
            self.speed_x *= -1
            self.speed_y *= -1
        is_catch = pygame.sprite.collide_rect(self, player2)
        if is_catch:
            self.speed_x *= -1
            self.speed_y *= -1

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, img, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self, win):
        win.blit(self.image, self.rect)

    def update_r(self):
        y_old = self.rect.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN] and self.rect.bottom < 600:
            self.rect.y += self.speed

    def update_l(self):
        y_old = self.rect.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif keys[pygame.K_s] and self.rect.bottom < 600:
            self.rect.y += self.speed

    def schet(self, s):
        text_go = font.render('Счет:', 1, (160, 202, 223))
        text_rect = text_go.get_rect()
        text_rect.center = (W // 2, H // 2)
        win.blit(text_go, text_rect)


win = pygame.display.set_mode((1520, 600))
run = True
clock = pygame.time.Clock()
fon = pygame.image.load('p.webp')
fon = pygame.transform.scale(fon, (1520, 600))
pygame.display.set_caption('Юньмэн. Пристань лотоса.')
fps = 60

font = pygame.font.Font('ofont.ru_Saytag.ttf', 70)
font1 = pygame.font.Font('ofont.ru_Saytag.ttf', 71)

player1 = Player(100, 300, 40, 106, 'plat.png', 5)
player2 = Player(1420, 300, 40, 106, 'plat.png', 5)
ball = Ball(760, 300, 50, 50, 'ball.png', 5, 5)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.blit(fon, (0,0))
    player1.draw(win)
    player1.update_l()
    player2.draw(win)
    player2.update_r()
    ball.draw(win)
    ball.update()
    pygame.display.update()
    clock.tick(fps)