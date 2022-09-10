import pygame, time

display_width = 600
display_height = 600


pygame.init()
screen = pygame.display.set_mode((display_width , display_height))
pygame.display.set_caption("Tic Tac Toe")

    # put font.ttf files in a seperate folder
font = pygame.font.SysFont('Ariel', 60)
# font = pygame.font.Font('I:\PythonFiles\CREW-tictactoe-main\Montserrat-Regular.ttf', 70)

    # get the cross and circle images from the folder 
cross_image = pygame.image.load("cross.png")
circle_image = pygame.image.load("circle1.png")

    # board 2d array to hold all the x and o digitally to check for win conditions
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


    # This function return the row and col coordiantes using the coordinates from mouse click
def get_pos(x, y):
    if x < 200:
        col = 0
    elif x > 200 and x < 400:
        col = 1 
    else:
        col = 2
    
    if y < 200:
        row = 0
    elif y > 200 and y < 400:
        row = 1 
    else:
        row = 2
        
    return (row, col)

    # This function returns the box coordinates meaning
        # determines the coordinates ('boxes') of where the images will be placed
def get_box(coordinate):
    if coordinate == (0, 0):
        return (0, 0)
    elif coordinate == (0, 1):
        return (210, 0)
    elif coordinate == (0, 2):
        return (410, 0)
    
    elif coordinate == (1, 0):
        return (0, 210)
    elif coordinate == (1, 1):
        return (210, 210)
    elif coordinate == (1, 2):
        return (410, 210)
    
    elif coordinate == (2, 0):
        return (0, 410)
    elif coordinate == (2, 1):
        return (210, 410)
    else:
        return (410, 410)

    # checks board for win conditions after every mouse click
def board_check(board):
    
    ## horizontal and vertical
    
    for i in range(2):    
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return board[i][0]
        
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return board[0][i]

    ## diagnal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][2]
    

def text_objects(text, color):
    textSurface=font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_screen(msg, color):
    textSurf, textRect = text_objects(msg, color)
    textRect.center = (display_width/2), (display_height/2)
        # puts the text rectanble on top of all the layers
    screen.blit(textSurf, textRect)


def game_over(winner):
    while True:
            # colour of screen after game ends
        screen.fill((0, 0, 0))
            # colour of text after game ends
                # contrast colours (light coral (240, 128, 128), cyan tint (81,170,175), pretty orange (242,171,35))
        message_screen(winner, (81, 170, 175))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

done = False

box_status = []

current_turn = 'cross'

occupied_boxes = []

# loop to start the actual game making

while not done:
    
    # Background RGB - Red, Green, Blue
    # original colour for course (173, 216, 230)
    screen.fill((81, 170, 175))
    # colour.adobe.com and colour-hex.com
    # Make the grid lines one by one

        # Vertical left line
    pygame.draw.rect(screen, (32, 32, 32), (display_width/3, 0, 10, display_height))
        # Vertical right line
    pygame.draw.rect(screen, (32, 32, 32), ((display_width*2)/3, 0, 10, display_height))
    
        # Horizontal up line
    pygame.draw.rect(screen, (32, 32, 32), ((0, display_height/3, display_width, 10)))
        # Horizontal down line
    pygame.draw.rect(screen, (32, 32, 32), ((0, (display_height*2)/3, display_width, 10)))
    
    
        
    if pygame.mouse.get_pressed()[0] == True:
            # get the coordinates from where the mouse is clicked
        cords = pygame.mouse.get_pos()
            # print(cords)
        mouse_position = get_pos(cords[0], cords[1])
            # To determine the coordinates where the image will be placed
        box_coordinate = get_box(mouse_position)
            # print(box_coordinate)
        
            # checks the occupied array if the box clicked is occupied or not? 
        if box_coordinate not in occupied_boxes:
            if current_turn == 'cross':
                    # inserts an image of cross into the box
                box_status.append([cross_image, box_coordinate])
                current_turn = 'circle'
                    # replaces the 0 in the board array to '1' meaning there is a 'X' in this place
                board[mouse_position[0]][mouse_position[1]] = 1
            else:
                    # inserts an image of circle into the box
                box_status.append([circle_image, box_coordinate])
                current_turn = 'cross'
                    # replaces the 0 in the board array to '2' meaning there is a 'O' in this place
                board[mouse_position[0]][mouse_position[1]] = 2

            # add the box to this array to prevent double entry
        occupied_boxes.append(box_coordinate)
        
        # makes sure that the images are always on the top layer every time the game screen refreshes
    for boxes in box_status:
        screen.blit(boxes[0], boxes[1])

        # if game is quit, then end the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        # does cross meet the win condtions?
    if board_check(board) == 1:
                # if yes, output the win message on screen
        game_over('Cross Wins')
        done = True
        # does circle meet the win condtions?
    if board_check(board) == 2:
            # if yes, output the win message on screen
        game_over('Circle Wins')
        done = True
        # takes the draw exception into account
    if len(box_status) == 9:
            # if all boxes are full and no win condition is meet, then output draw message on screen
        game_over('Game DRAW')
        done = True 
        
    pygame.display.update()
    time.sleep(0.05)








    
    
