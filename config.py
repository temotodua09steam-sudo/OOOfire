"""Конфигурация игры OOOfire"""

# Размеры окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

# Параметры игрока
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 40
PLAYER_SPEED = 5
PLAYER_START_X = SCREEN_WIDTH // 2
PLAYER_START_Y = SCREEN_HEIGHT - 80

# Параметры врага
ENEMY_WIDTH = 40
ENEMY_HEIGHT = 40
ENEMY_SPEED = 2
ENEMY_SPAWN_RATE = 30  # фреймов между спавнами

# Параметры пули
BULLET_WIDTH = 5
BULLET_HEIGHT = 15
BULLET_SPEED = 7
BULLET_COOLDOWN = 10  # фреймов между выстрелами

# Параметры игры
FPS = 60
GAME_TITLE = "OOOfire - Space Shooter"

# Очки
ENEMY_KILL_POINTS = 10
WAVE_BONUS = 50
