import pygame,os
from II import PictureData # Настройки изображений
#задний фон
backgr = pygame.image.load(os.path.join('img','space.svg'))

#Изображение корабля
SpaceShip_image = pygame.image.load(os.path.join('img', 'fighterspr1.png'))
SpaceShip_info = PictureData([45,45], [90,90], 45)

#Изображение корабля при ускорении
boosted_SpaceShip_image = pygame.image.load(os.path.join('img', 'fighterspr1normal.png'))
boosted_SpaceShip_info = PictureData([45,45], [90,90], 45)

#Изображение астероидов
asteroid_image = pygame.image.load(os.path.join('img', 'a10002.png'))
asteroid_info = PictureData([45,45], [90,90],45)

#Изображение ракеты
rocket_image = pygame.image.load(os.path.join('img', 'torpedo.png'))
rocket_info = PictureData([5,5], [20,20], 5, 50)

#Экран заставки
zastavka = pygame.image.load(os.path.join('img', 'zastavka.png'))
