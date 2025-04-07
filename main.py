import pygame as pg
import math
import random

# Constants

WIN_WIDTH = 1920
WIN_HEIGHT = 1080
G = 6.67 / (10**11)
simulation = True
window = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
FPS = 60
clock = pg.time.Clock()

# Vector class

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Summaring vectors

def sum_vecs(v1, v2):
    v = Vector(v1.x + v2.x, v1.y + v2.y)
    return v

class Object:
    def __init__(self, x, y, vx, vy, ax, ay, color, mass, volume):
        # Initializing :P

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.color = color
        self.mass = mass
        self.volume = volume
        self.radius = math.cbrt(3 * self.volume / (4 * math.pi))

    def update(self):
        F = Vector(0, 0)
        for obj in objects:
            if obj != self:
                d = math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)

                if d < self.radius + obj.radius:
                    # Calculating collision

                    self.vx = -self.vx
                    self.vy = -self.vy

                else:
                    # Calculating force vector

                    Ft = G * self.mass * obj.mass / (d ** 2)
                    FtV = Vector((obj.x - self.x) * (Ft / d), (obj.y - self.y) * (Ft / d))
                    F = sum_vecs(F, FtV)

        # Updating all variables

        self.ax = F.x / self.mass
        self.ay = F.y / self.mass

        self.vx += self.ax
        self.vy += self.ay

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x > WIN_WIDTH:
            self.x = 0

        if self.x < 0:
            self.x = 1920

        if self.y > WIN_HEIGHT:
            self.y = 0

        if self.y < 0:
            self.y = 1080

    def draw(self, window):
        # Drawing

        pg.draw.circle(window, self.color, (self.x, self.y), self.radius)

# Initializing planets (Some random for fun)

'''
P1 = Object(random.randint(20, 1900), random.randint(20, 1060),
            0, 0, 0, 0,
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            5 * 10**13, 10000)

P2 = Object(random.randint(20, 1900), random.randint(20, 1060),
            0, 0, 0, 0,
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            5 * 10**13, 10000)

P3 = Object(random.randint(20, 1900), random.randint(20, 1060),
            0, 0, 0, 0,
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            5 * 10**13, 10000)

P4 = Object(random.randint(20, 1900), random.randint(20, 1060),
            0, 0, 0, 0,
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            5 * 10**13, 10000)

P5 = Object(random.randint(20, 1900), random.randint(20, 1060),
            0, 0, 0, 0,
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            5 * 10**13, 10000)

'''

# Initializing objects list

objects = [Object(random.randint(20, 1900), random.randint(20, 1060),
            0, 0, 0, 0,
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            5 * 10**13, 10000) for i in range(3)]

while (simulation):
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            simulation = False

    window.fill((0, 0, 0))

    keys = pg.key.get_pressed()
    if keys[pg.K_q] or keys[pg.K_ESCAPE]:
        simulation = False

    for obj in objects:
        obj.update()

    for obj in objects:
        obj.move()
        obj.draw(window)

    pg.display.update()
