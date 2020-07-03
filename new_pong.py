import pygame
import time
import random
from sys import exit
from pygame.locals import *
import os

background_file_image = "../Images/background_pong.png"
global background, color1, color2, select_opponent
background = pygame.image.load(background_file_image)

pygame.init()
display_width = 640
display_height = 640

select_opponent = ""
color1 = (0, 0, 0)
color2 = (0, 0, 0)
white = (255, 255, 255)

red = (150, 0, 0)
green = (0, 150, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Pong Master")
clock = pygame.time.Clock()


# ===========Highlight the Versus Text====================
def highlight_text():
    global color1, color2, select_opponent
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # ============Highlight or click CPU text=============
    if 492 > mouse[0] > 390 and 360 > mouse[1] > 325:
        smallText = pygame.font.Font('freesansbold.ttf', 50)
        text = "CPU"
        display_text(smallText, 390, (display_height / 2), text, (0, 255, 0))
        if click[0] == 1:
            color2 = (0, 0, 0)
            color1 = (0, 255, 0)
            select_opponent = "CPU"

    # ===========Highlight or click Human Text================
    elif 560 > mouse[0] > 390 and 410 > mouse[1] > 375:
        smallText = pygame.font.Font('freesansbold.ttf', 50)
        text = "Human"
        display_text(smallText, 390, ((display_height + 100) / 2), text, (0, 255, 0))
        if click[0] == 1:
            color1 = (0, 0, 0)
            color2 = (0, 255, 0)
            select_opponent = "Human"

# =============Highlight or click button===============
def highlight_button():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # ============Highlight or click Go! button================
    if 200 > mouse[0] > 100 and 500 > mouse[1] > 450:
        pygame.draw.rect(gameDisplay, bright_green, (100, 450, 100, 50))

        # =============Click on the Go! button====================
        if click[0] == 1 and (color2 == (0, 255, 0) or color1 == (0, 255, 0)):
            pygame.quit()
            run_game()
    else:
        pygame.draw.rect(gameDisplay, green, (100, 450, 100, 50))

    # ================Highlight or click Quit button===============
    if 550 > mouse[0] > 450 and 500 > mouse[1] > 450:
        pygame.draw.rect(gameDisplay, bright_red, (450, 450, 100, 50))

        # =============Click on the Quit button==============
        if click[0] == 1:
            pygame.quit()
    else:
        pygame.draw.rect(gameDisplay, red, (450, 450, 100, 50))

# =============Text to screen function=================
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

# =============Text display function===============
def display_text(font, pos_x, pos_y, text, color):
    TextSurf, TextRect = text_objects(text, font, color)
    TextRect = (pos_x, pos_y)
    gameDisplay.blit(TextSurf, TextRect)
    return TextSurf, TextRect


def game_intro():
    global clock, gameDisplay, display_width, black, display_height, red, green
    global intro
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # ==============Versus Options===================
        gameDisplay.blit(background, (0, 0))
        smallText = pygame.font.Font('freesansbold.ttf', 50)
        text = "Human"
        display_text(smallText, 70, (display_height / 2), text, (0, 255, 0))
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        text = "VS"
        display_text(largeText, 250, (display_height / 2), text, (0, 0, 0))
        smallText = pygame.font.Font('freesansbold.ttf', 50)
        text = "CPU"
        display_text(smallText, 390, (display_height / 2), text, color1)
        smallText = pygame.font.Font('freesansbold.ttf', 50)
        text = "Human"
        display_text(smallText, 390, ((display_height + 100) / 2), text, color2)

        # ================Text on Button==================
        smallText = pygame.font.Font('freesansbold.ttf', 30)
        text = "GO!"
        quitText = pygame.font.Font('freesansbold.ttf', 30)
        quit_text = "QUIT"
        highlight_button()
        highlight_text()
        display_text(smallText, 123, 464, text, (0, 0, 0))
        display_text(quitText, 463, 462, quit_text, (0, 0, 0))

        pygame.display.update()


# ==============Collision of ball on edges=============
def collision():
    global ball, ball_speed_y, ball_speed_x, ball_x, ball_y
    if ball.top >= 460 or ball.bottom <= 20:
        ball_speed_y *= -1

    if ball.left >= 620 or ball.right <= 20:
        ball_speed_x *= -1

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    ball = pygame.Rect(ball_x, ball_y, 20, 20)


# ============CPU movement function=============
def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.bottom >= 480:
        opponent.bottom = 480

# ============Main Game function==============
def run_game():
    screen = pygame.display.set_mode((640, 480), 0, 32)

    # =================Global Variables to be used====================
    global ball, paddle, opponent, ball_speed_x, ball_speed_y, ball_x, ball_y, opponent_speed
    ball_speed_x, ball_speed_y, ball_x, ball_y, opponent_speed = 0.2, 0.2, 200, 240, 12

    paddle_y = 20
    opponent_y = 20

    paddle_move_y = 1
    opponent_move_y = 1

    paddle = Rect(600, paddle_y, 20, 100)
    opponent = Rect(20, opponent_y, 20, 100)
    ball = pygame.Rect(ball_x, ball_y, 20, 20)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()

        # ========Key movement for human paddle=========
        if keys[K_UP] and paddle_y > 0:
            paddle_y -= paddle_move_y
        elif keys[K_DOWN] and paddle_y < 380:
            paddle_y += paddle_move_y

        if select_opponent == "CPU":
            opponent_ai()

        # ============Key movement for human opponent==========
        else:
            if keys[K_w] and opponent_y > 0:
                opponent_y -= opponent_move_y
            elif keys[K_s] and opponent_y < 380:
                opponent_y += opponent_move_y
            opponent = Rect(20, opponent_y, 20, 100)

        paddle = Rect(600, paddle_y, 20, 100)

        screen.fill((0, 255, 50))

        if ball.colliderect(opponent) or ball.colliderect(paddle):
            ball_speed_x *= -1

        collision()

        # ============Display of objects on screen===============
        pygame.draw.rect(screen, (0, 0, 0), paddle)
        pygame.draw.rect(screen, (0, 0, 0), opponent)
        pygame.draw.ellipse(screen, (0, 0, 0), ball)
        pygame.draw.aaline(screen, (0, 0, 0), (320, 0), (320, 480))

        pygame.display.update()


game_intro()
