# Imports
import pygame
import random
import time
import math

# Initialize game engine
pygame.init()

# Window
VERSION = ("1.1.0")
WIDTH = 1920
HEIGHT = 1080
TITLE = "Atrophy"
screen = pygame.display.set_mode((WIDTH,HEIGHT),0,0)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKRED = (30,0,0)
RED = (50, 0, 0)
GREEN = (0, 50, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
GREY = (30,30,30)
LIGHTGREY = (35,35,35)
DARKGREY = (15,15,15)

# Fonts
FONT_XL = pygame.font.Font("font/dogica.ttf", 7500)
FONT_MD = pygame.font.Font("font/dogica.ttf", 25)
FONT_SM = pygame.font.Font("font/dogica.ttf", 20)

# Images
start_screen = pygame.image.load("images/Start.png").convert_alpha()
start_effect = pygame.image.load("images/Start(1).png").convert_alpha()
start_effect2x = pygame.transform.scale2x(start_effect)
start_text1 = pygame.image.load("images/Start(4).png").convert_alpha()
start_text = pygame.image.load("images/Start(2).png").convert_alpha()
start_vignette =  pygame.image.load("images/start_vignette.png").convert_alpha()

blackscreen = pygame.image.load("images/blackscreen.png").convert_alpha()
fade = pygame.image.load("images/fade.png").convert_alpha()

face1 = pygame.image.load("images/Face1.png").convert_alpha()
face2 = pygame.image.load("images/Face2.png").convert_alpha()
faceJ = pygame.image.load("images/FaceJ.png").convert_alpha()

face_list = [face1,face2,blackscreen]

horror1 = pygame.image.load("images/horror1.png").convert_alpha()
horror12x = pygame.transform.scale2x(horror1)
horror14x = pygame.transform.scale2x(horror12x)
horror18x = pygame.transform.scale2x(horror14x)
horror116x = pygame.transform.scale2x(horror18x)
monster1 = pygame.image.load("images/monster1.png").convert_alpha()
monster2 = pygame.image.load("images/monster2.png").convert_alpha()
monster3 = pygame.image.load("images/monster3.png").convert_alpha()
monster4 = pygame.image.load("images/monster4.png").convert_alpha()
monster5 = pygame.image.load("images/monster5.png").convert_alpha()
monster6 = pygame.image.load("images/monster6.png").convert_alpha()
monster7 = pygame.image.load("images/monster7.png").convert_alpha()

idleF = pygame.image.load("images/Dude1.png").convert_alpha()
walkF1 = pygame.image.load("images/WalkF1.png").convert_alpha()
walkF2 = pygame.image.load("images/WalkF2.png").convert_alpha()

idleR = pygame.image.load("images/IdleSide.png").convert_alpha()
walkR1 = pygame.image.load("images/Walk1.png").convert_alpha()
walkR2 = pygame.image.load("images/Walk2.png").convert_alpha()

idleL = pygame.image.load("images/IdleSide2.png").convert_alpha()
walkL1 = pygame.image.load("images/Walk12.png").convert_alpha()
walkL2 = pygame.image.load("images/Walk22.png").convert_alpha()

idleB = pygame.image.load("images/Dude2.png").convert_alpha()
walkB1 = pygame.image.load("images/WalkB1.png").convert_alpha()
walkB2 = pygame.image.load("images/WalkB2.png").convert_alpha()

vignette = pygame.image.load("images/vignette.png").convert_alpha()
vignette2x = pygame.transform.scale2x(vignette)
lowhealthvignette = pygame.image.load("images/lowhealthvignette.png").convert_alpha()
lowhealthvignette2x = pygame.transform.scale2x(lowhealthvignette)

speed = pygame.image.load("images/speed.png").convert_alpha()
sugar = pygame.image.load("images/sugar.png").convert_alpha()
needle = pygame.image.load("images/needle.png").convert_alpha()

heart = pygame.image.load("images/heart.png").convert_alpha()
brain = pygame.image.load("images/brain.png").convert_alpha()
eye = pygame.image.load("images/eye.png").convert_alpha()

ritual = pygame.image.load("images/ritual.png").convert_alpha()
ritualend = pygame.image.load("images/ritualend.png").convert_alpha()
run = pygame.image.load("images/run.png").convert_alpha()

blood = pygame.image.load("images/blood.png").convert_alpha()

credit_reply = ["How malicious are Malicious Teddy Bears?","I would like to thank my mom for this.","Got milk?","She said she was 18.","Coffee is bean soup.","Good code","Secret: I actually got scared making this game.","Thank Beckett for letting me steal his code. Like a real one, he carries.","ACTUALLY created by Mr. Cooper, the teacher.","SANTI.","Jake has a self-induced seizure fetish.","KENDAL. SHUP.","Christian only LOOKS Asian."]  


# Sounds
footsteps = pygame.mixer.Sound("music/footsteps.ogg")
monstersound = pygame.mixer.Sound("music/MonsterAmbience.ogg")
cough = pygame.mixer.Sound("music/cough.ogg")
breath = pygame.mixer.Sound("music/Breaths.ogg")
itemget = pygame.mixer.Sound("music/runbreath.ogg")
monster_scream = pygame.mixer.Sound("music/monster_scream.ogg")
found = pygame.mixer.Sound("music/found.ogg")

# Music

def play():
    # Stages
    START = 0
    PLAYING = 1
    END = 2

# Classes
    class Player:
        def __init__(self, dude_images, loc ,color):
            self.dude_F_images = [idleF,walkF1,walkF2]
            self.dude_L_images = [idleL,walkL1,walkL2]
            self.dude_R_images = [idleR,walkR1,walkR2]
            self.dude_B_images = [idleB,walkB1,walkB2]
            
            self.dude_index = 0
            self.dude = self.dude_F_images[self.dude_index]

            self.newblood = blood
            
            self.rect = idleF.get_rect()
            self.rect.topleft = loc
            self.color = color
            self.growth = 0
            self.constraint = 890
            
            self.speed_time = 0
            self.movement = 0
            self.space_timer = 0
            
            self.Stance = self.dude
            self.animation_tick = 0
            self.animation_speed = 10
            self.dude_ticks = 0

            self.vx = 0
            self.vy = 0

            self.score = 0
            self.organ_score = 0
            self.virus = 4

            self.reach_goal = False

            self.angle = 0
            self.random = 1

            self.organ_timer_reset = False

            self.footstep_ticks = 0

            self.cough_timer = 0
            self.coughing = False

        def make_random(self):
            self.random += 1


        def speed(self):
            if self.speed_time > 0:
                return 2 + self.movement
            else:
                return self.movement
            
        def draw(self):
            if self.vx < 0:
                self.dude_ticks += 1

                if self.dude_ticks % self.animation_speed == 0:
                    self.dude_index += 1

                    if self.dude_index > 2:
                        self.dude_index = 1
                
                self.dude_L_images = [idleL,walkL1,walkL2]
                self.dude = self.dude_L_images[self.dude_index]
                self.Stance = self.dude
                
            elif self.vx > 0:
                self.dude_ticks += 1

                if self.dude_ticks % self.animation_speed == 0:
                    self.dude_index += 1

                    if self.dude_index > 2:
                        self.dude_index = 1
                
                self.dude_R_images = [idleR,walkR1,walkR2]
                self.dude = self.dude_R_images[self.dude_index]
                self.Stance = self.dude
                
            elif self.vy > 0:
                self.dude_ticks += 1

                if self.dude_ticks % self.animation_speed == 0:
                    self.dude_index += 1

                    if self.dude_index > 2:
                        self.dude_index = 1
                
                self.dude_F_images = [idleF,walkF1,walkF2]
                self.dude = self.dude_F_images[self.dude_index]
                self.Stance = self.dude
                
            elif self.vy < 0:
                self.dude_ticks += 1

                if self.dude_ticks % self.animation_speed == 0:
                    self.dude_index += 1

                    if self.dude_index > 2:
                        self.dude_index = 1
                
                self.dude_B_images = [idleB,walkB1,walkB2]
                self.dude = self.dude_B_images[self.dude_index]
                self.Stance = self.dude
            else:
                if self.dude == self.dude_L_images[self.dude_index]:
                    self.dude_index = 0
                    self.dude_L_images = [idleL,walkL1,walkL2]
                    self.dude = self.dude_L_images[self.dude_index]
                    self.Stance = self.dude
                elif self.dude == self.dude_R_images[self.dude_index]:
                    self.dude_index = 0
                    self.dude_R_images = [idleR,walkR1,walkR2]
                    self.dude = self.dude_R_images[self.dude_index]
                    self.Stance = self.dude
                elif self.dude == self.dude_F_images[self.dude_index]:
                    self.dude_index = 0
                    self.dude_F_images = [idleF,walkF1,walkF2]
                    self.dude = self.dude_F_images[self.dude_index]
                    self.Stance = self.dude
                elif self.dude == self.dude_B_images[self.dude_index]:
                    self.dude_index = 0
                    self.dude_B_images = [idleB,walkB1,walkB2]
                    self.dude = self.dude_B_images[self.dude_index]
                    self.Stance = self.dude

            screen.blit(self.Stance, self.rect)

        def space(self):
            self.space_timer += 1
            if self.space_timer > 100:
                self.movement = 0
        
        def go_left(self):
            self.vx = -self.speed()
            
        def go_right(self):
            self.vx = self.speed()

        def go_up(self):
            self.vy = -self.speed()

        def go_down(self):
            self.vy = self.speed()

        def stop_x(self):
            self.vx = 0

        def stop_y(self):
            self.vy = 0

        def steps(self):
            '''if self.vx != 0 or self.vy != 0:
                self.footstep_ticks += 1
                if self.footstep_ticks % 75 == 0:
                    footsteps.play()
            else:
                footsteps.stop()'''

        def check_screen_edges(self):
            if self.rect.left < 0 + self.constraint:
                self.rect.left = 0 + self.constraint
            if self.rect.right > WIDTH - self.constraint:
                self.rect.right = WIDTH - self.constraint

            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT

            for w in walls:
                if (self.rect.right == WIDTH - self.constraint or self.rect.left == 0 + self.constraint) and (self.vx > 0 or self.vx < 0):
                    w.apply_speed(self)
                else:
                    w.maze_speed = 0

            for i in items:
                if (self.rect.right == WIDTH - self.constraint or self.rect.left == 0 + self.constraint) and (self.vx > 0 or self.vx < 0):
                    i.apply_speed(self)
                else:
                    i.maze_speed = 0
                    
            for s in structures:
                if (self.rect.right == WIDTH - self.constraint or self.rect.left == 0 + self.constraint) and (self.vx > 0 or self.vx < 0):
                    s.apply_speed(self)
                else:
                    s.maze_speed = 0

            for b in blood_list:
                if (self.rect.right == WIDTH - self.constraint or self.rect.left == 0 + self.constraint) and (self.vx > 0 or self.vx < 0):
                    b.apply_speed(self)
                else:
                    b.maze_speed = 0

            for m in monster_list:
                if (self.rect.right == WIDTH - self.constraint or self.rect.left == 0 + self.constraint) and (self.vx > 0 or self.vx < 0):
                    m.apply_speed(self)
                else:
                    m.maze_speed = 0

        def move_and_check_walls(self):
            self.rect.x += self.vx

            for w in walls:
                if self.rect.colliderect(w.rect):
                    if self.vx == 0:
                        self.rect.right = w.rect.left
                    elif self.vx > 0:
                        self.rect.right = w.rect.left
                        self.vx = 0
                    elif self.vx < 0:
                        self.rect.left = w.rect.right
                        self.vx = 0

            self.rect.y += self.vy

            for w in walls:
                if self.rect.colliderect(w.rect):
                    if self.vy == 0:
                        self.rect.top = w.rect.bottom
                    elif self.vy < 0:
                        self.rect.top = w.rect.bottom
                        self.vy = 0
                    elif self.vy > 0:
                        self.rect.bottom = w.rect.top
                        self.vy = 0

        def check_items(self):
            for i in items:
                if self.rect.colliderect(i.rect):
                    i.apply(self)

            for m in monster_list:
                if m1.rect.contains(p1.rect):
                    m.apply(self)

        def cough(self):
            itemget.stop()
            cough.stop()
            found.stop()
            cough.play()
            found.set_volume(.5)
            if self.dude_ticks % 3 == 0 and p1.organ_score > 0:
                found.play()
            self.angle += 30 
            self.newblood = pygame.transform.rotate(blood,self.angle*self.random)
            rx = random.randrange(-64,10)
            ry = random.randrange(-64,10)
            b = Blood([self.rect.x+rx,self.rect.y+ry,8*64,4*64], self.newblood)
            blood_list.append(b)

            self.coughing = True
            self.cough_timer = 1

        def alert(self):
            if self.coughing == True:
                self.cough_timer += 1
                if self.cough_timer > 250:
                    self.coughing = False
                    self.cough_timer = 0

        def check_goal(self):
            if r1.rect.contains(self.rect) and self.organ_score == 3:
                self.reach_goal = True

        def update(self):
            self.space()
            
            if 12 > self.space_timer > 0:
                if m1.player_distance < 300:
                    self.movement = m1.monster_speed
                else:
                    self.movement = 4
            else:
                self.movement = 2
     
            if self.speed_time > 0:
                self.speed_time -= 1
                
            self.move_and_check_walls()
            self.check_screen_edges()
            self.check_items()
            self.steps()
            self.make_random()
            self.alert()


    class Wall:
        def __init__(self, rect_xywh,color):
            self.rect = pygame.Rect(rect_xywh)
            self.color = color
            self.maze_speed = 0

        def apply_speed(self,player):
            self.maze_speed = player.vx

        def move(self):
            self.rect.x -= self.maze_speed

        def update(self):
            self.move()
                
             
        def draw(self):
            pygame.draw.rect(screen, self.color, self.rect)



    class Coin:

        def __init__(self, rect_xywh,image):
            self.rect = pygame.Rect(rect_xywh)
            self.image = image
            self.maze_speed = 0

        def apply(self,player):
            player.score += 1
            player.speed_time = 200
            items.remove(self)
            cough.stop()
            itemget.stop()
            itemget.set_volume(.7)
            itemget.play()
            itemget.fadeout(4000)

        def apply_speed(self,player):
            self.maze_speed = player.vx

        def move(self):
            self.rect.x -= self.maze_speed

        def draw(self):
            screen.blit(self.image, self.rect)

        def update(self):
            self.move()


    class Keys:

        def __init__(self, rect_xywh,image):
            self.rect = pygame.Rect(rect_xywh)
            self.image = image
            self.maze_speed = 0

        def apply(self,player):
            player.organ_score += 1
            player.virus -= 1
            items.remove(self)
            player.organ_timer_reset = True

        def apply_speed(self,player):
            self.maze_speed = player.vx

        def move(self):
            self.rect.x -= self.maze_speed

        def draw(self):
            screen.blit(self.image, self.rect)

        def update(self):
            self.move()


    class Ritual:

        def __init__(self, rect_xywh,image):
            self.rect = pygame.Rect(rect_xywh)
            self.image = image
            self.maze_speed = 0

        def apply_speed(self,player):
            self.maze_speed = player.vx

        def move(self):
            self.rect.x -= self.maze_speed

        def draw(self):
            screen.blit(self.image, self.rect)

        def change_image(self):
            for p in players:
                if p.organ_score == 3:
                    self.image = ritualend

        def update(self):
            self.change_image()
            self.move()


    class Blood:

        def __init__(self, rect_xywh,image):
            self.rect = pygame.Rect(rect_xywh)
            self.image = p1.newblood
            self.maze_speed = 0

        def apply_speed(self,player):
            self.maze_speed = player.vx

        def move(self):
            self.rect.x -= self.maze_speed

        def draw(self):
            screen.blit(self.image, self.rect)

        def update(self):
            self.move()


    class Monster:

        def __init__(self, rect_xywh,image):
            self.monster_anim_list = [monster1,monster2,monster3,monster4,monster5,monster6,monster7]
            self.monster_index = 0

            self.monster = self.monster_anim_list[self.monster_index]
            
            self.rect = pygame.Rect(rect_xywh)
            self.image = self.monster
            self.maze_speed = 0
            self.angle = 0

            self.x = WIDTH/2 - (256/2)
            self.y = -1000
            self.pmx = self.x
            self.pmy = self.y
            self.dx = 0
            self.dy = 0
            self.distance = 0

            self.px = random.randrange(0,WIDTH)
            self.py = random.randrange(0,HEIGHT)
            self.ticks = 0

            self.player_distance = 0

            self.monster_speed = 3

            self.jumpscare_J = False

            self.found_x = 0
            self.found_y = 0
            
        def apply_speed(self,player):
            self.maze_speed = player.vx

        def move(self):
            self.x -= self.maze_speed

        def apply(self,player):
            monster_scream.play()

        def draw(self):
            self.ticks += 1
            if self.ticks % 10 == 0:
                self.monster_index += 1
                if self.monster_index > 6:
                    self.monster_index = 0
            self.monster = self.monster_anim_list[self.monster_index]

            if p1.organ_score == 2:
                self.monster_speed = 5
            elif p1.organ_score == 3:
                self.monster_speed = 8
            
            if p1.cough_timer > 0:
                self.found_x = b.rect.x+32
                self.found_y = b.rect.y+32
                self.radians = math.atan2(self.found_y-self.pmy,self.found_x-self.pmx)
                self.angle = math.atan2(self.found_y-self.pmy,self.found_x-self.pmx)*(180/math.pi)
                self.distance = math.hypot(self.found_x-self.pmx,self.found_y-self.pmy)
                self.player_distance = math.hypot(p1.rect.x-self.pmx,p1.rect.y-self.pmy)
                self.distance = int(self.distance)

                if self.distance < 10:
                    p1.cough_timer = 300

            else:
                self.radians = math.atan2(self.py-self.pmy,self.px-self.pmx)
                self.angle = math.atan2(self.py-self.pmy,self.px-self.pmx)*(180/math.pi)
                self.distance = math.hypot(self.px-self.pmx,self.py-self.pmy)
                self.player_distance = math.hypot((p1.rect.x+32)-self.pmx,(p1.rect.y+32)-self.pmy)
                self.distance = int(self.distance)

            
            self.dx = math.cos(self.radians)*self.monster_speed
            self.dy = math.sin(self.radians)*self.monster_speed

            self.pmx = self.x
            self.pmy = self.y

            if self.distance:
                self.distance -= 1
                self.x += self.dx
                self.y += self.dy

            if self.distance < 10:
                self.px = random.randrange(-500,WIDTH+500)
                self.py = random.randrange(-100,HEIGHT+100)

            if self.player_distance < 300:
                self.jumpscare_J = True

            self.px -= self.maze_speed

            self.rect.x = int(self.x)-(256/2)
            self.rect.y = int(self.y)-(256/2)

            monster_image = pygame.transform.rotate(self.monster,90-self.angle)
            screen.blit(monster_image, self.rect)                               
        def update(self):
            self.move()

    # Helper Functions
    def show_start_screen():
        screen.blit(start_screen, [0, 0])
        
    def show_end_screen():
        screen.blit(run,[0,0])

    def draw_grid():
        for x in range(-300, WIDTH+300, 40):
             pygame.draw.line(screen, WHITE, [x, 0], [x, HEIGHT], 1)
        for y in range(0, HEIGHT, 40):
            pygame.draw.line(screen, WHITE, [0, y], [WIDTH, y], 1)

        text = FONT_SM.render(str(p1.score), True, WHITE)
        rect = text.get_rect()
        rect.top = 20
        rect.right = WIDTH - 20
        screen.blit(text, rect)

        text = FONT_SM.render(str(p1.organ_score), True, WHITE)
        rect = text.get_rect()
        rect.top = 65
        rect.right = WIDTH - 20
        screen.blit(text, rect)

    # Make game objects
    ''' 
    Objects are instances of classes.
    '''

    p1 = Player(idleF,[(WIDTH/2)-32, (HEIGHT/2)-32], RED)

    players = [p1]

    w1 = Wall([448,448,128,128], WHITE)
    w2 = Wall([WIDTH,HEIGHT/2-(128/2),320,128], WHITE)
    w3 = Wall([0-320,HEIGHT/2-(128/2),320,128], WHITE)
    w4 = Wall([(WIDTH/2)-(192/2),0,192,320], WHITE)
    w5 = Wall([(WIDTH/2)-(192/2),HEIGHT-320,192,320], WHITE)
    w6 = Wall([WIDTH/10,HEIGHT/5,256+64,128], WHITE)
    w7 = Wall([WIDTH/5,0,128,256], WHITE)
    w8 = Wall([WIDTH/10,HEIGHT-HEIGHT/5-128,256+64,128], WHITE)
    w9 = Wall([WIDTH/5,HEIGHT-256,128,256], WHITE)
    w10 = Wall([WIDTH-WIDTH/10-(256+64),HEIGHT-HEIGHT/5-128,256+64,128], WHITE)
    w11 = Wall([WIDTH-WIDTH/5-(128),HEIGHT-256,128,256], WHITE)
    w12 = Wall([WIDTH-WIDTH/10-(256+64),HEIGHT/5,256+64,128], WHITE)
    w13 = Wall([WIDTH-WIDTH/5-(128),0,128,256], WHITE)
    w14 = Wall([WIDTH-200-200,HEIGHT/2-(128/2),200,128], WHITE)
    w15 = Wall([200,HEIGHT/2-(128/2),200,128], WHITE)
   
    wL = Wall([-WIDTH-500,0,WIDTH,HEIGHT], WHITE)
    wR = Wall([WIDTH+500,0,WIDTH,HEIGHT], WHITE)
    wU = Wall([(WIDTH/2)-WIDTH,0,2*WIDTH,40], WHITE)
    wD = Wall([(WIDTH/2)-WIDTH,HEIGHT-40,2*WIDTH,40], WHITE)


    walls = [w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,wL,wR,wU,wD]

    location_list = [[100-64+30,(HEIGHT/2)-32,64,64],[250,HEIGHT-160,64,64],[WIDTH-250-64,160-64,64,64],[WIDTH-100-30,(HEIGHT/2)-32,64,64],[WIDTH-250-64,HEIGHT-160,64,64],[250,160-64,64,64]]

    c1_loc = random.choice(location_list)
    location_list.remove(c1_loc)
    c1 = Coin(c1_loc, speed)

    c2_loc = random.choice(location_list)
    location_list.remove(c2_loc)                                                                                              
    c2 = Coin(c2_loc, sugar)

    c3_loc = random.choice(location_list)
    location_list.remove(c3_loc)
    c3 = Coin(c3_loc, needle)

    k1_loc = random.choice(location_list)
    location_list.remove(k1_loc)
    k1 = Keys(k1_loc, heart)

    k2_loc = random.choice(location_list)
    location_list.remove(k2_loc)
    k2 = Keys(k2_loc, eye)

    k3_loc = random.choice(location_list)
    location_list.remove(k3_loc)
    k3 = Keys(k3_loc, brain)

    items = [c1,c2,c3,k1,k2,k3]

    r1 = Ritual([(WIDTH/2)-((7*64)/2),(HEIGHT/2)-((4*64)/2),7*64,4*64],ritual)
    structures = [r1]

    blood_list = []

    m1 = Monster([0,0,256,256],monster1)
    monster_list = [m1]
    
    # Initial States

    grid_on = False
    vignette_on = True
    stage = START

    health = 5
    health_color = GREY
    regen = 0

    kill = 3
    hurt_ticks = 0

    music_on = True

    blinking_ticks = 0
    blink_speed = 2
    blinking_sign = blink_speed

    clock_ticks = 0
    time_ticks = 0

    text_length = 10

    angle = 0

    monster_effect_y = -15000
    monster_effect_x = -WIDTH

    transition_on = False
    transition_ticks = 0
    start_game = False

    fade_ticks = 300
    danger_fade_ticks = 0

    end_credit_ticks = 0

    fullscreen = True

    space_color = DARKGREY

    organ_timer = 30

    face_index = 0
    face = face_list[face_index]
    face_ticks = 0

    jumpscare_on = False
    
    warning1_fade = 0
    warning1_speed = 2

    warning2_fade = 0
    warning2_speed = 2

    warning3_fade = 0
    warning3_speed = 2

    organ_timer_color = DARKGREY

    jumpscare_ticks = 0

    win = 0

    # Game loop
    done = False

    while not done:
        # Event processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    grid_on = not grid_on
                if event.key == pygame.K_SPACE:
                    if stage != END:
                        if angle > 3:
                            transition_on = True

                        if stage == START:
                            if transition_on == True and transition_ticks > 100:
                                start_game = True
                        
                        if stage == PLAYING and p1.organ_score > 0:
                            p1.space_timer = 0
                            c = random.randrange(0,10)
                            if c == 0:
                                breath.play()
                if event.key == pygame.K_p:
                    if vignette_on == True:
                        vignette_on = False
                    else:
                        vignette_on = True
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_r:
                    restart = True
                if event.key == pygame.K_6:
                    kill -= 1
                if event.key == pygame.K_a:
                    p1.check_goal()
                if event.key == pygame.K_r:
                    play()
            '''if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)'''
                







        pressed = pygame.key.get_pressed()

        if stage == PLAYING and fade_ticks < 0:
            if (pressed[pygame.K_UP] == pressed[pygame.K_DOWN]):
                p1.stop_y()
            elif pressed[pygame.K_UP]:
                p1.go_up()
            elif pressed[pygame.K_DOWN]:
                p1.go_down()

            if (pressed[pygame.K_LEFT] == pressed[pygame.K_RIGHT]):
                p1.stop_x()
            elif pressed[pygame.K_LEFT]:
                p1.go_left()
            elif pressed[pygame.K_RIGHT]:
                p1.go_right()


      
        
        # Logic        
        if stage == START:
            if music_on == True:
                pygame.mixer.music.load('music/startmusic.ogg')
                pygame.mixer.music.play()
                pygame.mixer.music.play(-1)
                music_on = False
        
        if stage == PLAYING:
            if music_on == False:
                pygame.mixer.music.fadeout(2000)
                if pygame.mixer.music.get_busy() == True:
                    pygame.mixer.music.unload()
                    pygame.mixer.music.set_volume(.3)
                    pygame.mixer.music.load('music/music.ogg')
                    pygame.mixer.music.play()
                    pygame.mixer.music.play(-1)
                    music_on = True
            
            p1.update()

            monster = random.randrange(0,2500)
            if monster == 0:
                monstersound.play()
                monstersound.fadeout(5000)
            
            blinking_ticks += blinking_sign

            if blinking_ticks > 125:
                blinking_sign = -blink_speed
            if blinking_ticks < 0:
                blinking_sign = blink_speed

            for p in players:
                if p.speed_time > 30 and (health_length/50)*100 < 1000:
                    health_fade = 180
                    health += .01
                    health_color = GREEN
                else:
                    health_color = GREY

            if p1.reach_goal == True:
                stage = END


            hurt_ticks -= 1

            if p1.vx != 0 or p1.vy != 0:
                coughing = random.randrange(0,(250*p1.virus))
                if coughing == 0:
                    for p in players:
                        p.cough()
                        health -= 1
                        hurt_ticks = 20
                        health_fade = 180

            if p1.vx == 0 and p1.vy == 0 and p.speed_time < 30:
                health_color = DARKGREY

            if hurt_ticks > 10:
                health_color = RED


        health_length = 100*health+regen
        if health_length > 250 and (health_length/50)*100 < 500 and (p1.vx == 0 and p1.vy == 0):
            regen += .1
            
        if health_length <= 250 and (p1.vx == 0 and p1.vy == 0):
            regen += .5
            
        if health_length <= 200:
            health_color = DARKRED


        # Drawing code
        screen.fill(LIGHTGREY)
        
        for s in structures:
            if p1.organ_score > 1:
                s.draw()
            s.update()

        for b in blood_list:
            b.draw()
            b.update()

        for p in players:
            p.draw()

        for w in walls:
            w.draw()
            w.update()

        for i in items:
            i.draw()
            i.update()
            
        if stage == PLAYING and p1.organ_score > 0:
            for m in monster_list:
                m.draw()
                m.update()


        if vignette_on == True:
            screen.blit(vignette2x,[p.rect.x - 970, p.rect.y - 1170])
            lowhealthvignette.set_alpha(danger_fade_ticks)
            screen.blit(lowhealthvignette,[0,0])
            if health_length <= 200 or organ_timer < 10:
                danger_fade_ticks = 255
            else:
                danger_fade_ticks -= 1

        if grid_on:
            draw_grid()
            
        if stage == START:
            monster = random.randrange(0,2500)
            if monster == 0:
                monstersound.set_volume(.1)
                monstersound.play()
                monstersound.fadeout(5000)
            show_start_screen()
            angle += .08 
            screen_effect_image = pygame.transform.rotate(start_effect,angle)
            screen.blit(screen_effect_image, ((WIDTH/2)-int(screen_effect_image.get_width()/2), (HEIGHT/2)-int(screen_effect_image.get_height()/2)))
            monster_effect_y += 300
            screen.blit(horror14x, [monster_effect_x, monster_effect_y])
            if monster_effect_y > (HEIGHT+30000):
                monster_effect_spawn = random.randrange(-300,750)
                if monster_effect_spawn == 0:
                    monster_effect_y = -10000
                    monster_effect_x = random.randrange(int(-WIDTH-(WIDTH/2)),int(WIDTH/2))
            screen.blit(start_vignette, [0, 0])
            if angle > 5:
                screen.blit(start_text1,[0,0])
                start_text.set_alpha((angle-5)*75)
                screen.blit(start_text, [0, 0])
            else:
                screen.blit(start_text1,[0,0])

            fade_ticks -= 20
            if fade_ticks > 0:
                blackscreen.set_alpha(fade_ticks)
                screen.blit(blackscreen, [0,0,0,0])


            if transition_on == True:
                transition_ticks += 2

                screen.fill(BLACK)
                
                text = FONT_SM.render("Collect 3 organs.", True, WHITE)
                text.set_alpha(100)
                rect = text.get_rect()
                rect.centerx = WIDTH/2
                rect.centery = HEIGHT/2 - 330
                screen.blit(text, rect)

                text = FONT_SM.render("Arrows to move.", True, WHITE)
                text.set_alpha(100)
                rect = text.get_rect()
                rect.centerx = WIDTH/2
                rect.centery = HEIGHT/2 - 220
                screen.blit(text, rect)

                text = FONT_SM.render("The top bar is how long you have until you NEED to find an organ.", True, WHITE)
                text.set_alpha(100)
                rect = text.get_rect()
                rect.centerx = WIDTH/2
                rect.centery = HEIGHT/2 - 110
                screen.blit(text, rect)

                text = FONT_SM.render("The bottom bar is your health. The more you move, the more you lose health.", True, WHITE)
                text.set_alpha(100)
                rect = text.get_rect()
                rect.centerx = WIDTH/2
                rect.centery = HEIGHT/2
                screen.blit(text, rect)
                
                text = FONT_SM.render("Stay still to heal or collect healing items.", True, WHITE)
                text.set_alpha(100)
                rect = text.get_rect()
                rect.centerx = WIDTH/2
                rect.centery = HEIGHT/2 + 110
                screen.blit(text, rect)

                text = FONT_SM.render("Press [ESC] to exit and [R] to restart.", True, WHITE)
                text.set_alpha(100)
                rect = text.get_rect()
                rect.centerx = WIDTH/2
                rect.centery = HEIGHT/2 + 220
                screen.blit(text, rect)

                if transition_ticks > 120:
                    text = FONT_MD.render("Press [SPACE] to continue", True, WHITE)
                    text.set_alpha((transition_ticks-120)*5)
                    rect = text.get_rect()
                    rect.centerx = WIDTH/2
                    rect.centery = HEIGHT/2 + 330
                    screen.blit(text, rect)
                        
        if start_game == True:
            stage = PLAYING
            fade_ticks = 300
            start_game = False


        if stage == PLAYING:
            fade_ticks -= 3
            if fade_ticks > 0:
                blackscreen.set_alpha(fade_ticks)
                screen.blit(blackscreen, [0,0,0,0])
            
            clock_ticks += 1
            if clock_ticks % 60 == 0:
                time_ticks += 1
            text = FONT_SM.render(str(time_ticks), True, WHITE)
            text.set_alpha(100)
            rect = text.get_rect()
            rect.centerx = WIDTH/2
            rect.top = 50
            screen.blit(text, rect)

            rect.centerx = WIDTH/2
            rect.centery = HEIGHT/2
            pygame.draw.rect(screen, health_color,[rect.centerx - (((health_length/50)*100)/2),HEIGHT - 65,(health_length/50)*100,5])



            if clock_ticks % 60 == 0:
                organ_timer -= 1
            pygame.draw.rect(screen, organ_timer_color,[rect.centerx - (((organ_timer/30)*1000)/2),HEIGHT - 85,(organ_timer/30)*1000,5])

            if organ_timer < 10:
                organ_timer_color = DARKRED
            else:
                organ_timer_color = DARKGREY


            if p1.organ_timer_reset == True:
                organ_timer = 30
                p1.organ_timer_reset = False

        
            if r1.rect.contains(p1.rect) and p1.organ_score == 3:
                text = FONT_SM.render("Press [A]", True, WHITE)
                text.set_alpha(blinking_ticks)
                screen.blit(text, [rect.centerx/3,rect.centery,0,0])
            else:
                if blinking_ticks > 0:
                    blinking_ticks -= 3
                    text = FONT_SM.render("Press [A]", True, WHITE)
                    text.set_alpha(blinking_ticks)
                    screen.blit(text, [rect.centerx/3,rect.centery,0,0])

            if p1.organ_score == 1:
                warning1_fade += warning1_speed
                text = FONT_SM.render("Spam [SPACE] to run", True, WHITE)
                text.set_alpha(warning1_fade)
                screen.blit(text, [rect.centerx/3-80,rect.centery,0,0])
                if warning1_fade > 270:
                    warning1_speed = -2

            if organ_timer < 10:
                warning2_fade += warning2_speed
                text = FONT_SM.render("Find another organ soon", True, WHITE)
                text.set_alpha(warning2_fade)
                screen.blit(text, [rect.centerx+(rect.centerx/3),rect.centery,0,0])
                if warning2_fade > 255:
                    warning2_fade = 255
            else:
                if warning2_fade > 0:
                    warning2_fade -= 3
                    text = FONT_SM.render("Find another organ soon", True, WHITE)
                    text.set_alpha(warning2_fade)
                    screen.blit(text, [rect.centerx+(rect.centerx/3),rect.centery,0,0])

            if p1.organ_score == 3:
                warning3_fade += warning3_speed
                text = FONT_SM.render("Find the pentagram", True, WHITE)
                text.set_alpha(warning3_fade)
                screen.blit(text, [rect.centerx+(rect.centerx/3),rect.centery,0,0])
                if warning3_fade > 270:
                    warning3_speed = -2

        if m1.jumpscare_J == True and m1.player_distance < 300:
            jumpscare_ticks += 1
            jumpscare = random.randrange(0,5)
            if jumpscare_ticks < 600:
                if 2 >= jumpscare_ticks % 2 >= 0:
                    if jumpscare == 0:
                        screen.blit(fade,(0,0,0,0))
            else:
                jumpscare_ticks = 0
                m1.jumpscare_J = False



        if m1.player_distance < 90 and m1.player_distance != 0:
            jumpscare_on = True
        
        if jumpscare_on == True:
            face_ticks += 1
            if face_ticks % 3 == 0:
                face_index += 1
                if face_index > 2:
                    face_index = 0
            face = face_list[face_index]
            pygame.draw.rect(screen, BLACK,[0,0,WIDTH,HEIGHT])
            screen.blit(face,((WIDTH/2)-(544),0,0,0))

            if face_ticks > 100:
                stage = END
                win = 1

        elif health_length <= 0:
            stage = END
            win = 3

        elif organ_timer <= 0:
            stage = END
            win = 2

        elif kill <= 0:
            break



        if stage == END:
            if win == 0:
                pygame.draw.rect(screen, DARKGREY,[0,0,WIDTH,HEIGHT])
            else:
                pygame.draw.rect(screen, RED,[0,0,WIDTH,HEIGHT])
            end_credit_ticks += 1

            if end_credit_ticks > 50 and win == 0:
                text = FONT_SM.render("You've completed beta version " + VERSION +".", True, WHITE)
                text.set_alpha(150)
                rect = text.get_rect()
                rect.centerx = WIDTH/2
                rect.centery = HEIGHT/2 - 200
                screen.blit(text, rect)

            elif end_credit_ticks > 50 and win == 1:
                text = FONT_SM.render("You've been ripped apart.", True, WHITE)
                text.set_alpha(150)
                rect = text.get_rect()
                rect.centerx = WIDTH/2
                rect.centery = HEIGHT/2 - 200
                screen.blit(text, rect)

            elif end_credit_ticks > 50 and win == 2:
                text = FONT_SM.render("Your organs fell out.", True, WHITE)
                text.set_alpha(150)
                rect = text.get_rect()
                rect.centerx = WIDTH/2
                rect.centery = HEIGHT/2 - 200
                screen.blit(text, rect)

            elif end_credit_ticks > 50 and win == 3:
                text = FONT_SM.render("You coughed up too much blood.", True, WHITE)
                text.set_alpha(150)
                rect = text.get_rect()
                rect.centerx = WIDTH/2
                rect.centery = HEIGHT/2 - 200
                screen.blit(text, rect)

            if end_credit_ticks > 150:
                text = FONT_SM.render("Your time is " + str(time_ticks) + " seconds.", True, WHITE)
                text.set_alpha(150)
                rect = text.get_rect()
                rect.centerx = WIDTH/2
                rect.centery = HEIGHT/2 - 100
                screen.blit(text, rect)

            if end_credit_ticks > 250:
                text = FONT_SM.render("Made by Victor I. Pham", True, WHITE)
                text.set_alpha(150)
                rect = text.get_rect()
                rect.centerx = WIDTH/2
                rect.centery = HEIGHT/2
                screen.blit(text, rect)

            if end_credit_ticks == 300 :
                response = random.choice(credit_reply)
            
            if end_credit_ticks > 350:
                text = FONT_SM.render(response, True, WHITE)
                text.set_alpha(150)
                rect = text.get_rect()
                rect.centerx = WIDTH/2
                rect.centery = HEIGHT/2 + 100
                screen.blit(text, rect)

            if end_credit_ticks > 500:
                text = FONT_SM.render("Press [R] to restart", True, WHITE)
                text.set_alpha(225)
                rect = text.get_rect()
                rect.centerx = WIDTH/2
                rect.centery = HEIGHT/2 + 200
                screen.blit(text, rect)

            if end_credit_ticks == 50:
                print("             ___________")
                print("            '._==_==_=_.'")
                print("            .-\:      /-.")
                print("           | (|:.     |) |")
                print("            '-|:.     |-'")
                print("              \::.    /")
                print("               '::. .'")
                print("                 ) (")
                print("               _.' '._")
                print("              `=======`")


        

        
        # Update screen
        pygame.display.flip()
        clock.tick(refresh_rate)

    # Close window on quit
    pygame.quit()

play()

