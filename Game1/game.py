import pygame


pygame.init()
window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Game 1")


playerIMG = pygame.image.load('textures/player.jpg')
playerX = 100
playerY = 100




def playerSpawn(x,y):
    window.blit(playerIMG, (x, y))   



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pressed = pygame.key.get_pressed()
    if pressed [pygame.K_LEFT]:
        playerX -= .1

    if pressed [pygame.K_RIGHT]:
        playerX += .1

    if pressed [pygame.K_UP]:
        playerY -= .1

    if pressed [pygame.K_DOWN]:
        playerY += .1

    playerSpawn(playerX, playerY)
    pygame.display.update()

