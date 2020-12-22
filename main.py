import pygame
import sys
from PIL import Image
# image = Image.open("Webp.net-resizeimage (15).png")
# mode = image.mode
# size = image.size
# data = image.tobytes()
#
# py_image = pygame.image.fromstring(data, size, mode)
image = pygame.image.load("Webp.net-resizeimage (15).png")
w, h = image.get_size()
image2 = pygame.image.load("Untitled.png")
sc = pygame.display.set_mode((w, h))
mouse = pygame.mouse.get_pos()
i = 0
image3 = pygame.transform.rotate(image2, i)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # image = image.rotate(10)
            i += 1
            image3 = pygame.transform.rotate(image, i)
            print(mouse)
    mouse = pygame.mouse.get_pos()
    # py_image = pygame.image.fromstring(data, size, mode)
    rect = image3.get_rect()
    rect.center = w/2, h/2
    sc.fill((245, 245, 245))
    # sc.blit(image,(0,0))
    sc.blit(image3,rect)
    pygame.display.flip()
