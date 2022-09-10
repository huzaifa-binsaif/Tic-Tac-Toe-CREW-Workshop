import pygame

pygame.init()

pygame.display.init
pygame.display.set_mode
# Open a window on the screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
Color = (255, 255, 255)

#draw a line on the screen

Start_pos = (0, 0)
End_pos = (250, 250)
width = 600

running = True

while running:

    screen.fill(Color)

    pygame.draw.line(screen, (0,0,0), (0,250) ,(600,250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
