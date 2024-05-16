import pygame
import random

from os import path

img_dir = path.join(path.dirname(__file__), 'img')

WHITE = (255, 255, 255)
cosmos = (0, 59, 89)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
score = 0

width = 500  # ширина игрового окна
height = 800 # высота игрового окна
game_speed = 40 # частота кадров в секунду
pygame.mixer.init()
pygame.init()

firing_mode_laser=False;
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Простые астероиды/Глущенко")
clock = pygame.time.Clock()


font_name = pygame.font.match_font('arial')
def text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, GREEN)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Rocket(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = rocket_img
        self.image = pygame.transform.scale(rocket_img, (40, 60))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.movey = -20

    def update(self):
        self.rect.y += self.movey
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 400))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.movey = -20

    def update(self):
        self.rect.y += self.movey
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = asteroid_img
        self.image = pygame.transform.scale(asteroid_img, (30, 42))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-140, -60)
        self.movey = random.randrange(2, 12)
        self.movex = random.randrange(-5, 5)
        self.radius = int(self.rect.width / 2)

    def update(self):
        self.rect.y += self.movey
        self.rect.x += self.movex
        if self.rect.top > height + 10 or self.rect.left < -45 or self.rect.right > width + 40:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-140, -60)
            self.movey = random.randrange(2, 12)
class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spaceship_img
        self.image = pygame.transform.scale(spaceship_img, (70, 80))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height - 10
        self.movex = 0
        self.movey = 0
        self.radius = int(self.rect.width / 2)

    def update(self):
        self.movex = 0
        self.movey = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.movex = -12
        if keystate[pygame.K_d]:
            self.movex = 12
        if keystate[pygame.K_s]:
            self.movey = +12
        if keystate[pygame.K_w]:
            self.movey = -12
        self.rect.x += self.movex
        self.rect.y += self.movey
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top > height-80:
            self.rect.top = height-80
        if self.rect.bottom < height-160:
            self.rect.bottom = height-160

    def shoot(self):
        rocket = Rocket(self.rect.centerx, self.rect.top)
        all_sprites.add(rocket)
        rockets.add(rocket)
    def shoot_laser(self):
        laser = Laser(self.rect.centerx, self.rect.top)
        all_sprites.add(laser)
        lasers.add(laser)

spaceship_img = pygame.image.load(path.join(img_dir, "SpaceShipNormal.png")).convert()
asteroid_img = pygame.image.load(path.join(img_dir, "asteroid1_grey.svg")).convert()
background = pygame.image.load(path.join(img_dir, 'spacefield_a-000.png')).convert()
rocket_img = pygame.image.load(path.join(img_dir, 'torpedo.svg')).convert()
laser_img = pygame.image.load(path.join(img_dir, 'projectile2.svg')).convert()
background_rect = background.get_rect()
all_sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
rockets = pygame.sprite.Group()
lasers = pygame.sprite.Group()
spaceship = Spaceship()
all_sprites.add(spaceship)
for i in range(8):
    aster = Asteroid()
    all_sprites.add(aster)
    asteroids.add(aster)
screen.fill(cosmos)
loop = True
while loop:

    clock.tick(game_speed) #Контроль скорости игры
    for event in pygame.event.get():
        # проверка на закрытие
        if event.type == pygame.QUIT:
           loop = False
        elif event.type == pygame.KEYDOWN:
            if firing_mode_laser==False and event.key == pygame.K_n:
                firing_mode_laser=True
            elif firing_mode_laser==True and event.key == pygame.K_n:
                firing_mode_laser = False
            if firing_mode_laser and event.key == pygame.K_SPACE:
                spaceship.shoot_laser()
            elif not firing_mode_laser and event.key == pygame.K_SPACE:
                spaceship.shoot()

    all_sprites.update()
    hits = pygame.sprite.groupcollide(asteroids, rockets, True, True)
    for hit in hits:
        aster = Asteroid()
        all_sprites.add(aster)
        asteroids.add(aster)
        score+=1
    hits = pygame.sprite.groupcollide(asteroids, lasers, True, False )
    for hit in hits:
        aster = Asteroid()
        all_sprites.add(aster)
        asteroids.add(aster)
        score += 1

    damage = pygame.sprite.spritecollide(spaceship, asteroids, False, pygame.sprite.collide_circle)
    if damage:
        loop = False


    # Рендеринг
    screen.fill(cosmos)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    text(screen, str(score), 18, 10, 10)
    pygame.display.flip()


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Конец игры")
clock = pygame.time.Clock()
running=True
while running:
    # Держим цикл на правильной скорости
    clock.tick(100)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = False
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
    text(screen, "Игра окончена! Ваш счет: " + str(score)+"Для выхода нажмите ENTER", 18, width / 2, height / 2)

    text(screen, "Для выхода нажмите ENTER", 18, width / 2, height / 2 - 20)

pygame.quit()