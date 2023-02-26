import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Traveler')
clock = pygame.time.Clock()
pixel_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

score_surf = pixel_font.render('Welcome Traveler', False, (64,64,64)).convert()
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600, 300))

snail_x_pos = 600

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        #if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print('collision')

    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf,(0,300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10, 10)
    screen.blit(score_surf, score_rect)

   
    screen.blit(snail_surf, snail_rect)
    if snail_rect.left < -10 : snail_rect.left = 800
    snail_rect.left -= 4
    
    screen.blit(player_surf, player_rect)
    if player_rect.left > 810 : player_rect.left = 0
    player_rect.left += 1

    #if player_rect.colliderect(snail_rect):
    #    print('collision')

    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint((mouse_pos)):
    #    print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)