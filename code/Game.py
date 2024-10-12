#!/usr/bin/python
#*** coding: utf-8 ***
import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))  # Game screen scaling

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # # check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:  # Variável QUIT = 256
            #         print('Quitting...')
            #         pygame.quit()  # Close Window
            #         quit()  # End pygame