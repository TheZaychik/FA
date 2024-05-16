import pygame, sys, os, random, math
from pygame.locals import *
from II import PictureData # Настройки изображений
from PreSet import *
from helper_functions import *
from load_img import *
from aster import Asteroid
pygame.mixer.pre_init()
pygame.init()                      
fps = pygame.time.Clock()


#Настройки холста через импортированные данные
display = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Астероиды/Зачет/Глущенко')

class SpaceShip:
    def __init__(self, position, speed, angle, image, boosted_image, info):
        self.position = [position[0]-45,position[1]-45]
        self.speed = [speed[0],speed[1]]
        self.boost = False
        self.angle = angle
        self.angle_speed = 0
        self.image = image
        self.boosted_image = boosted_image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.forward = [0,0]

    def shoot(self):
        global a_missile

        rocket_pos = [self.position[0]+40 + self.radius * self.forward[0], self.position[1]+40 + self.radius * self.forward[1]]

        rocket_vel = [self.speed[0] + 6 * self.forward[0], self.speed[1] + 6 * self.forward[1]]
        rocket_group.add(Asteroid(rocket_pos, rocket_vel, self.angle, 0, rocket_image, rocket_info))

    def set_boost(self, boost):
        self.boost = boost


    def get_position(self):
        return (int(self.position[0] + self.radius), int(self.position[1] + self.radius))

    def get_radius(self):
        return self.radius

    def draw(self,area):
        if self.boost:
            area.blit(rot_center(self.boosted_image, self.angle), self.position)
        else:
            area.blit(rot_center(self.image, self.angle), self.position)

    def update(self):
        acceleration = 1 # Ускорение
        fric = acceleration / 20

        self.angle += self.angle_speed

        self.forward = angle_to_vector(math.radians(self.angle))

        if self.boost:
            self.speed[0] += self.forward[0] * acceleration
            self.speed[1] += self.forward[1] * acceleration

        self.speed[0] *= (1 - fric)
        self.speed[1] *= (1 - fric)

        # update position
        self.position[0] = (self.position[0] + self.speed[0]) % (WIDTH - self.radius)
        self.position[1] = (self.position[1] + self.speed[1]) % (HEIGHT - self.radius)

    def set_angle_vel(self, speed):
        self.angle_speed = speed


#Функция для считывания взрыва
def splice_explosion(width, height, filename):
    images = []
    seting_picture = pygame.image.load(os.path.join('img', filename)).convert_alpha()

    setting_width, master_height = seting_picture.get_size()
    for i in range(int(setting_width/width)):
    	images.append(seting_picture.subsurface((i*width,0,width,height)))
    return images
        

#Обработка анимации взрыва
explosion_images = splice_explosion(128, 128, 'explosion_blue.png')
explosion_info = PictureData([64,64], [128,128], 64, 24, True)

#Создание объектов класса
My_SpaceShip = SpaceShip([WIDTH//2, HEIGHT//2], [0,0], 0, SpaceShip_image, boosted_SpaceShip_image, SpaceShip_info)
asteroids_group = set([])
rocket_group = set([])
explosion_group = set([])

#отрисовка и обновление астероидов
def process_asteroids_group(area):
    
    for asteroid in asteroids_group:
        asteroid.draw(area)
        asteroid.update()
        
    for rocket in list(rocket_group):
        rocket.draw(area)
        if rocket.update():
            rocket_group.remove(rocket)

    for explosion in explosion_group:
        explosion.draw(area)


#Описание получения урона

def group_damage(group,other_object):
    counter = len(group)
    
    for element in list(group):
        if element.damage(other_object):
            explosion_group.add(Asteroid([element.get_position()[0] - 3*element.radius,element.get_position()[1] - 3*element.radius], [0,0], 0, 0, explosion_images, explosion_info))
            group.remove(element)
            
    return counter - len(group)

#получение урона несколькими объектами
def group_group_damage(first_group, second_group):
    counter = 0
    
    for element in list(first_group):
        if group_damage(second_group,element) > 0:
            counter += 1
            first_group.remove(element)

    return counter


#Отрисовка главной поверхности
def draw(area):
    global score,lives,running
    
    area.fill(BLACK)
    area.blit(backgr,(0,0))

    #вывести корабль
    My_SpaceShip.draw(area)

    if running:
        #выводить астероиды
        process_asteroids_group(area)

        #обновлять корабль
        My_SpaceShip.update()

        #проверка на столкновения
        if group_damage(asteroids_group,My_SpaceShip) > 0:
            if lives > 1:
                lives -= 1
            else:
                lives = 0
                running=False
        
        hits = group_group_damage(rocket_group, asteroids_group)
        if hits > 0:
            score += hits;
    else:
        area.blit(zastavka, (WIDTH//2 - 150, HEIGHT//2 - 100))

    #Отрисовка верхней панели
    f1 = pygame.font.SysFont("arial", 30)
    label1 = f1.render("Жизней осталось : "+str(lives), 1, GREEN)
    area.blit(label1, (20,20))

    f2 = pygame.font.SysFont("arial", 30)
    label2 = f2.render("Счёт : "+str(score), 1, GREEN)
    area.blit(label2, (650, 20))

def rot_center(image, angle):
    #Прокурутка прямоугольника для объекта относительно центра
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
    
#keydown handler
def keydown(event):
    ang_speed = 4.5
    
    if event.key == K_LEFT:
        My_SpaceShip.set_angle_vel(ang_speed)
    if event.key == K_RIGHT:
        My_SpaceShip.set_angle_vel(-ang_speed)
    if event.key == K_UP:
        My_SpaceShip.set_boost(True)
    if event.key == K_SPACE:
        My_SpaceShip.shoot()
            


def keyup(event):

    if event.key in (K_LEFT,K_RIGHT):
        My_SpaceShip.set_angle_vel(0)
    if event.key == K_UP:
        My_SpaceShip.set_boost(False)
    
#С какой частотой спавнить астероиды
def timer():
    global time
    
    if time <= WIDTH: 
        time += 1
        if time % 60 == 0:
            asteroid_spawn()
    else:
        time = 0


def asteroid_spawn():
    global asteroids_group,running
    
    if len(asteroids_group) < 12 and running:
        
        while True:
            random_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
    
            if dist(random_pos,My_SpaceShip.get_position()) <= asteroid_info.get_radius() + 2 * My_SpaceShip.get_radius():
                continue
            else:
                rock_pos = random_pos
                break
        
        increase = score/10 #Увеличение сложности игры в зависимости от набранного счета
        
        rock_vel = [random.random() * (3 + increase) - (1 + increase), random.random() * (3 + increase) - (1 + increase)]
        rock_avel = random.random() * 6 - 1
        asteroids_group.add(Asteroid(rock_pos, rock_vel, 0, rock_avel, asteroid_image, asteroid_info))

def click(event):
    global running, lives, score, asteroids_group, rocket_group, My_SpaceShip
    
    if event.button == 1 and event.pos[0] in range(WIDTH//2 - 200, WIDTH//2 + 200) and event.pos[1] in range(HEIGHT//2 - 150, HEIGHT//2 + 150) and not running:
        running = True
        #lives = 5
        #score = 0
        asteroids_group = set([])
        rocket_group = set([])

#бесконечный цикл игры
while True:
    draw(display)
    timer()
    for event in pygame.event.get(): #Перебор событий игры
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
    fps.tick(60) #Количество кадров в секунду (сколько отрисовок делает игра)