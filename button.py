import pygame
from pygame import font

class Button:

    def __init__(self,game, msg):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.width = 200
        self.height = 50

        self.button_color = (255,0,0)
        self.text_color = (255,255,255)
        self.font = font.SysFont(None,48)

        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    
    def _prep_msg(self,msg):
        self.msg_image = self.font.render(msg, True, self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
