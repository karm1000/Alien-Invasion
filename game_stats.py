

class GameStats:

    def __init__(self,game):
        self.game = game
        self.settings = game.settings
        self.score = 0

        self.reset_stats()

    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.level = 1