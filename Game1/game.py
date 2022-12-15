import pygame


pygame.init()
window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Game 1")


class Character():
    health = 100
    armor = 100
    player = pygame.image.load('textures/images.jpg')
    playerX = 100
    playerY = 100 



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    
    pygame.display.update()
