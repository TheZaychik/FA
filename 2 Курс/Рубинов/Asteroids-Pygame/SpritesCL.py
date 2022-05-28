import math, pygame

class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound=None):
        if sound:
            sound.play()
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        self.pos = [pos[0] + self.radius, pos[1] + self.radius]

    def collide(self, other_object):
        if dist(self.pos, other_object.get_position()) <= self.radius + other_object.get_radius():
            return True
        else:
            return False

    def get_position(self):
        return [int(self.pos[0]), int(self.pos[1])]

    def get_radius(self):
        return self.radius

    def draw(self, canvas):
        if self.animated:
            self.age += 1
            if self.age < self.lifespan:
                canvas.blit(self.image[self.age], self.pos)
        else:
            canvas.blit(rot_center(self.image, self.angle),
                        (int(self.pos[0] - self.radius), int(self.pos[1] - self.radius)))

    def update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % w
        self.pos[1] = (self.pos[1] + self.vel[1]) % h
        self.age += 1
        if self.age < self.lifespan:
            return False
        else:
            return True


w = 800
h = 600

def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)

def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image