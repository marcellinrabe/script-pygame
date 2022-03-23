import pygame
import Player
pygame.init()

surface = pygame.display.set_mode((0, 0))
pygame.display.set_caption("commando")


run = True

player = Player.Player(surface)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rotation(0, -30)
                
            if event.key == pygame.K_RIGHT:
                player.rotation(0, 30)
    pygame.display.flip()
pygame.quit()

pygame.mainloop()
