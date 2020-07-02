import pygame
from sys import exit
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

ball_speed_x, ball_speed_y, ball_x, y, y2, ball_y = 1, 1, 320, 20, 20, 240
ball_angle_in_radians = 60
frame_no = 0

move_y = 0
move_y2 = 0
paddle = Rect(20, 20, 20, 100)
paddle2 = Rect(600, 20, 20, 100)

ball = pygame.Rect(ball_x, ball_y, 20, 20)

while True:
    for event in pygame.event.get():
        #print(event)
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
    # screen.blit(sprite, (100, 100))

    y += move_y
    if y > 400:
        y = 390
        paddle = Rect(20, y, 20, 100)
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
    print(y)

    pygame.draw.rect(screen, (0, 0, 0), paddle)
    pygame.draw.rect(screen, (0, 0, 0), paddle2)
    pygame.draw.ellipse(screen, (0, 0, 0), ball)

    if ball_x > 620 or ball_x < 20:
        ball_speed_x *= -1

    if ball_y > 460 or ball_y < 20:
        ball_speed_y *= -1

    if ball.colliderect(paddle2) or ball.colliderect(paddle):
        ball_speed_x *= -1

    ball_x += ball_speed_x
    ball_y += ball_speed_y
    ball = pygame.Rect(ball_x, ball_y, 20, 20)

    pygame.display.update()
