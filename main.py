import numpy as np
import sys
import pygame
import time
# "{0:.0%}".format(data["lost"]/data["total"])

bg = (200, 200, 200)
total = 0
elapsed = 0
clock = pygame.time.Clock()

pygame.init()
pygame.font.init()

font = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((600, 600))
screen.fill(bg)

values = {
    "cat": 0,
    "dog": 0,
    "human": 0,
}

objects = {
    "cat": 1,
    "dog": 1,
    "human": 1,
}
def text_draw():
    # clearing so numbers show correctly
    screen.fill(bg)
    totals = font.render("Total {} {}".format(total, elapsed), False, (0, 0, 0))
    dog = font.render("dog {} {}".format(values["dog"], "{0:.0%}".format(values["dog"]/total)), False, (0, 0, 0))
    cat = font.render("cat {} {}".format(values["cat"], "{0:.0%}".format(values["cat"]/total)), False, (0, 0, 0))
    human = font.render("human {} {}".format(values["human"], "{0:.0%}".format(values["human"]/total)), False, (0, 0, 0))
    screen.blit(totals, (78, 50))
    screen.blit(dog, (100, 100))
    screen.blit(cat, (105, 150))
    screen.blit(human, (60, 200))


while 1:
    start = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    total += 1
    x = np.random.choice(list(objects))
    values[x] += objects[x]

    # updating visuals
    text_draw()
    pygame.display.update()

    times = (time.time() - start)
    print(times)
    if times > 0.0:
        elapsed = 1.0 / times
