#!/usr/bin/python
#*** coding: utf-8 ***
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, MENU_OPTION, C_YELLOW, C_WHITE, C_ORANGE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)  # Create a rectangle on the home screen to place the image.

    def run(self):
        menu_option = 0
        pygame.mixer.music.load('./assets/menu.mp3')  # only load
        pygame.mixer.music.play(-1)  # -1 = Infinite Loop

        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # Place the image in the rectangle.
            self.menu_text(70, "Mountain", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(70, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 170 + 25 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 170 + 25 * i))

            pygame.display.flip()  # Update the images on the entire screen.

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Variável QUIT = 256
                    pygame.quit()  # Close Window
                    quit()  # End pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
