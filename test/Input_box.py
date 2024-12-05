import pygame
from setting import *
from pygame_textinput.textinput import TextInput

class InputBox:
    def __init__(self, center_x, center_y, width, height, font_path, font_size=32, text=''):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (center_x, center_y)
        self.color_inactive = pygame.Color(GREEN)
        self.color_active = pygame.Color(BLACK)
        self.color = self.color_inactive
        self.font = pygame.font.Font(font_path, font_size)
        self.text_input = TextInput(self.font, self.color_active)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        
        if self.active:
            self.text_input.update([event])

        if event.type == pygame.USEREVENT and hasattr(event, 'Text'):
            return event.Text
        return None

    def update(self, events):
        if self.active:
            self.text_input.update(events)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.text_input.get_surface(), (self.rect.x + 5, self.rect.y + 5))

    def get_text(self):
        return self.text_input.value




