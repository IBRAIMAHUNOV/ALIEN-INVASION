import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, представлящий одного прищельца."""

    def __init__(self, ai_settings, screen):
        """Ининциализирует прищельца и задает начальную позицию."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения прищельца и назначение атрибута rect.
        self.image = pygame.image.load('C:/Users/Arstan Ernisbekov/Downloads/alienship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый прищелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной позиции прищельца.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Возвращает True, если прищелец находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Перемещает прищельцев в право или влево."""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Выводит прищельца в текущем положении."""
        self.screen.blit(self.image, self.rect)
