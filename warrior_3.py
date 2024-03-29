import pygame
from pygame.locals import *
import sys
import random
import time
from tkinter import filedialog
from tkinter import *
import numpy

pygame.init()  # Begin pygame

# Declaring variables to be used through the program
vec = pygame.math.Vector2
HEIGHT = 350
WIDTH = 700
ACC = 0.3
FRIC = -0.10
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

# Create the display
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


# light shade of the button 
color_light = (170,170,170)
color_dark = (100,100,100)
color_white = (255,255,255) 
  
# defining a font
headingfont = pygame.font.SysFont("Verdana", 40)
regularfont = pygame.font.SysFont('Corbel',25)
smallerfont = pygame.font.SysFont('Corbel',16) 
text = regularfont.render('LOAD' , True , color_light)



# Run animation for the RIGHT
run_ani_R = [pygame.image.load("Movement_Animations/Player_Sprite_R.png"), pygame.image.load("Movement_Animations/Player_Sprite2_R.png"),
             pygame.image.load("Movement_Animations/Player_Sprite3_R.png"),pygame.image.load("Movement_Animations/Player_Sprite4_R.png"),
             pygame.image.load("Movement_Animations/Player_Sprite5_R.png"),pygame.image.load("Movement_Animations/Player_Sprite6_R.png"),
             pygame.image.load("Movement_Animations/Player_Sprite_R.png")]

# Run animation for the LEFT
run_ani_L = [pygame.image.load("Movement_Animations/Player_Sprite_L.png"), pygame.image.load("Movement_Animations/Player_Sprite2_L.png"),
             pygame.image.load("Movement_Animations/Player_Sprite3_L.png"),pygame.image.load("Movement_Animations/Player_Sprite4_L.png"),
             pygame.image.load("Movement_Animations/Player_Sprite5_L.png"),pygame.image.load("Movement_Animations/Player_Sprite6_L.png"),
             pygame.image.load("Movement_Animations/Player_Sprite_L.png")]

# Attack animation for the RIGHT
attack_ani_R = [pygame.image.load("Movement_Animations/Player_Sprite_R.png"), pygame.image.load("Attack_Animations/Player_Attack_R.png"),
                pygame.image.load("Attack_Animations/Player_Attack2_R.png"),pygame.image.load("Attack_Animations/Player_Attack2_R.png"),
                pygame.image.load("Attack_Animations/Player_Attack3_R.png"),pygame.image.load("Attack_Animations/Player_Attack3_R.png"),
                pygame.image.load("Attack_Animations/Player_Attack4_R.png"),pygame.image.load("Attack_Animations/Player_Attack4_R.png"),
                pygame.image.load("Attack_Animations/Player_Attack5_R.png"),pygame.image.load("Attack_Animations/Player_Attack5_R.png"),
                pygame.image.load("Movement_Animations/Player_Sprite_R.png")]

# Attack animation for the LEFT
attack_ani_L = [pygame.image.load("Movement_Animations/Player_Sprite_L.png"), pygame.image.load("Attack_Animations/Player_Attack_L.png"),
                pygame.image.load("Attack_Animations/Player_Attack2_L.png"),pygame.image.load("Attack_Animations/Player_Attack2_L.png"),
                pygame.image.load("Attack_Animations/Player_Attack3_L.png"),pygame.image.load("Attack_Animations/Player_Attack3_L.png"),
                pygame.image.load("Attack_Animations/Player_Attack4_L.png"),pygame.image.load("Attack_Animations/Player_Attack4_L.png"),
                pygame.image.load("Attack_Animations/Player_Attack5_L.png"),pygame.image.load("Attack_Animations/Player_Attack5_L.png"),
                pygame.image.load("Movement_Animations/Player_Sprite_L.png")]

# Animations for the Health Bar
health_ani = [pygame.image.load("health/heart0.png"), pygame.image.load("health/heart.png"),
              pygame.image.load("health/heart2.png"), pygame.image.load("health/heart3.png"),
              pygame.image.load("health/heart4.png"), pygame.image.load("health/heart5.png")]

