import sys
import pygame
import threading
import time
import datetime
import platform
import subprocess
pygame.init()
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption('The Red Robot Radio 1.0.0 - Virtualx Game Engine')
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()
FPS = 6000
ax = 0
ay = 0
bx = 0
by = 0
cx = 0
cy = 0
dx = 0
dy = 0
ex = 0
ey = 0
music = False #To disable music at game start set to false
BLACK = (0, 0, 0)
#WHITE = (255, 255, 255)
pygame.mixer.music.load('music/space.ogg')
csfx = pygame.mixer.Sound('sfx/crash.ogg')
lcfx = pygame.mixer.Sound('sfx/complete.ogg')
if music:
    pygame.mixer.music.play(-1)
#sound = pygame.mixer.Sound(file='bmx.ogg')
#raw_array = sound.get_raw()
#raw_array = raw_array[100000:92557920]
#cut_sound = pygame.mixer.Sound(buffer=raw_array)
#cut_sound.play(-1)
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('backgrounds/galaxy.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.velocity = [0, 0]
    def update(self):
        self.rect.move_ip(*self.velocity)
class Crash(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('backgrounds/crash.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.velocity = [0, 0]
class Antenna(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('backgrounds/antenna.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.velocity = [0, 0]
    def update(self):
        self.rect.move_ip(*self.velocity)
class Player(pygame.sprite.Sprite):
    def __init__(self,xset,yset):
        pygame.sprite.Sprite.__init__(self)
        self.x = xset
        self.y = yset
        self.image = pygame.image.load('sprites/ss.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,108, 68)
        self.velocity = [0, 0]
    def update(self):
            self.rect.move_ip(*self.velocity)
class Wallh(pygame.sprite.Sprite):
    def __init__(self,xset,yset):
        pygame.sprite.Sprite.__init__(self)
        self.x = xset
        self.y = yset
        self.image = pygame.image.load('sprites/wallh.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,50, 1000)
        self.velocity = [0, 0]
    def update(self):
        self.rect.move_ip(bx, by)
class Wallv(pygame.sprite.Sprite):
    def __init__(self,xset,yset):
        pygame.sprite.Sprite.__init__(self)
        self.x = xset
        self.y = yset
        self.image = pygame.image.load('sprites/wallv.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,3400, 50)
        self.velocity = [0, 0]
    def update(self):
        self.rect.move_ip(bx, by)
class Css(pygame.sprite.Sprite):
    def __init__(self,xset,yset):
        pygame.sprite.Sprite.__init__(self)
        self.x = xset
        self.y = yset
        self.image = pygame.image.load('sprites/css.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,108, 68)
        self.velocity = [0, 0]
    def update(self):
        self.rect.move_ip(bx, by)
class Sat(pygame.sprite.Sprite):
    def __init__(self,xset,yset):
        pygame.sprite.Sprite.__init__(self)
        self.x = xset
        self.y = yset
        self.image = pygame.image.load('sprites/sat.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,30, 22)
        self.velocity = [0, 0]
    def update(self):
        self.rect.move_ip(bx, by)
class Goal(pygame.sprite.Sprite):
    def __init__(self,xset,yset):
        pygame.sprite.Sprite.__init__(self)
        self.x = xset
        self.y = yset
        self.image = pygame.image.load('sprites/radio.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,69, 120)
        self.velocity = [0, 0]
    def update(self):
        self.rect.move_ip(bx, by)
class Bus(pygame.sprite.Sprite):
    def __init__(self,xset,yset):
        pygame.sprite.Sprite.__init__(self)
        self.x = xset
        self.y = yset
        self.image = pygame.image.load('sprites/bus.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,118, 63)
        self.velocity = [0, 0]
    def update(self):
        self.rect.move_ip(bx, by)
class Tc(pygame.sprite.Sprite):
    def __init__(self,xset,yset):
        pygame.sprite.Sprite.__init__(self)
        self.x = xset
        self.y = yset
        self.image = pygame.image.load('sprites/tc.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,118, 63)
        self.velocity = [0, 0]
    def update(self):
        self.rect.move_ip(bx, by)
class Iss(pygame.sprite.Sprite):
    def __init__(self,xset,yset):
        pygame.sprite.Sprite.__init__(self)
        self.x = xset
        self.y = yset
        self.image = pygame.image.load('sprites/iss.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,98, 128)
        self.velocity = [0, 0]
    def update(self):
        self.rect.move_ip(bx, by)
class Ast1(pygame.sprite.Sprite):
    def __init__(self,xset,yset):
        pygame.sprite.Sprite.__init__(self)
        self.x = xset
        self.y = yset
        self.image = pygame.image.load('sprites/asteroid.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,108, 78)
        self.velocity = [0, 0]
    def update(self):
        self.rect.move_ip(cx, cy)
class Ast2(pygame.sprite.Sprite):
    def __init__(self,xset,yset):
        pygame.sprite.Sprite.__init__(self)
        self.x = xset
        self.y = yset
        self.image = pygame.image.load('sprites/asteroid.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,108, 78)
        self.velocity = [0, 0]
    def update(self):
        self.rect.move_ip(dx, dy)
class Ast3(pygame.sprite.Sprite):
    def __init__(self,xset,yset):
        pygame.sprite.Sprite.__init__(self)
        self.x = xset
        self.y = yset
        self.image = pygame.image.load('sprites/asteroid.png')
        #self.image = pygame.Surface((32, 32))
        #self.image.fill(WHITE)
        #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.rect = pygame.Rect(self.x,self.y,108, 78)
        self.velocity = [0, 0]
    def update(self):
        self.rect.move_ip(ex, ey)
player = Player(346,206)
css1 = Css(483,262)
css2 = Css(500,400)
css3 = Css(1582,470)
sat1 = Sat(550,-100)
sat2 = Sat(600,100)
sat3 = Sat(1240,120)
goal = Goal(1940,-16)
bus1 = Bus(600,656)
bus2 = Bus(1258,320)
bus3 = Bus(1970,524)
tc1 = Tc(854,472)
tc2 = Tc(1164,570)
tc3 = Tc(1760,680)
iss1 = Iss(878,140)
iss2 = Iss(1136,-6)
iss3 = Iss(1742,222)
ast1 = Ast1(120,200)
ast2 = Ast2(300,100)
ast3 = Ast3(500,150)
wall1 = Wallh(-100,-200)
wall2 = Wallh(2150,-200)
wall3 = Wallv(-200,-200)
wall4 = Wallv(-200,800)
background = Background()
crash = Crash()
antenna = Antenna()
running = True
live = True
complete = False
debug = False # This set debug mode
pygame.mouse.set_visible(False)
#rect = pygame.Rect((0, 0), (32, 32))
#image = pygame.Surface((32, 32))
#image.fill(WHITE)
start_time = pygame.time.get_ticks()
runtime = 0
pygame.event.set_grab(True)
while running:
    dt = clock.tick(FPS) / 1000
    #screen.fill(BLACK)
    datetime.datetime.now()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_m:
                pygame.mixer.music.play(-1)
            elif event.key == pygame.K_c:
                if debug:
                    #this trigger spaceship crash event
                    live = False
                    pygame.mixer.music.stop()
                    csfx.play()
            elif event.key == pygame.K_r:
                #this restart the game
                player = Player(346,206)
                css1 = Css(483,262)
                css2 = Css(500,400)
                css3 = Css(1582,470)
                sat1 = Sat(550,-100)
                sat2 = Sat(600,100)
                sat3 = Sat(1240,120)
                goal = Goal(1940,-16)
                bus1 = Bus(600,656)
                bus2 = Bus(1258,320)
                bus3 = Bus(1970,524)
                tc1 = Tc(854,472)
                tc2 = Tc(1164,570)
                tc3 = Tc(1760,680)
                iss1 = Iss(878,140)
                iss2 = Iss(1136,-6)
                iss3 = Iss(1742,222)
                ast1 = Ast1(120,200)
                ast2 = Ast2(300,100)
                ast3 = Ast3(500,150)
                wall1 = Wallh(-100,-200)
                wall2 = Wallh(2150,-200)
                wall3 = Wallv(-200,-200)
                wall4 = Wallv(-200,800)
                live = True
                complete = False
                if music:
                    pygame.mixer.music.play(-1)
                start_time = pygame.time.get_ticks()
            elif event.key == pygame.K_ESCAPE:
                quit()
        if event.type == pygame.MOUSEMOTION:
            #This control camera
            pygame.mouse.set_pos([400, 240])
            ax, ay = event.rel
            bx = ax * 7
            by = ay * 7
            cx = ax * 3
            cy = ay * 3
            dx = ax * 2
            dy = ay * 2
            ex = ax * 1
            ey = ay * 1


    if live:
        runtime = pygame.time.get_ticks() - start_time
        if (live & debug == False):
            if pygame.sprite.collide_rect(player, wall3):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, wall4):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, wall1):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, wall2):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, css1):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, css2):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, css3):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, sat1):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, sat2):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, sat3):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, bus1):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, bus2):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, tc1):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, tc2):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, iss1):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, iss2):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, iss3):
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif pygame.sprite.collide_rect(player, goal):
                live = False
                complete = True
                pygame.mixer.music.stop()
                lcfx.play()
    player.update()
    css1.update()
    css2.update()
    css3.update()
    sat1.update()
    sat2.update()
    sat3.update()
    goal.update()
    bus1.update()
    bus2.update()
    bus3.update()
    tc1.update()
    tc2.update()
    tc3.update()
    iss1.update()
    iss2.update()
    iss3.update()
    ast1.update()
    ast2.update()
    ast3.update()
    wall1.update()
    wall2.update()
    wall3.update()
    wall4.update()
    if live:
        screen.blit(background.image, background.rect)
        screen.blit(ast3.image, ast3.rect)
        screen.blit(ast2.image, ast2.rect)
        screen.blit(ast1.image, ast1.rect)
        screen.blit(player.image, player.rect)
        screen.blit(css1.image, css1.rect)
        screen.blit(css2.image, css2.rect)
        screen.blit(css3.image, css3.rect)
        screen.blit(sat1.image, sat1.rect)
        screen.blit(sat2.image, sat2.rect)
        screen.blit(sat3.image, sat3.rect)
        screen.blit(goal.image, goal.rect)
        screen.blit(bus1.image, bus1.rect)
        screen.blit(bus2.image, bus2.rect)
        screen.blit(bus3.image, bus3.rect)
        screen.blit(tc1.image, tc1.rect)
        screen.blit(tc2.image, tc2.rect)
        screen.blit(tc3.image, tc3.rect)
        screen.blit(iss1.image, iss1.rect)
        screen.blit(iss2.image, iss2.rect)
        screen.blit(iss3.image, iss3.rect)
        screen.blit(wall1.image, wall1.rect)
        screen.blit(wall2.image, wall2.rect)
        screen.blit(wall3.image, wall3.rect)
        screen.blit(wall4.image, wall4.rect)
    elif complete:
        playhr = (int(runtime / 3600000))
        playmin = (int(runtime / 60000) - (playhr * 60))
        playsec = (int(runtime / 1000) - (playmin * 60) - (playhr * 3600))
        playmsec = (runtime - (playsec * 1000) - (playmin * 60000) - (playhr * 3600000))
        playtime = "%d:%02d:%02d:%03d" % (playhr, playmin, playsec, playmsec)
        screen.blit(antenna.image, antenna.rect)
        yourtimetext = font.render(str("Your Time"), True, pygame.Color('white'))
        screen.blit(yourtimetext, (350, 400))
        yourtime = font.render(str(playtime), True, pygame.Color('white'))
        screen.blit(yourtime, (350, 440))
    else:
        playhr = (int(runtime / 3600000))
        playmin = (int(runtime / 60000) - (playhr * 60))
        playsec = (int(runtime / 1000) - (playmin * 60) - (playhr * 3600))
        playmsec = (runtime - (playsec * 1000) - (playmin * 60000) - (playhr * 3600000))
        playtime = "%d:%02d:%02d:%03d" % (playhr, playmin, playsec, playmsec)
        screen.blit(crash.image, crash.rect)
        yourtimetext = font.render(str("Your Time"), True, pygame.Color('white'))
        screen.blit(yourtimetext, (350, 400))
        yourtime = font.render(str(playtime), True, pygame.Color('white'))
        screen.blit(yourtime, (350, 440))
    rfps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
    screen.blit(rfps, (50, 50))
    if debug:
        sysclock = font.render(str(datetime.datetime.utcnow()), True, pygame.Color('white'))
        cpuarch = font.render(str(platform.machine()), True, pygame.Color('white'))
        playcount = font.render(str(runtime), True, pygame.Color('white'))
        infox = font.render(str(bx), True, pygame.Color('white'))
        infoy = font.render(str(by), True, pygame.Color('white'))
        screen.blit(sysclock, (120, 50))
        screen.blit(cpuarch, (50, 80))
        screen.blit(playcount, (160, 80))
        screen.blit(infox, (50, 110))
        screen.blit(infoy, (50, 140))
    pygame.display.update()