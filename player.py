"""Класс игрока - космический корабль"""

import pygame
from config import *


class Player(pygame.sprite.Sprite):
    """Класс игрока (космический корабль)"""

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.shoot_cooldown = 0

    def update(self):
        """Обновление позиции игрока"""
        # Движение
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Границы экрана
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        # Уменьшение cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def handle_input(self, keys):
        """Обработка ввода клавиш"""
        self.speed_x = 0
        self.speed_y = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.speed_x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.speed_x = PLAYER_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.speed_y = -PLAYER_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.speed_y = PLAYER_SPEED

    def shoot(self):
        """Возвращает True если можно выстрелить"""
        if self.shoot_cooldown <= 0:
            self.shoot_cooldown = BULLET_COOLDOWN
            return True
        return False

    def get_bullet_position(self):
        """Возвращает позицию, откуда выстреливать пулю"""
        return self.rect.centerx, self.rect.top
