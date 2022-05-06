import sys, pygame

pygame.init()


size = width, height = 800, 600

speed = [1, 1]

fuchsia = 255, 0, 255

pygame.display.set_caption("latający baniak")

screen = pygame.display.set_mode(size)


baniak = pygame.image.load("baniak.png")

baniakrect = baniak.get_rect()


while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()


    baniakrect = baniakrect.move(speed)

    if baniakrect.left < 0 or baniakrect.right > width:

        speed[0] = -speed[1]

    if baniakrect.top < 0 or baniakrect.bottom > height:

        speed[1] = -speed[1]


    screen.fill(fuchsia)

    screen.blit(baniak, baniakrect)

    pygame.display.flip()
