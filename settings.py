
class Settings:
    def __init__(self,speed=1.5):
        
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = speed

        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (220, 223, 0)
        self.bullets_allowed = 5

        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.alien_points = 50
        self.initialize_speeds()

    def initialize_speeds(self):
        
        self.bullet_speed = 2.0
        self.alien_speed = 1.5
        self.fleet_drop_speed = 7
        # 1 is right and -1 is left
        self.fleet_direction = 1

    def increase_speed(self):
        
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale  