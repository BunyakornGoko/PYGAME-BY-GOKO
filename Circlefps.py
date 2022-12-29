
import pygame
import numpy as np

pygame.init()

display = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
fps = 240
y = 360
x = 600
while True : 
    # check exit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # check user input
    if pygame.key.get_pressed()[pygame.K_w]:
        y -= 5
    if pygame.key.get_pressed()[pygame.K_s]:
        y += 5
    if pygame.key.get_pressed()[pygame.K_a]:
        x -= 5
    if pygame.key.get_pressed()[pygame.K_d]:
        x += 5

    # compute
    
    display.fill('blue')
    pygame.draw.circle(display, 'yellow', (x, y), 50)


    # wait 
    clock.tick(fps)

    # display to player
    pygame.display.update()
    x += 0
   