import pygame

print('Setup Start')  # Comment that only appears in the terminal to visualize events
pygame.init()
window = pygame.display.set_mode(size=(600, 480))  # Game screen scaling
print('Setup End')

print('Loop Start')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Variável QUIT = 256
            pygame.quit()  # Close Window
            quit()  # End pygame


