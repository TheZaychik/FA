import pygame
from PreSet import *
from helper_functions import *
from load_img import *

def rot_center(image, angle):
    #Прокурутка прямоугольника для объекта относительно центра
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

class Asteroid:
    def __init__(self, position, speed, ang, ang_speed, image, info):
        self.speed = [speed[0], speed[1]]
        self.angle = ang
        self.angle_speed = ang_speed
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.time_to_die = info.get_lifespan()
        self.animated = info.get_animated()
        self.chet = 0
        self.position = [position[0] + self.radius, position[1] + self.radius]

    def damage(self, other_object):
        if dist(self.position, other_object.get_position()) <= self.radius + other_object.get_radius():
            return True
        else:
            return False

    def get_position(self):
        return [int(self.position[0]), int(self.position[1])]

    def get_radius(self):
        return self.radius

    def draw(self, area):
        if self.animated:
            self.chet += 1
            if self.chet < self.time_to_die:
                area.blit(self.image[self.chet], self.position)
        else:
            area.blit(rot_center(self.image, self.angle),
                      (int(self.position[0] - self.radius), int(self.position[1] - self.radius)))

    def update(self):
        # обновление угла
        self.angle += self.angle_speed

        # обновление позиции
        self.position[0] = (self.position[0] + self.speed[0]) % WIDTH
        self.position[1] = (self.position[1] + self.speed[1]) % HEIGHT

        self.chet += 1

        if self.chet < self.time_to_die:
            return False
        else:
            return True
