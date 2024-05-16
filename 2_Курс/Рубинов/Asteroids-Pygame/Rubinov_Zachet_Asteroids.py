
import pygame, sys, os, random, math
from pygame.locals import *
from SpritesCL import Sprite

pygame.mixer.pre_init()
pygame.init()                      
fps = pygame.time.Clock()

#Цвета
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

#Глобальные
w = 800
h = 600
time = 0
score = 0
lives = 3
started = False

window = pygame.display.set_mode((w, h), 0, 32)
pygame.display.set_caption('Астеройды')

def angle_to_vector(ang):
    return [math.cos(ang), -math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)

#Класс для картинок
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

#Класс для корабля
class Ship:
    def __init__(self, pos, vel, angle, image, thrust_image, info):
        self.pos = [pos[0]-45,pos[1]-45]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.thrust_image = thrust_image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.forward = [0,0]

    def shoot(self):
        global a_missile
        missile_pos = [self.pos[0]+40 + self.radius * self.forward[0], self.pos[1]+40 + self.radius * self.forward[1]]
        missile_vel = [self.vel[0] + 6 * self.forward[0], self.vel[1] + 6 * self.forward[1]]
        missile_group.add(Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info))

    def set_thrust(self, thrust):
        self.thrust = thrust


    def get_position(self):
        return (int(self.pos[0] + self.radius), int(self.pos[1] + self.radius))

    def get_radius(self):
        return self.radius

    def draw(self,canvas):
        if self.thrust:
            canvas.blit(rot_center(self.thrust_image, self.angle), self.pos)
        else:
            canvas.blit(rot_center(self.image, self.angle), self.pos)

    def update(self):
        acc = 0.5
        fric = acc / 20
        self.angle += self.angle_vel
        self.forward = angle_to_vector(math.radians(self.angle))
        if self.thrust:
            self.vel[0] += self.forward[0] * acc
            self.vel[1] += self.forward[1] * acc
        self.vel[0] *= (1 - fric)
        self.vel[1] *= (1 - fric)
        self.pos[0] = (self.pos[0] + self.vel[0]) % (w - self.radius)
        self.pos[1] = (self.pos[1] + self.vel[1]) % (h - self.radius)

    def set_angle_vel(self, vel):
        self.angle_vel = vel

def load_sliced_sprites( w, h, filename):
    images = []
    master_image = pygame.image.load(os.path.join('images', filename)).convert_alpha()
    master_width, master_height = master_image.get_size()
    for i in range(int(master_width/w)):
    	images.append(master_image.subsurface((i*w,0,w,h)))
    return images



#Изображения
explosion_images = load_sliced_sprites(128, 128, 'explosion.png')
explosion_info = ImageInfo([64,64], [128,128], 64, 24, True)
space = pygame.image.load(os.path.join('images','Fon.jpg'))
tuman = pygame.image.load(os.path.join('images','tuman.png'))
ship_image = pygame.image.load(os.path.join('images','ship.png'))
ship_info = ImageInfo([45,45], [90,90], 45)
thrusted_ship_image = pygame.image.load(os.path.join('images','ship_thrusted.png'))
thrusted_ship_info = ImageInfo([45,45], [90,90], 45)
rock_image = pygame.image.load(os.path.join('images','asteroid.png'))
rock_info = ImageInfo([45,45], [90,90],45)
missile_image = pygame.image.load(os.path.join('images','shot2.png'))
missile_info = ImageInfo([5,5], [10,10], 5, 50)
splash = pygame.image.load(os.path.join('images','start.png'))


#Создание объектов
Korabl = Ship([w//2, h//2], [0,0], 0, ship_image, thrusted_ship_image, ship_info)
rock_group = set([])
missile_group = set([])
explosion_group = set([])



def process_sprite_group(canvas):
    
    for rock in rock_group:
        rock.draw(canvas)
        rock.update()
        
    for missile in list(missile_group):
        missile.draw(canvas)
        if missile.update():
            missile_group.remove(missile)

    for explosion in explosion_group:
        explosion.draw(canvas)


#Столкновение
def group_collide(group,other_object):
    counter = len(group)
    for element in list(group):
        if element.collide(other_object):
            explosion_group.add(Sprite([element.get_position()[0] - 3*element.radius,element.get_position()[1] - 3*element.radius], [0,0], 0, 0, explosion_images, explosion_info))
            group.remove(element)
    return counter - len(group)

def group_group_collide(first_group, second_group):
    counter = 0
    for element in list(first_group):
        if group_collide(second_group,element) > 0:
            counter += 1
            first_group.remove(element)
    return counter


#Отрисовка
def draw(canvas):
    global score,lives,started
    
    canvas.fill(BLACK)
    canvas.blit(space,(0,0))
    canvas.blit(tuman,(time*.6,0))
    canvas.blit(tuman,(time*.3-w,0))

    Korabl.draw(canvas)

    if started:
        process_sprite_group(canvas)
        Korabl.update()
        if group_collide(rock_group,Korabl) > 0:
            if lives > 1:
                lives -= 1
            else:
                lives = 0
                started=False
        hits = group_group_collide(missile_group, rock_group)
        if hits > 0:
            score += hits;
    else:
        canvas.blit(splash, (w//2 - 400, h//2 - 150))

    #Счёт
    myfont1 = pygame.font.SysFont("Times New Roman", 20)
    label1 = myfont1.render("Жизни : "+str(lives), 1, (255,0,0))
    canvas.blit(label1, (50,20))

    myfont2 = pygame.font.SysFont("Times New Roman", 20)
    label2 = myfont2.render("Счёт : "+str(score), 1, (255,0,0))
    canvas.blit(label2, (670, 20))

#Кручение вокруг своей оси
def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
    
#Клавиши
def keydown(event):
    ang_vel = 4.5
    if event.key == K_LEFT:
        Korabl.set_angle_vel(ang_vel)
    if event.key == K_RIGHT:
        Korabl.set_angle_vel(-ang_vel)
    if event.key == K_UP:
        Korabl.set_thrust(True)
    if event.key == K_SPACE:
        Korabl.shoot()

def keyup(event):
    if event.key in (K_LEFT,K_RIGHT):
        Korabl.set_angle_vel(0)
    if event.key == K_UP:
        Korabl.set_thrust(False)

# Таймер
def timer():
    global time
    if time <= w:
        time += 1
        if time % 30 == 0:
            rock_spawner()
    else:
        time = 0

#Появление Астеройдов
def rock_spawner():
    global rock_group,started
    if len(rock_group) < 12 and started:
        while 1:
            random_pos = [random.randrange(0, w), random.randrange(0, h)]
            if dist(random_pos,Korabl.get_position()) <= rock_info.get_radius() + 2 * Korabl.get_radius():
                continue
            else:
                rock_pos = random_pos
                break
        increase = score/100
        rock_vel = [random.random() * (3 + increase) - (1 + increase), random.random() * (3 + increase) - (1 + increase)]
        rock_avel = random.random() * 6 - 1
        rock_group.add(Sprite(rock_pos, rock_vel, 0, rock_avel, rock_image, rock_info))

def click(event):
    global started, lives, score, rock_group, missile_group, Korabl
    if event.button == 1 and event.pos[0] in range(w//2 - 200, w//2 + 200) and event.pos[1] in range(h//2 - 150, h//2 + 150) and not started:
        started = True
        lives = 3
        score = 0
        rock_group = set([])
        missile_group = set([])


while True:
    draw(window)
    timer()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == MOUSEBUTTONDOWN:
            click(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    fps.tick(60)
