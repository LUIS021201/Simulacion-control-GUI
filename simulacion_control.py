import pygame

pygame.init()

clk = pygame.time.Clock()

size = width, heigth = 860, 479
screen = pygame.display.set_mode(size)
background_image = pygame.image.load('img/control.png').convert()
frameRect = pygame.Rect((0,0),(width,heigth))

while True:

    pygame.event.pump()
    screen.blit(background_image, (0,0))

    Keys = pygame.key.get_pressed()

    if Keys[pygame.K_a]: screen.blit(crosshair, (165,270))
    if Keys[pygame.K_s]: screen.blit(crosshair, (195,310))
    if Keys[pygame.K_d]: screen.blit(crosshair, (240,270))
    if Keys[pygame.K_w]: screen.blit(crosshair, (195,230))

    if Keys[pygame.K_j]: screen.blit(crosshair, (575,270))
    if Keys[pygame.K_k]: screen.blit(crosshair, (655,330))
    if Keys[pygame.K_l]: screen.blit(crosshair, (740,270))
    if Keys[pygame.K_i]: screen.blit(crosshair, (655,210))

    if Keys[pygame.K_e]: screen.blit(crosshair, (360,290))
    if Keys[pygame.K_r]: screen.blit(crosshair, (440,290))


    x = -1 if Keys[pygame.K_a] else 1 if Keys[pygame.K_d] else 0
    y = -1 if Keys[pygame.K_w] else 1 if Keys[pygame.K_s] else 0

    crosshair = pygame.surface.Surface((15,15))
    pygame.draw.circle(crosshair, pygame.Color("black"),(5,5),5,0)
    crosshairb = pygame.surface.Surface((15,15))
    pygame.draw.circle(crosshairb, pygame.Color("red"),(5,5),5,0)



    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(crosshairb,((x*40)+195,(y*40)+270))

    pygame.display.flip()
    clk.tick(40)

