

class GameStats:

    def __init__(self,game):
        self.game = game
        self.settings = game.settings
        self.score = 0
        self.highscore = 0
        # self.first = True
        self.reset_stats()

    
    def reset_stats(self):
        # if self.first:
        self.ships_left = self.settings.ship_limit
            # self.first = False
        # else:
        #     self.ships_left = self.settings.ship_limit + 1
        self.level = 1
        self.score = 0