import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images_right = [pygame.image.load("enemy_right.png")]  # Load enemy image for right movement
        self.images_left = [pygame.image.load("enemy_left.png")]    # Load enemy image for left movement
        self.image = self.images_right[0]
        self.rect = self.image.get_rect()

        # Position and movement
        self.pos = vec(random.randint(600, 700), 235)  # Spawn on the right side of the screen
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.direction = random.choice(["LEFT", "RIGHT"])  # Random initial direction
        self.jump_timer = 0  # Timer for occasional jumps

        # Enemy movement AI
        self.ai_timer = random.randint(30, 120)  # Timer for random direction change
        self.moving_right = False
        self.moving_left = False

    def move(self):
        # Update AI movement
        self.ai_timer -= 1
        if self.ai_timer <= 0:
            self.ai_timer = random.randint(30, 120)  # Reset the timer
            self.moving_right = not self.moving_right  # Randomly decide to move right or left
            self.moving_left = not self.moving_left

        # Update direction and velocity based on AI movement
        if self.moving_right:
            self.direction = "RIGHT"
            self.vel.x = 2  # Adjust the value for enemy's horizontal speed
        elif self.moving_left:
            self.direction = "LEFT"
            self.vel.x = -2  # Adjust the value for enemy's horizontal speed
        else:
            self.vel.x = 0

        # Apply gravity
        self.acc = vec(0, 0.5)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Enemy jumping occasionally
        if self.jump_timer <= 0:
            if random.random() < 0.01:  # Adjust the probability of jumping (lower for less frequent jumps)
                self.jump()
                self.jump_timer = random.randint(30, 150)  # Adjust the jump timer (higher for less frequent jumps)
        else:
            self.jump_timer -= 1

        # Wrap around the screen when reaching the edges
        if self.pos.x > WIDTH:
            self.pos.x = 0
        elif self.pos.x < 0:
            self.pos.x = WIDTH

        # Update rect with new position
        self.rect.topleft = self.pos

    def jump(self):
        self.rect.x += 1
        # Check if enemy is in contact with the ground
        hits = pygame.sprite.spritecollide(self, ground_group, False)
        self.rect.x -= 1
        # Make enemy jump only if touching the ground
        if hits and not player.jumping:
            self.vel.y = -10  # Adjust the value for enemy's vertical jump speed


class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load("backgrounds/Background.png")
            self.rectBGimg = self.bgimage.get_rect()        
            self.bgY = 0
            self.bgX = 0

      def render(self):
            displaysurface.blit(self.bgimage, (self.bgX, self.bgY))      


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("backgrounds/Ground.png")
        self.rect = self.image.get_rect(center = (350, 350))
        self.bgX1 = 0
        self.bgY1 = 285

    def render(self):
        displaysurface.blit(self.image, (self.bgX1, self.bgY1)) 


