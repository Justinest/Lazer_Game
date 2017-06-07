import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1080
 
pygame.init()



        
class Block1(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self, filename):
     
        # Call the parent class (Sprite) constructor
        super().__init__()
     
        # Load the image
        self.image = pygame.image.load("Hydra.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(-100, -20)
        self.rect.x = random.randrange(0, screen_width)
 
    def update(self):
        """ Called each frame. """
 
        # Move block down one pixel
        self.rect.y += 5 
 
        # If block is too far down, reset to top of screen.
        if self.rect.y > 950:
            self.reset_pos()
            
        
 
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
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

 
        
class Ship(pygame.sprite.Sprite):
    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]    
    def __init__(self, filename):
     
        # Call the parent class (Sprite) constructor
        super().__init__()
     
        # Load the image
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(BLACK)
        
        
     
        # Set our transparent color
        self.image.set_colorkey(BLACK)    
        self.rect = self.image.get_rect()
 
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([2, 50])
        self.image.fill(WHITE)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 50

class Bullet1(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([2, 50])
        self.image.fill(WHITE)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 50
        
        
        

# Set the height and width of the screen
screen_width = 1920   
screen_height = 1080
screen = pygame.display.set_mode([screen_width,screen_height])
 

# This is a list of 'sprites.' Each block in the program is          
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
block_list1 = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()


 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

pygame.display.set_caption("Justin's Game")

for i in range(400):
    # This represents a block
    block = Block1("Hydra.png")
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    block_list.add(block)
    block_list1.add(block)
    all_sprites_list.add(block)
    
# Create a Ship
player = Ship("player.png")



all_sprites_list.add(player)


#SOUND
click_sound = pygame.mixer.Sound("Pew.ogg")
click_sound1 = pygame.mixer.Sound("Star.ogg")
click_sound2 = pygame.mixer.Sound("Ending.ogg")
click_sound3 = pygame.mixer.Sound("Cringe.ogg")
click_sound4 = pygame.mixer.Sound("Metal.ogg")
 
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Hides Le Mouse 
pygame.mouse.set_visible(0)

 
# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)
 
display_instructions = True
instruction_page = 1
name = ""
 

# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                name += event.unicode
            elif event.key == pygame.K_BACKSPACE: 
                name = name[:-1]
            elif event.key == pygame.K_RETURN:
                instruction_page += 1  
                if instruction_page == 4:
                    display_instructions = False                
 
    # Set the screen background
    background_position1 = [0, 0]
    background_image1 = pygame.image.load("TheOne.jpg").convert()
    screen.blit(background_image1, background_position1)
    
    if instruction_page == 1:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.
        text = font.render("Welcome To My Game", True, WHITE)
        screen.blit(text, [850, 450])    
        click_sound1.play()  
        
       
        
         
       
    
       
       

    if instruction_page == 2:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.
        
      
 
        text = font.render("Instructions", True, WHITE)
        screen.blit(text, [10, 10])
       
        text = font.render("Enter your name: ", True, WHITE)
        screen.blit(text, [10, 40])    
       
        text = font.render(name, True, WHITE)
        screen.blit(text, [220, 40])        
 
        text = font.render("Shoot Down the enemies without losing your 10 lives", True, WHITE)
        screen.blit(text, [10, 80])
       
        text = font.render("Hit enter to continue", True, WHITE)
        screen.blit(text, [10, 120])
 
    if instruction_page == 3:
        # Draw instructions, page 2
        text = font.render("Justin's Final assignment game", True, WHITE)
        screen.blit(text, [10, 10])    
 
        text = font.render("Hit enter to continue", True, WHITE)
        screen.blit(text, [10, 40])
 
        text = font.render("Level 1", True, WHITE)
        screen.blit(text, [10, 80])
        click_sound1.stop()  
    
    

    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
   
   
    # Set positions of graphics
    background_position = [0, 0]
     
     
    # Load and set up graphics.
    background_image = pygame.image.load("SPACERINO.jpg").convert() 
    
    #Ammo
    ammo = 120
    
    #score
    score = 0
    
    #Life
    life = 10
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True    
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet1()
            click_sound.play()
            bullet1 = Bullet()
            click_sound.play()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x + 0
            bullet.rect.y = player.rect.y + 50
            bullet1.rect.x = player.rect.x + 100
            bullet1.rect.y = player.rect.y + 50           
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet) 
            all_sprites_list.add(bullet1)
            bullet_list.add(bullet1)
            ammo -=1
            print ( ammo )
            #if ammo == 0:
                #done = True
                
            
            
    # --- Game logic
    screen.blit(background_image, background_position)

    # Call the update() method on all the sprites
    all_sprites_list.update()
 

    
    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
     
 
        # For each block hit, remove the bullet and add to the score
        #Score for shooting
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1 
            click_sound3.play()
            print(score)
            #Add Ammo for level two
            #Victory Conditions
            if score == 50:
                ammo +=50
            #if score == 100:
                #done = True
        
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -2:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            

# Clear the screen
    #Scoreboard
    scoretext = "Score: " + str(score)
    text = font.render(scoretext, True, WHITE)
    screen.blit(text, [10, 10])    

    #Life
    lifetext = "Life: " + str(life)
    text = font.render(lifetext, True, WHITE)
    screen.blit(text, [10, 50])      
    
    #ammo
    ammotext = "Ammo:" +str(ammo)
    text = font.render(ammotext, True, WHITE)
    screen.blit(text, [10, 90])     
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
     
    # Fetch the x and y out of the list, 
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]
     
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True) 
 
    # Check the list of collisions.
    # Score 
    for block in blocks_hit_list:
        life -=1
        click_sound4.play()
        print( life )
        #if life == 0:
            #done = True
            
         
    # Draw all the spites
    all_sprites_list.draw(screen)
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit() 
    # Set the screen background
screen.fill(WHITE)
    
    