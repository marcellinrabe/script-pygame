import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, surface: pygame.Surface, color, pos:tuple, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
        self.surface = surface
        self.x, self.y = pos
        self.rect = pygame.draw.rect(surface, color, (self.x, self.y, 50, 50))

    
    def enCollision(self, object: pygame.sprite.Sprite) -> bool:
        if self.rect.x < object.rect.x + object.rect.w \
            and self.rect.x + self.rect.w > object.rect.x \
            and self.rect.y < object.rect.y + object.rect.h \
            and self.rect.h + self.rect.y > object.rect.y:

            return True
        else:
            return False

        
