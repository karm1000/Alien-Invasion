import pygame

class Scoreboard:
    
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.game_stats = game.game_stats
        self.text_color = (30,30,30)
        self.font = pygame.font.Font(None,48)
        self.prep_score()
        self.prep_level()

    def prep_score(self):
        score_str = str(self.game_stats.score)
        self.score_image = self.font.render(score_str, True,
        self.text_color, self.settings.bg_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_level(self):
        level_str = str(f"Level {self.game_stats.level}")
        self.level_image = self.font.render(level_str, True,
        self.text_color, self.settings.bg_color)
        
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.level_image,self.level_rect)

