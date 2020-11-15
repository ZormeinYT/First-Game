import pygame, sys

def refreshScreen():
    screen.fill((0, 255, 0))

    # Barrels
    pygame.draw.rect(screen, (150, 75, 0), barrel)
    pygame.draw.rect(screen, (150, 75, 0), barrel2)


    # Bush
    pygame.draw.rect(screen, (0, 255, 0), bush_hitbox)
    pygame.draw.circle(screen, (0, 0, 0), (400, 50), 27)
    pygame.draw.circle(screen, (0, 200, 0), (400, 50), 25)

    pygame.draw.rect(screen, (0, 255, 0), bush2_hitbox)
    pygame.draw.circle(screen, (0, 0, 0), (50, 400), 27)
    pygame.draw.circle(screen, (0, 200, 0), (50, 400), 25)


    # Player
    pygame.draw.rect(screen, (255, 0, 0), player)

    pygame.display.update()

# Map objects

# Barrels
barrel = pygame.Rect(50, 50, 25, 25)
barrel2 = pygame.Rect(300, 300, 25, 25)

# Bush
bush_hitbox = pygame.Rect(373, 23, 54, 54)
bush2_hitbox = pygame.Rect(25, 373, 54, 54)

pygame.init()
WIDTH,HEIGHT = 500, 500
pygame.display.set_caption('First project')
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

# Player
player = pygame.Rect(250 - 25, 250 - 25, 50, 50)
player_vel_x = 5
player_vel_y = 5

# Music
music = True
pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and player.x + player.width < WIDTH:
        player.x += player_vel_x
        if player.colliderect(barrel2) or player.colliderect(barrel):
            player.x -= player_vel_x
        if player.colliderect(bush_hitbox) or player.colliderect(bush2_hitbox):
            player.x -= player_vel_x
    if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= player_vel_x
            if player.colliderect(barrel2) or player.colliderect(barrel):
                player.x += player_vel_x
            if player.colliderect(bush_hitbox) or player.colliderect(bush2_hitbox):
                player.x += player_vel_x
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= player_vel_y
        if player.colliderect(barrel2) or player.colliderect(barrel):
            player.y += player_vel_y
        if player.colliderect(bush_hitbox) or player.colliderect(bush2_hitbox):
            player.y += player_vel_y
    if keys[pygame.K_DOWN] and player.y + player.width < WIDTH:
        player.y += player_vel_y
        if player.colliderect(barrel2) or player.colliderect(barrel):
            player.y -= player_vel_y
        if player.colliderect(bush_hitbox) or player.colliderect(bush2_hitbox):
            player.y -= player_vel_y
    if keys[pygame.K_m]:
        if music:
            music = False
            pygame.mixer.music.pause()
        else:
            music = True
            pygame.mixer.music.play(-1)

    #for solid in solidobj:
        #if player.colliderect(solid):

    refreshScreen()
