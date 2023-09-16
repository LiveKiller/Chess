import pygame

pygame.init()
back = (192,192,192)
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Master')
gameDisplay.fill(back)

running = True
while running:
    gameDisplay.fill(back)
    if pygame.mouse.get_pressed()[0] == True:gameDisplay.blit(pygame.image.load("b.png"),(pygame.mouse.get_pos()[0]-45,17))
    gameDisplay.fill((255, 204, 153), pygame.Rect(100, 100, 300, 50))
    pygame.draw.circle(gameDisplay, (255, 204, 153), (400, 125), 25)
    if pygame.mouse.get_pressed()[0] == True:gameDisplay.blit(pygame.image.load("c.png"),(pygame.mouse.get_pos()[0]-12,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:running = False
    pygame.display.update()
pygame.quit()
quit()