class Item(pygame.sprite.Sprite):
      def __init__(self, itemtype):
            super().__init__()
            if itemtype == 1: self.image = pygame.image.load("Items/heart.png")
            elif itemtype == 2: self.image = pygame.image.load("Items/coin.png")
            self.rect = self.image.get_rect()
            self.type = itemtype
            self.posx = 0
            self.posy = 0
            
      def render(self):
            self.rect.x = self.posx
            self.rect.y = self.posy
            displaysurface.blit(self.image, self.rect)

      def update(self):
            hits = pygame.sprite.spritecollide(self, Playergroup, False)
            # Code to be activated if item comes in contact with player
            if hits:
                  if player.health < 5 and self.type == 1:
                        player.health += 1
                        health.image = health_ani[player.health]
                        self.kill()
                  if self.type == 2:
                        handler.money += 1
                        self.kill()
                        


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Movement_Animations/Player_Sprite_R.png")
        self.rect = self.image.get_rect()

        # Position and direction
        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direction = "RIGHT"

        # Movement 
        self.jumping = False
        self.running = False
        self.move_frame = 0

        #Combat
        self.attacking = False
        self.cooldown = False
        self.immune = False
        self.special = False
        self.experiance = 0
        self.attack_frame = 0
        self.health = 5
        self.mana = 0
        self.game_over=False

    def move(self):
          if cursor.wait == 1: return
          
          # Keep a constant acceleration of 0.5 in the downwards direction (gravity)
          self.acc = vec(0,0.5)

          # Will set running to False if the player has slowed down to a certain extent
          if abs(self.vel.x) > 0.3:
                self.running = True
          else:
                self.running = False

          # Returns the current key presses
          pressed_keys = pygame.key.get_pressed()

          # Accelerates the player in the direction of the key press
          if pressed_keys[K_LEFT]:
                self.acc.x = -ACC
          if pressed_keys[K_RIGHT]:
                self.acc.x = ACC 

          # Formulas to calculate velocity while accounting for friction
          self.acc.x += self.vel.x * FRIC
          self.vel += self.acc
          self.pos += self.vel + 0.5 * self.acc  # Updates Position with new values

          # This causes character warping from one point of the screen to the other
          if self.pos.x > WIDTH:
                self.pos.x = 0
                background.bgX -= 5  # Scroll background to the left
          if self.pos.x < 0:
                self.pos.x = WIDTH
                background.bgX += 5  # Scroll background to the right
        
          self.rect.midbottom = self.pos  # Update rect with new pos            

    def gravity_check(self):
          hits = pygame.sprite.spritecollide(player ,ground_group, False)
          if self.vel.y > 0:
              if hits:
                  lowest = hits[0]
                  if self.pos.y < lowest.rect.bottom:
                      self.pos.y = lowest.rect.top + 1
                      self.vel.y = 0
                      self.jumping = False


    def update(self):
          if cursor.wait == 1: return
          
          # Return to base frame if at end of movement sequence 
          if self.move_frame > 6:
                self.move_frame = 0
                return

          # Move the character to the next frame if conditions are met 
          if self.jumping == False and self.running == True:  
                if self.vel.x > 0:
                      self.image = run_ani_R[self.move_frame]
                      self.direction = "RIGHT"
                else:
                      self.image = run_ani_L[self.move_frame]
                      self.direction = "LEFT"
                self.move_frame += 1

          # Returns to base frame if standing still and incorrect frame is showing
          if abs(self.vel.x) < 0.2 and self.move_frame != 0:
                self.move_frame = 0
                if self.direction == "RIGHT":
                      self.image = run_ani_R[self.move_frame]
                elif self.direction == "LEFT":
                      self.image = run_ani_L[self.move_frame]

    def attack(self):        
          # If attack frame has reached end of sequence, return to base frame      
          if self.attack_frame > 10:
                self.attack_frame = 0
                self.attacking = False

          # Check direction for correct animation to display  
          if self.direction == "RIGHT":
                 self.image = attack_ani_R[self.attack_frame]
          elif self.direction == "LEFT":
                 self.correction()
                 self.image = attack_ani_L[self.attack_frame] 

          # Update the current attack frame  
          self.attack_frame += 1
          

    def jump(self):
        self.rect.x += 1

        # Check to see if payer is in contact with the ground
        hits = pygame.sprite.spritecollide(self, ground_group, False)
        
        self.rect.x -= 1

        # If touching the ground, and not currently jumping, cause the player to jump.
        if hits and not self.jumping:
           self.jumping = True 
           self.vel.y = -12

    def correction(self):
          # Function is used to correct an error
          # with character position on left attack frames
          if self.attack_frame == 1:
                self.pos.x -= 20
          if self.attack_frame == 10:
                self.pos.x += 20
                
    def player_hit(self):
        if self.cooldown == False:      
            self.cooldown = True # Enable the cooldown
            pygame.time.set_timer(hit_cooldown, 1000) # Resets cooldown in 1 second

            self.health = self.health - 1
            health.image = health_ani[self.health]
            
            if self.health <= 0:
                self.kill()
                self.game_over=True
                pygame.display.update()

      
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()     
        self.pos = vec(0,0)
        self.vel = vec(0,0)

        self.direction = random.randint(0,1) # 0 for Right, 1 for Left
        self.vel.x = random.randint(2,6) / 2  # Randomised velocity of the generated enemy
        self.mana = random.randint(1, 3)  # Randomised mana amount obtained upon    

        # Sets the intial position of the enemy
        if self.direction == 0:
            self.pos.x = 0
            self.pos.y = 235
        if self.direction == 1:
            self.pos.x = 700
            self.pos.y = 235


      def move(self):
        if cursor.wait == 1: return
        
        # Causes the enemy to change directions upon reaching the end of screen    
        if self.pos.x >= (WIDTH-20):
              self.direction = 1
        elif self.pos.x <= 0:
              self.direction = 0

        # Updates positon with new values     
        if self.direction == 0:
            self.pos.x += self.vel.x
        if self.direction == 1:
            self.pos.x -= self.vel.x
            
        self.rect.topleft = self.pos # Updates rect
               
      def update(self):
            # Checks for collision with the Player
            hits = pygame.sprite.spritecollide(self, Playergroup, False)

            # Activates upon either of the two expressions being true
            if hits and player.attacking == True:
                  self.kill()
                  handler.dead_enemy_count += 1
                  
                  if player.mana < 100: player.mana += self.mana # Release mana
                  player.experiance += 1   # Release expeiriance
                  
                  rand_num = numpy.random.uniform(0, 100)
                  item_no = 0
                  if rand_num >= 0 and rand_num <= 5:  # 1 / 20 chance for an item (health) drop
                        item_no = 1
                  elif rand_num > 5 and rand_num <= 15:
                        item_no = 2

                  if item_no != 0:
                        # Add Item to Items group
                        item = Item(item_no)
                        Items.add(item)
                        # Sets the item location to the location of the killed enemy
                        item.posx = self.pos.x
                        item.posy = self.pos.y
                 

            # If collision has occured and player not attacking, call the "hit" func.            
            elif hits and player.attacking == False:
                  player.player_hit()
                  
      def render(self):
            # Displayed the enemy on screen
            displaysurface.blit(self.image, self.rect)


