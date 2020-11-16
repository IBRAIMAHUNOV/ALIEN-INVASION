class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_settings):
        """Инициализирует статистику игры."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Игра Alien Invasion запускается в не активном состоянии.
        self.game_active = True  # False

        # рекорд не должен сбрасываться.
        self.high_score = 0

    def reset_stats(self):
        """Инициализирует статистику изменяющийся в ходе игры."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1