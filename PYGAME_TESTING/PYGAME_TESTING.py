import pygame
import sys

pygame.init()
size = 840, 640
speed = [0, 1]
screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")

ballrect = ball.get_rect()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > size[0]:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > size[1]:
#         speed[1] = -speed[1]

#     screen.blit(ball, ballrect)
while True:
    screen.fill((255, 255, 255))
    pygame.draw.circle(ball,color=(0,0,0),center=(2,2),radius=20)
    pygame.display.flip()
