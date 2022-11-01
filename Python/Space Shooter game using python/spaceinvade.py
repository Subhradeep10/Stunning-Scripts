import pygame
import os
import time
import random

WIDTH,HEIGHT=750,750
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space shooter tutorial")

#load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("D:\spaceinvader","pixel_player_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("D:\spaceinvader\assets","pixel_player_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("D:\spaceinvader\assets","pixel_player_blue_small.png"))

#MAIN PLAYER
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("D:\spaceinvader\assets","pixel_player_yellow.png"))

#lasers
RED_LASER=pygame.image.load(os.path.join("D:\spaceinvader\assets","pixel_laser_red.png"))
GREEN_LASER=pygame.image.load(os.path.join("D:\spaceinvader\assets","pixel_laser_green.png"))
BLUE_LASER=pygame.image.load(os.path.join("D:\spaceinvader\assets","pixel_laser_blue.png"))
YELLOW_LASER=pygame.image.load(os.path.join("D:\spaceinvader\assets","pixel_laser_yellow.png"))

#bg
BG=pygame.transform.scale(pygame.image.load(os.path.join("D:\spaceinvader\assets","background-black.png")),(WIDTH,HEIGHT))
    
class player:
    def __init__(self,x,y,health=100):
        self.x=x
        self.y=y
        self.health=health
        self.player_img=none
        self.laser_img = none
        self.lasers=[]
        self.cool_down_counter = 0
        
    def draw(self,window):
        window.blit(self.player_img,(self.x,self.y))
        

        
class Player(ship):
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.player_img=YELLOW_SPACE_player
        self.laser_img =YELOW_LASER
        self.mask = pygame.mask.from_surface(self.player_img)
        self.max_health=health

class Enemy(Ship):
    COLOR_MAP={
    "red":(RED_SPACE_SHIP,RED_LASER),
    "green": (GREEN_SPACE_SHIP,GREEN_LASER),
    "blue": (BLUE_SPACE_SHIP,BLUE_LASER)    }

    def__init__(self,x,y,color,health=100)
    super().__init__(x,y,health)


    def move(self,vel):
        self.y +=vel


        
    


def main():
    run=True
    FPS=60
    level=1
    lives=5
    main_font = pygame.font.sysFont("comicsans",50)
    lost_font = pygame.font.sysFont("comicsans",50)


    enemies=[]
    wave_length=5
    enemy_vel=1
    
    player_vel= 5
    
    player=player(300,650)
    clock=pygame.time.Clock()

    lost=False
    
    def redraw_window():
        WIN.blit(BG,(0,0))
        #draw text
        lives_label = main_font.render(f"Lives:{lives}",1,(255,255,255))
        level_label = main_font.render(f"Level:{level}",1,(255,255,255))
        
        WIN.blit(lives_label,(10,10))
        WIN.blit(level_label,(WIDTH-level_label.get_width -10,10))
        
        for enemy in enemies:
            enemy.draw(WIN)
        
        player.draw(WIN)

        if lost:
            lost_label=lost_font.render("You Lost!!",1,(255,255,255))
            WIN.blit(lost_label,(WIDTH/2- lost_label.get_width()/2,350))


        
        pygame.display.update()

        
    while run:
        clock.tick(FPS)

        if lives<=0 or player.health<=0:
            lost=True



        if len (enemies)==0:
            level+=1
            wave_length+=5
            for i in range (wave_length):
                enemy=Enemy(random.randrange(50,WIDTH-100),random.randrange(-1500,-100),random.choice(["red","blue","green"]))
                enemies.append(enemy)
        
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        
        keys =pygame.key.get_pressed()
        if keys[pygame.k_a] and player.x - player_vel > 0: #left
            player.x -=player_vel
        if keys[pygame.k_d] and player.x + player_vel + player.get_width() < WIDTH: #right
            player.x +=player_vel
        if keys[pygame.k_w] and player.y - player_vel > 0: #up
            player.y -=player_vel 
        if keys[pygame.k_s] and player.y + player_vel + player.get_height() < HEIGHT:  #down
            player.y +=player_vel 

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            if enemy.y+enemy.get_height() > HEIGHT:
                lives-=1
                enemies.remove(enemy)


    redraw_window()