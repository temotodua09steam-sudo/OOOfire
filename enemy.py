"""Класс врага"""

import pygame
import random
from config import *


class Enemy(pygame.sprite.Sprite):
    """Класс врага"""

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = random.choice([-2, -1, 1, 2])
        self.speed_y = random.randint(1, 3)
        self.shoot_cooldown = random.randint(30, 100)
        self.health = 1

    def update(self):
        """Обновление позиции врага"""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Отскок от границ
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed_x *= -1

        # Удаление врага, если он вышел за нижнюю границу
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

        # Уменьшение cooldown выстрела
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def should_shoot(self):
        """Проверка, должен ли враг выстрелить"""
        return self.shoot_cooldown <= 0

    def reset_shoot_cooldown(self):
        """Сброс cooldown выстрела"""
        self.shoot_cooldown = random.randint(30, 100)

    def get_bullet_position(self):
        """Возвращает позицию, откуда выстреливать пулю врага"""
        return self.rect.centerx, self.rect.bottom
