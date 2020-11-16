
class Settings():
    """Класс для хранения всех настроек игры Alien invasion"""

    def __init__(self):
        """Инициализирует настройки игры."""

        # параметры экрана
        self.screen_width = 1300
        self.screen_height = 680
        self.bg_color = (29, 21, 55)
        self.ship_speed_factor = 2.0
        self.ship_limit = 3

        # параметры пули
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 8
        self.bullet_color = 2, 22, 222
        self.bullets_allowed = 3

        # параметры прищельцев.
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 3
        # fleet_direction 1 обозначает движение в право, а -1 в лево
        self.fleet_direction = 1

        # Темп ускорения игры.
        self.speedup_scale = 1.1

        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction = 1 обозначает движение в право; a -1 - влево
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости, стоимость пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

