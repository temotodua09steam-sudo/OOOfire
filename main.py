"""Главный файл игры OOOfire - Space Shooter"""

import pygame
import random
import sys
from config import *
from player import Player
from enemy import Enemy
from bullet import Bullet, EnemyBullet


class Game:
    """Основной класс игры"""

    def __init__(self):
        """Инициализация игры"""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

        # Sprite группы
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()

        # Создание игрока
        self.player = Player(PLAYER_START_X, PLAYER_START_Y)
        self.all_sprites.add(self.player)

        # Игровые переменные
        self.score = 0
        self.wave = 1
        self.enemy_spawn_counter = 0
        self.running = True
        self.game_over = False
        self.enemy_count = 3 + (self.wave * 2)  # Враги зависят от волны
        self.enemies_killed = 0

    def spawn_enemy(self):
        """Спавн врага"""
        if len(self.enemies) < self.enemy_count and self.enemy_spawn_counter >= ENEMY_SPAWN_RATE:
            x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
            y = random.randint(-50, -10)
            enemy = Enemy(x, y)
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)
            self.enemy_spawn_counter = 0
        else:
            self.enemy_spawn_counter += 1

    def handle_input(self):
        """Обработка входа"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_SPACE and not self.game_over:
                    if self.player.shoot():
                        bullet_x, bullet_y = self.player.get_bullet_position()
                        bullet = Bullet(bullet_x, bullet_y)
                        self.all_sprites.add(bullet)
                        self.bullets.add(bullet)
                if event.key == pygame.K_r and self.game_over:
                    self.reset_game()

        keys = pygame.key.get_pressed()
        if not self.game_over:
            self.player.handle_input(keys)

    def update(self):
        """Обновление игры"""
        if not self.game_over:
            self.all_sprites.update()
            self.spawn_enemy()

            # Враги стреляют
            for enemy in self.enemies:
                if enemy.should_shoot():
                    bullet_x, bullet_y = enemy.get_bullet_position()
                    enemy_bullet = EnemyBullet(bullet_x, bullet_y)
                    self.all_sprites.add(enemy_bullet)
                    self.enemy_bullets.add(enemy_bullet)
                    enemy.reset_shoot_cooldown()

            # Проверка столкновений: пули игрока с врагами
            collisions = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)
            for collision in collisions:
                self.score += ENEMY_KILL_POINTS
                self.enemies_killed += 1

            # Проверка столкновений: враги с игроком
            enemy_hits = pygame.sprite.spritecollide(self.player, self.enemies, True)
            if enemy_hits:
                self.game_over = True

            # Проверка столкновений: пули врагов с игроком
            player_hits = pygame.sprite.spritecollide(self.player, self.enemy_bullets, True)
            if player_hits:
                self.game_over = True

            # Проверка завершения волны
            if len(self.enemies) == 0 and self.enemies_killed >= self.enemy_count:
                self.next_wave()

    def next_wave(self):
        """Переход на следующую волну"""
        self.wave += 1
        self.enemy_count = 3 + (self.wave * 2)
        self.enemies_killed = 0
        self.score += WAVE_BONUS

    def reset_game(self):
        """Перезагрузка игры"""
        self.__init__()

    def draw(self):
        """Отрисовка игры"""
        self.screen.fill(BLACK)

        # Отрисовка спритов
        self.all_sprites.draw(self.screen)

        # Отрисовка интерфейса
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        wave_text = self.small_font.render(f"Wave: {self.wave}", True, CYAN)
        enemies_text = self.small_font.render(f"Enemies: {len(self.enemies)}", True, GREEN)

        self.screen.blit(score_text, (10, 10))
        self.screen.blit(wave_text, (SCREEN_WIDTH - 150, 10))
        self.screen.blit(enemies_text, (SCREEN_WIDTH - 150, 40))

        # Экран Game Over
        if self.game_over:
            game_over_text = self.font.render("GAME OVER", True, RED)
            final_score = self.font.render(f"Final Score: {self.score}", True, WHITE)
            final_wave = self.font.render(f"Wave: {self.wave}", True, YELLOW)
            restart_text = self.small_font.render("Press R to Restart or ESC to Exit", True, CYAN)

            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
            score_rect = final_score.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            wave_rect = final_wave.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))

            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(final_score, score_rect)
            self.screen.blit(final_wave, wave_rect)
            self.screen.blit(restart_text, restart_rect)

        pygame.display.flip()

    def run(self):
        """Основной игровой цикл"""
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