class Castle(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.hide = False
            self.image = pygame.image.load("castle.png")

      def update(self):
            if self.hide == False:
                  displaysurface.blit(self.image, (400, 80))


class EventHandler():
      def __init__(self):
            self.enemy_count = 0
            self.dead_enemy_count = 0
            self.battle = False
            self.enemy_generation = pygame.USEREVENT + 2
            self.stage = 1
            self.money = 0
            self.paused=False
            self.stage_enemies=[5,10,15]

            self.stage_enemies = []
            for x in range(1, 21):
                  self.stage_enemies.append(int((x ** 2 / 2) + 1))
            
      def stage_handler(self):
            # Code for the Tkinter stage selection window
            self.root = Tk()
            self.root.geometry('200x170')
            
            button1 = Button(self.root, text = "Twilight Dungeon", width = 18, height = 2,
                            command = self.world1)
            button2 = Button(self.root, text = "Skyward Dungeon", width = 18, height = 2,
                            command = self.world2)
            button3 = Button(self.root, text = "Hell Dungeon", width = 18, height = 2,
                            command = self.world3)
             
            button1.place(x = 40, y = 15)
            button2.place(x = 40, y = 65)
            button3.place(x = 40, y = 115)
            
            self.root.mainloop()
      
      def world1(self):
            self.root.destroy()
            pygame.time.set_timer(self.enemy_generation, 2000)
            button.imgdisp = 1
            castle.hide = True
            self.battle = True

      def world2(self):
            self.battle = True
            button.imgdisp = 1
            

      def world3(self):
            self.battle = True
            button.imgdisp = 1
 
      def next_stage(self):  # Code for when the next stage is clicked
            button.imgdisp = 1
            self.stage += 1
            print("Stage: "  + str(self.stage))
            self.enemy_count = 0
            self.dead_enemy_count = 0

            if handler.stage <= len(handler.stage_enemies):
                  pygame.time.set_timer(self.enemy_generation, 1500 - (50 * self.stage))      
            else:
                  print("Congratulations! You've completed all stages!")

      def update(self):
            if self.dead_enemy_count == self.stage_enemies[self.stage - 1]:
                  self.dead_enemy_count = 0
                  stage_display.clear = True
                  stage_display.stage_clear()

      def home(self):
            # Reset Battle code
            pygame.time.set_timer(self.enemy_generation, 0)
            self.battle = False
            self.enemy_count = 0
            self.dead_enemy_count = 0
            self.stage = 1

            # Destroy any enemies or items lying around
            for group in Enemies, Items:
                  for entity in group:
                        entity.kill()
            
            # Bring back normal backgrounds
            castle.hide = False
            background.bgimage = pygame.image.load("backgrounds/Background.png")
            ground.image = pygame.image.load("backgrounds/Ground.png")



class HealthBar(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("health/heart5.png")

      def render(self):
            displaysurface.blit(self.image, (10,10))


class StageDisplay(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.text = headingfont.render("STAGE: " + str(handler.stage), True, color_dark)
            self.rect = self.text.get_rect()
            self.posx = -100
            self.posy = 100
            self.display = False
            self.clear = False

      def move_display(self):
            # Create the text to be displayed
            self.text = headingfont.render("STAGE: " + str(handler.stage), True, color_dark)
            if self.posx < 720:
                  self.posx += 6
                  displaysurface.blit(self.text, (self.posx, self.posy))
            else:
                  self.display = False
                  self.posx = -100
                  self.posy = 100


      def stage_clear(self):
            self.text = headingfont.render("STAGE CLEAR!", True , color_dark)
            button.imgdisp = 0
            
            if self.posx < 720:
                  self.posx += 10
                  displaysurface.blit(self.text, (self.posx, self.posy))
            else:
                  self.clear = False
                  self.posx = -100
                  self.posy = 100
                  
     

class StatusBar(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((90, 66))
            self.rect = self.surf.get_rect(center = (500, 10))
            self.exp = player.experiance
            
      def update_draw(self):
            # Create the text to be displayed
            text1 = smallerfont.render("STAGE: " + str(handler.stage) , True , color_white)
            text2 = smallerfont.render("EXP: " + str(player.experiance) , True , color_white)
            text3 = smallerfont.render("MANA: " + str(player.mana) , True , color_white)
            text4 = smallerfont.render("FPS: " + str(int(FPS_CLOCK.get_fps())) , True , color_white)
            self.exp = player.experiance

            # Draw the text to the status bar
            displaysurface.blit(text1, (585, 7))
            displaysurface.blit(text2, (585, 22))
            displaysurface.blit(text3, (585, 37))
            displaysurface.blit(text4, (585, 52))


class Cursor(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.image = pygame.image.load("cursor.png")
            self.rect = self.image.get_rect()
            self.wait = 0

      def pause(self):
            if self.wait == 1:
                  self.wait = 0
            else:
                  self.wait = 1

      def hover(self):
          if 620 <= mouse[0] <= 660 and 300 <= mouse[1] <= 345:
                pygame.mouse.set_visible(False)
                cursor.rect.center = pygame.mouse.get_pos()  # update position 
                displaysurface.blit(cursor.image, cursor.rect)
          else:
                pygame.mouse.set_visible(True)
                

class PButton(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.vec = vec(620, 300)
            self.imgdisp = 0

      def render(self, num):
            if (num == 0):
                  self.image = pygame.image.load("Buttons/home_small.png")
            elif (num == 1):
                  if cursor.wait == 0:
                        self.image = pygame.image.load("Buttons/pause_small.png")
                  else:
                        self.image = pygame.image.load("Buttons/play_small.png")
                                    
            displaysurface.blit(self.image, self.vec)

            if 620 <= mouse[0] <= 660 and 300 <= mouse[1] <= 350:
                  pygame.mouse.set_visible(False)
                  cursor.rect.center = pygame.mouse.get_pos()  # update position 
                  displaysurface.blit(cursor.image, cursor.rect)
                  
                  if pygame.mouse.get_pressed()[0]:
                        if num == 0:
                              handler.home()
                        elif num == 1:
                              if cursor.wait == 0:
                                    if not handler.paused:
                                          cursor.pause()
                                          handler.paused = True
                                    else:
                                          cursor.pause()
                                          handler.paused = False
                  else:
                        pygame.mouse.set_visible(True)     
            


Enemies = pygame.sprite.Group()
enemy=Enemy()
Enemies.add(enemy)
player = Player()
Playergroup = pygame.sprite.Group()
Playergroup.add(player)

background = Background()
button = PButton()
ground = Ground()
cursor = Cursor()

ground_group = pygame.sprite.Group()
ground_group.add(ground)

castle = Castle()
handler = EventHandler()
health = HealthBar()
stage_display = StageDisplay()
status_bar = StatusBar()
Fireballs = pygame.sprite.Group()
Items = pygame.sprite.Group()

hit_cooldown = pygame.USEREVENT + 1

          
            
            

while True:
    player.gravity_check()
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == hit_cooldown:
            player.cooldown = False
        # Will run when the close window button is clicked    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == handler.enemy_generation and cursor.wait == 0:
            if handler.enemy_count < handler.stage_enemies[handler.stage - 1]:
                  enemy = Enemy()
                  Enemies.add(enemy)
                  handler.enemy_count += 1
        
        # For events that occur upon clicking the mouse (left click) 
        if event.type == pygame.MOUSEBUTTONDOWN:
              if 620 <= mouse[0] <= 660 and 300 <= mouse[1] <= 350:
                    print("PAUSE")
                    if button.imgdisp == 1:
                        cursor.pause()
                    elif button.imgdisp == 0:
                          handler.home()


        # Event handling for a range of different key presses    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if not handler.paused:
                    cursor.pause()
                    handler.paused = True
            elif event.key == pygame.K_c:
                if handler.paused:
                    cursor.pause()
                    handler.paused = False
                    print("UNPAUSE")
            if event.key == pygame.K_n:
                  if handler.battle == True and len(Enemies) == 0:
                        handler.next_stage()
                        stage_display = StageDisplay()
                        stage_display.display = True
            if event.key == pygame.K_q and 450 < player.rect.x < 550:
                handler.stage_handler()
            if event.key == pygame.K_SPACE:
                player.jump()
            if event.key == pygame.K_RETURN:
                if player.attacking == False:
                    player.attack()
                    player.attacking = True      

    # Player and game logic update only when not paused
    if not handler.paused and not player.game_over:
        player.gravity_check()
        player.update()
        player.move()
        # Other game logic...
    # Render game over screen if player is dead
    if player.game_over:
        print("GAME OVER!")
        # Render a semi-transparent overlay
        pygame.draw.rect(displaysurface, (0, 0, 0, 128), displaysurface.get_rect())
        # Render game over text
        game_over_text = headingfont.render("GAME OVER", True, color_white)
        displaysurface.blit(game_over_text, ((WIDTH - game_over_text.get_width()) // 2, (HEIGHT - game_over_text.get_height()) // 2))

    # Rendering code for background, sprites, status bars, etc.
    # Display and Background related functions         
    background.render()
    ground.render()
    button.render(button.imgdisp)
    cursor.hover()

    if handler.dead_enemy_count == handler.stage_enemies[handler.stage - 1]:
            handler.dead_enemy_count = 0
            handler.next_stage()
    # If game is paused, render pause menu
    if handler.paused:
        # Render a semi-transparent overlay
        pygame.draw.rect(displaysurface, (10, 10, 20, 128), displaysurface.get_rect())
        # Render pause text
        pause_text = regularfont.render("PAUSED", True, color_dark)
        displaysurface.blit(pause_text, ((WIDTH - pause_text.get_width()) // 2, (HEIGHT - pause_text.get_height()) // 2))

    # Player related functions
    player.update()
    if player.attacking == True:
          player.attack() 
    player.move()                


    # Render stage display
    if stage_display.display == True:
          stage_display.move_display()
    if stage_display.clear == True:
          stage_display.stage_clear()

    # Rendering Sprites
    castle.update()
    if player.health > 0:
        displaysurface.blit(player.image, player.rect)
    health.render()

    # Status bar update and render
    displaysurface.blit(status_bar.surf, (580, 5))
    status_bar.update_draw()
    handler.update()

    
    for i in Items:
          i.render()
          i.update() 
   
    for entity in Enemies:
          entity.update()
          entity.move()
          entity.render()
      

    pygame.display.update()      
    FPS_CLOCK.tick(FPS)
