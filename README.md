# Pong-troubles
import pygame
from sys import exit
from pygame.locals import*

#sprite_file = "Images/name.jpg"

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

#sprite = pygame.image.load(sprite_file)

speed_x, speed_y, x, y, y2, y3 = 133, 170, 320, 20, 20, 240
move_y = 0
move_y2 = 0
paddle = Rect(20, 20, 20, 100)
paddle2 = Rect(600, 20, 20, 100)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        print(event)
        time_passed = clock.tick()
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_s:
                move_y = +1
            elif event.key == K_w:
                move_y = -1
            elif event.key == K_UP:
                move_y2 = -1
            elif event.key == K_DOWN:
                move_y2 = +1

        elif event.type == KEYUP:
            if event.key == K_s:
                move_y = 0
            elif event.key == K_w:
                move_y = 0
            elif event.key == K_UP:
                move_y2 = 0
            elif event.key == K_DOWN:
                move_y2 = 0
    screen.fill((255, 255, 255))
    #screen.blit(sprite, (100, 100))

    y += move_y
    if y > 400:
        y = 400
        paddle = Rect(20, 390, 20, 100)
    elif 400 > y > 0:
        paddle = Rect(20, y, 20, 100)
    elif y < 0:
        y = 0
        paddle = Rect(20, y, 20, 100)

    y2 += move_y2
    if y2 > 400:
        y2 = 400
        paddle2 = Rect(600, 390, 20, 100)
    elif 400 > y2 > 0:
        paddle2 = Rect(600, y2, 20, 100)
    elif y2 < 0:
        y2 = 0
        paddle2 = Rect(600, y2, 20, 100)

    pygame.draw.rect(screen, (0, 0, 0), paddle)
    pygame.draw.rect(screen, (0, 0, 0), paddle2)
    pygame.draw.circle(screen, (0, 0, 0), (x, y3), 20)

    #time_passed = clock.tick(100)
    #time_passed_in_seconds = time_passed/1000

    x += int(clock.tick(10) * speed_x * 0.001)
    y3 += int(clock.tick() * speed_y * 0.001)



    pygame.display.update()
