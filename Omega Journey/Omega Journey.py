"""
 Omega Journey
 A Game by Gustave Rosanio
 This game consists of three rooms
 Room 1: Moving blocks that player must dodge in order to advance
 Room 2: Maze that player must navigate in order to advance
 Room 3: Enemy that mirros the players movement the player must pass to advance

 This was created for Advnaced Programming Workshop Pygame 04210
 Professor Bo Sun.
 Start date of project: 4/13/2018
 Finish date of project: 
"""
 
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PLAYER_BROWN =(157,142,135)

class Block(pygame.sprite.Sprite):
    """
    This class creates 4 blocks used in room 1,
    that when hit the player will
    be reset to the bottom.
    """
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
    def set_coords(self, x, y):
        # sets the coordiates for the sprite position
        self.rect.x = x
        self.rect.y = y
    def move_right(self):
        self.rect.x += 4
        if (self.rect.x >= 600):
            self.rect.x = 200
    def move_left(self):
        self.rect.x += -4
        if (self.rect.x <= 200):
            self.rect.x = 600
        

# create the blocks for room 1 and set thir starting coodinates
block1 = Block(BLACK, 20, 15)
block1.set_coords(201, 50)
block2 = Block(BLACK, 20, 15)
block2.set_coords(599, 100)
block3 = Block(BLACK, 20, 15)
block3.set_coords(201, 150)
block4 = Block(BLACK, 20, 15)
block4.set_coords(599, 200)
block5 = Block(BLACK, 20, 15)
block5.set_coords(201, 250)
block6 = Block(BLACK, 20, 15)
block6.set_coords(599, 300)
block7 = Block(BLACK, 20, 15)
block7.set_coords(201, 350)
block8 = Block(BLACK, 20, 15)
block8.set_coords(599, 400)

# create a list for the block sprites
block_list = pygame.sprite.Group()
# adds the blocks to the list
block_list.add(block1)
block_list.add(block2)
block_list.add(block3)
block_list.add(block4)
block_list.add(block5)
block_list.add(block6)
block_list.add(block7)
block_list.add(block8)

     
pygame.init()

# Functions
def print_instructions():
    print("Welcome to Omega Journey!")
    print("Your goal in this game is to reach the final room")
    print("But beware, puzzles and enemies are in your way")
    print("Defeat the challanges in each room, and the Golden Challice will be yours!")
    

 
