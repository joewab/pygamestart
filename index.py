import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Traveler')
clock = pygame.time.Clock()
pixel_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()
text_surf = pixel_font.render('Welcome Traveler', False, 'Black').convert()

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

    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf,(0,300))
    screen.blit(text_surf, (250, 50))

   
    screen.blit(snail_surf, snail_rect)
    if snail_rect.left < -10 : snail_rect.left = 800
    snail_rect.left -= 4
    
    screen.blit(player_surf, player_rect)
    if player_rect.left > 810 : player_rect.left = 0
    player_rect.left += 1

    pygame.display.update()
    clock.tick(60)