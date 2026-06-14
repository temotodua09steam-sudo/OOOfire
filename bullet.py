"""Класс пули"""

import pygame
from config import *


class Bullet(pygame.sprite.Sprite):
    """Класс пули игрока"""

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -BULLET_SPEED

    def update(self):
        """Обновление позиции пули"""
        self.rect.y += self.speed_y

        # Удаление пули, если она вышла за границы экрана
        if self.rect.bottom < 0:
            self.kill()


class EnemyBullet(pygame.sprite.Sprite):
    """Класс пули врага"""

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speed_y = 3

    def update(self):
        """Обновление позиции пули врага"""
        self.rect.y += self.speed_y

        # Удаление пули, если она вышла за границы экрана
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
