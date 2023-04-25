import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self,screen,gun):

        """создаю пулю в позиции пушки"""

        super(Bullet,self).__init__()

        self.screen=screen
        self.rect=pygame.Rect(0,0,2,12)
        self.color=113,200,52
        self.speed=5.9
        self.rect.centerx=gun.rect.centerx
        self.rect.top=gun.rect.top
        self.y=float(self.rect.y)

    def update(self):

        """перемещение пули вверх"""

        self.y-=self.speed
        self.rect.y=self.y

    def draw_bullet(self):

        """рисую пулю на экране"""

        pygame.draw.rect(self.screen,self.color,self.rect)


























































































































