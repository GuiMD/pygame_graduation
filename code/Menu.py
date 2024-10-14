#!/usr/bin/python
#*** coding: utf-8 ***
import pygame.image

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)  # Create a rectangle on the home screen to place the image.

    def run(self, ):
        self.window.blit(source=self.surf, dest=self.rect)  # Place the image in the rectangle.
        pygame.display.flip()  # Update the images on the entire screen.
        pass
