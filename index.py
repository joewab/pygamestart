import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Traveler')
clock = pygame.time.Clock()
pixel_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

score_surf = pixel_font.render('Welcome Traveler', False, (64,64,64)).convert()
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600, 300))

snail_x_pos = 600

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    if player_rect.bottom >= 300:
                        player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom >= 300:
                        player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800

    if game_active:
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,300))

        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10, 10)
        screen.blit(score_surf, score_rect)

        #snail
        screen.blit(snail_surf, snail_rect)
        if snail_rect.left < -10 : snail_rect.left = 800
        snail_rect.left -= 4
        
        #player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Yellow')

    pygame.display.update()
    clock.tick(60)