import pygame 
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from time import sleep
# make stars


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.game_active = False
        self.bg_color = (0, 140, 255)
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.game_stats = GameStats(self)
        self.play_button = Button(self,"Play")
        self.sb =  Scoreboard(self)
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        self._check_aliens_bottom()
    
    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if(alien.rect.bottom>self.settings.screen_height):
                self._ship_hit()
                break

    def _create_stars(self):
        pass
    
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
        
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        
        self.settings.fleet_direction *= -1 


    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        current_x, current_y = alien_width, alien_height
        while current_y< (self.settings.screen_height - 2.0*alien_height):
            while current_x < self.settings.screen_width:
                self._create_alien(current_x,current_y)
                current_x += 2 * alien_width
            
            current_x = alien_width
            current_y += 1*alien_height

    def _create_alien(self,x_position,y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.y = y_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)



    def _check_events(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
               
    
    def _check_keydown_events(self,event):
        
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True 
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True 
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True 
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False 
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False 

    def _check_play_button(self,mouse_pos):
        if self.game_active==False and self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True
            self.game_stats.reset_stats()
            self.sb.prep_level()
            self.sb.prep_ships()


    def _fire_bullet(self):
        if(len(self.bullets)<self.settings.bullets_allowed):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        self._check_bullet_alien_collision()
        

    def _check_bullet_alien_collision(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        collisions = pygame.sprite.groupcollide(self.aliens,self.bullets,True,True)

        if(collisions):
            for aliens in collisions.values(): 
                self.game_stats.score += self.settings.alien_points * len(aliens)
            # self.game_stats.score += self.settings.alien_points
            
            self.sb.prep_score()
            self.sb.check_highscore()


        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.game_stats.level += 1
            self.sb.prep_level()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()  
        self.aliens.draw(self.screen) 
        self.sb.show_score()
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _ship_hit(self):
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self.sb.prep_ships()
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            sleep(1)
        else:
            self.game_active = False


if __name__ == "__main__":
    game = AlienInvasion()

    game.run_game()