# Set the width and height of the screen [width, height]
size = (800, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Omega Journey")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Load in the sound files
bump_sound = pygame.mixer.Sound("Collision(Bump).wav")
warp_sound = pygame.mixer.Sound("Collision(Warp).wav")

# Load in the player, final boss, and challice icons
player_image = pygame.image.load("Player(cropped).png").convert()
player_image.set_colorkey(PLAYER_BROWN)
enemy_image = pygame.image.load("Enemy(cropped).png").convert()
enemy_image.set_colorkey(WHITE)
challice = pygame.image.load("Golden_Chalice.png").convert()
# Load in the background graphics

# Starting position of the background
background_position = [0,0]

# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Speed in pixels per frame
# For player
y_speed = 0
x_speed = 0

# For enemy
x_echange = 0
y_echange = 0

# Current position
# For player
x_coord = 400
y_coord = 480

# For enemy
x_enemy = 350
y_enemy = 80

#---------- Begin creation of the rooms ----------#
# Use this to control what room is being loaded onto the screen
room_number = 1
# Create the first room
def room1():
    # drawing code for the boundries
    pygame.draw.rect(screen,BLUE,[0,0,200,800],0)
    pygame.draw.rect(screen,BLUE,[600,0,200,800],0)
    # draws the room number on the screen
    font = pygame.font.SysFont('Calibri',25,True,False)
    text_room = font.render("Room 1",True,WHITE)
    screen.blit(text_room, [50,450])
    block_list.draw(screen)

def room2():
    # drawing code for the boundries
    pygame.draw.rect(screen,GREEN,[0,0,200,500],0)
    pygame.draw.rect(screen,GREEN,[200,0,100,300],0)
    pygame.draw.rect(screen,GREEN,[300,200,200,100],0)
    pygame.draw.rect(screen,GREEN,[300,365,500,100],0)
    pygame.draw.rect(screen,GREEN,[550,200,250,200],0)
    pygame.draw.rect(screen,GREEN,[450,450,350,50],0)
    pygame.draw.rect(screen,GREEN,[550,0,250,300],0)
    pygame.draw.rect(screen,GREEN,[300,0,50,200],0)
    pygame.draw.rect(screen,GREEN,[370,0,50,165],0)
    pygame.draw.rect(screen,GREEN,[420,0,150,165],0)
    # draws the room number on the screen
    font = pygame.font.SysFont('Calibri',25,True,False)
    text_room = font.render("Room 2",True,WHITE)
    screen.blit(text_room, [50,450])

def room3():
    # drawing code for the boundies
    # top & bottom bumpers
    pygame.draw.rect(screen,RED,[0,0,380,50],0)
    pygame.draw.rect(screen,RED,[420,0,380,50],0)
    pygame.draw.rect(screen,RED,[0,450,380,50],0)
    pygame.draw.rect(screen,RED,[420,450,380,50],0)
    # side bumpers
    pygame.draw.rect(screen,RED,[0,0,50,500],0)
    pygame.draw.rect(screen,RED,[750,0,50,500],0)
    # draws the room number on the screen
    font = pygame.font.SysFont('Calibri',25,True,False)
    text_room = font.render("Room 3",True,WHITE)
    screen.blit(text_room, [50,450])

def victory_room():
    # drawing code for the background of the room
    pygame.draw.rect(screen,BLACK,[0,0,800,500],0)
    # draws the room number on the screen
    font = pygame.font.SysFont('Calibri',25,True,False)
    text_room = font.render("Congradulations, you have found the Golden Challice!",True,WHITE)
    screen.blit(text_room, [50,50])
    text_thanks = font.render("Thank you for playing my game!",True,WHITE)
    screen.blit(text_thanks, [50,100])
    # draw the golden challice on the screen
    screen.blit(challice,[400,200])
    

#----------End room creation----------#  

print_instructions()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            print("User decided to quit the game")
            # User pressed down on a key
 
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
                if (room_number == 3):
                    x_echange = -2
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
                if (room_number == 3):
                    x_echange = 2
            elif event.key == pygame.K_UP:
                y_speed = -3
                if (room_number == 3):
                    y_echange = 2
            elif event.key == pygame.K_DOWN:
                y_speed = 3
                if (room_number == 3):
                    y_echange = -2
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
                x_echange = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
                y_echange = 0
 
    # --- Game logic should go here


#---------- Collision logic starts here ----------#
    # collision for room one
    if room_number == 1:
        if x_coord < 200:
            x_coord = 201
            bump_sound.play()
        elif x_coord > 585:
           x_coord = 584
           bump_sound.play()
        elif y_coord > 500:
            y_coord = 470
            bump_sound.play()

        # checks to see if they player exited the room and go to the next
        if (y_coord < 0):
            room_number = room_number + 1
            x_coord = 400
            y_coord = 480

        # collision for the sprites
        if((x_coord >= block1.rect.x) and (x_coord <= block1.rect.x + 20)) and ((y_coord >= block1.rect.y) and (y_coord <= block1.rect.y + 15)):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
        elif((x_coord >= block2.rect.x) and (x_coord <= block2.rect.x + 20)) and ((y_coord >= block2.rect.y) and (y_coord <= block2.rect.y + 15)):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
        elif((x_coord >= block3.rect.x) and (x_coord <= block3.rect.x + 20)) and ((y_coord >= block3.rect.y) and (y_coord <= block3.rect.y + 15)):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
        elif((x_coord >= block4.rect.x) and (x_coord <= block4.rect.x + 20)) and ((y_coord >= block4.rect.y) and (y_coord <= block4.rect.y + 15)):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
        elif((x_coord >= block5.rect.x) and (x_coord <= block5.rect.x + 20)) and ((y_coord >= block5.rect.y) and (y_coord <= block5.rect.y + 15)):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
        elif((x_coord >= block6.rect.x) and (x_coord <= block6.rect.x + 20)) and ((y_coord >= block6.rect.y) and (y_coord <= block6.rect.y + 15)):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
        elif((x_coord >= block7.rect.x) and (x_coord <= block7.rect.x + 20)) and ((y_coord >= block7.rect.y) and (y_coord <= block7.rect.y + 15)):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
        elif((x_coord >= block8.rect.x) and (x_coord <= block8.rect.x + 20)) and ((y_coord >= block8.rect.y) and (y_coord <= block8.rect.y + 15)):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
            
    # collision for room two
    elif room_number == 2:
        if y_coord > 500:
            y_coord = 470
            bump_sound.play()
        elif (x_coord > 0  and x_coord < 200) and (y_coord > 0 and y_coord < 500):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
        elif (x_coord > 300 and x_coord < 500) and (y_coord > 200 and y_coord < 300):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
        elif (x_coord > 200 and x_coord < 300) and (y_coord > 0 and y_coord < 300):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
        elif (x_coord > 290 and x_coord < 800) and (y_coord > 360 and y_coord < 465):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
        elif (x_coord > 540 and x_coord < 800) and (y_coord > 200 and y_coord < 400):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
        elif (x_coord > 440 and x_coord < 800) and (y_coord > 450 and y_coord < 500):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
        elif (x_coord > 540 and x_coord < 800) and (y_coord > 0 and y_coord < 300):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
        elif (x_coord > 290 and x_coord < 350) and (y_coord > -5 and y_coord < 200):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
        elif (x_coord > 360 and x_coord < 420) and (y_coord > -5 and y_coord < 165):
            x_coord = 400
            y_coord = 480
            warp_sound.play()
        elif (x_coord > 410 and x_coord < 570) and (y_coord > 0 and y_coord < 165):
            x_coord = 400
            y_coord = 480
            warp_sound.play()

        # checks to see if they player exited the room and go to the next
        if (y_coord < 0):
            room_number = room_number + 1
            x_coord = 400
            y_coord = 480
            
    # collisions for room 3
    elif room_number == 3:
        if y_coord > 500:
            y_coord = 470
            bump_sound.play()
        elif (x_coord > -10 and x_coord < 380) and (y_coord > -5 and y_coord < 50):
            x_coord = 400
            y_coord = 480
            x_enemy = 350
            y_enemy = 80
            warp_sound.play()
        elif (x_coord > 410 and x_coord < 800) and (y_coord > -5 and y_coord < 50):
            x_coord = 400
            y_coord = 480
            x_enemy = 350
            y_enemy = 80
            warp_sound.play()
        elif (x_coord > -10 and x_coord < 380) and (y_coord > 435 and y_coord < 500):
            x_coord = 400
            y_coord = 480
            x_enemy = 350
            y_enemy = 80
            warp_sound.play()
        elif (x_coord > 410 and x_coord < 800) and (y_coord > 435 and y_coord < 500):
            x_coord = 400
            y_coord = 480
            x_enemy = 350
            y_enemy = 80
            warp_sound.play()
        elif (x_coord > 0 and x_coord < 50) and (y_coord > 0 and y_coord < 500):
            x_coord = 400
            y_coord = 480
            x_enemy = 350
            y_enemy = 80
            warp_sound.play()
        elif (x_coord > 740 and x_coord < 800) and (y_coord > 0 and y_coord < 500):
            x_coord = 400
            y_coord = 480
            x_enemy = 350
            y_enemy = 80
            warp_sound.play()

        # check to see if they player has hit the enemy
        # if player has hit the enemy send them back to the begining of the game
        if((x_coord >= x_enemy) and (x_coord <= x_enemy + 50)) and ((y_coord >= y_enemy) and (y_coord <= y_enemy + 100)):
            room_number = 1
            x_coord = 400
            y_coord = 480
            x_enemy = 350
            y_enemy = 80
            warp_sound.play()

        # checks to see if they player exited the room and go to the next
        if (y_coord < 0):
            room_number = room_number + 1
            x_coord = 400
            y_coord = 480
            
    # collision for victory room
    elif room_number == 4:
        if x_coord < 0:
            x_coord = 1
        elif x_coord > 790:
            x_coord = 780
        elif y_coord > 490:
            y_coord = 480
        elif y_coord < 0:
            y_coord = 1
#---------- Collision logic ends here ----------#
        

    # Code to move the player
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    # Code to move the enemy
    x_enemy = x_enemy + x_echange
    y_enemy = y_enemy + y_echange
    
    # --- Screen-clearing code goes here
    screen.fill(WHITE)
 
 
    # --- Drawing code should go here
    
    # logic to determine what room the player is in
    if room_number == 1:
        room1()
    elif room_number == 2:
        room2()
    elif room_number == 3:
        room3()
    elif room_number == 4:
        victory_room()
        
    screen.blit(player_image, [x_coord,y_coord])
    if (room_number == 3):
        screen.blit(enemy_image, [x_enemy, y_enemy])

    # if the room number = 1 then draw move the block sprites
    if (room_number == 1):
        block1.move_right()
        block2.move_left()
        block3.move_right()
        block4.move_left()
        block5.move_right()
        block6.move_left()
        block7.move_right()
        block8.move_left()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
