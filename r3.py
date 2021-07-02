import sys
import pygame
import threading
import time
import datetime
import platform
import subprocess
#introplay = "ffplay -autoexit -window_title Intro intro.ogv"
#process = subprocess.Popen(introplay.split(), stdout=subprocess.PIPE)
#output, error = process.communicate()
pygame.init()
pygame.joystick.init()
if pygame.joystick.get_count() == 0:
    print ("Please connect a compatible joystick")
else:
    joystick = pygame.joystick.Joystick(0)
    #tested with ds4 controller on rpi, please use joysticktest script to test your controller
    joystick.init()
    if (int(joystick.get_numaxes()) > 3) & ((str(platform.machine()) == "x86") | (str(platform.machine()) == "AMD64")):
        gamepad = 1
        compatible = True
        
    elif int(joystick.get_numaxes()) > 4:
        gamepad = 2
        compatible = True
    else:
        compatible = False
    if compatible:
        screen = pygame.display.set_mode((800, 480))
        pygame.display.set_caption('The Red Robot Radio - Virtualx Game Engine')
        font = pygame.font.Font(None, 30)
        clock = pygame.time.Clock()
        FPS = 6000
        BLACK = (0, 0, 0)
        #WHITE = (255, 255, 255)
        pygame.mixer.music.load('space.ogg')
        csfx = pygame.mixer.Sound('crash.ogg')
        lcfx = pygame.mixer.Sound('complete.ogg')
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
                self.image = pygame.image.load('galaxy.png')
                #self.image = pygame.Surface((32, 32))
                #self.image.fill(WHITE)
                self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
                self.velocity = [0, 0]
            def update(self):
                self.rect.move_ip(*self.velocity)
        class Supernova(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load('supernova.png')
                #self.image = pygame.Surface((32, 32))
                #self.image.fill(WHITE)
                self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
                self.velocity = [0, 0]
        class Antenna(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__()
                self.image = pygame.image.load('antenna.png')
                #self.image = pygame.Surface((32, 32))
                #self.image.fill(WHITE)
                self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
                self.velocity = [0, 0]
        class Player(pygame.sprite.Sprite):
            def __init__(self,xset,yset):
                pygame.sprite.Sprite.__init__(self)
                self.x = xset
                self.y = yset
                self.image = pygame.image.load('ss.png')
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
                #self.image = pygame.Surface((32, 32))
                #self.image.fill(WHITE)
                #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
                self.rect = pygame.Rect(self.x,self.y,50, 1000)
                self.velocity = [0, 0]
            def update(self):
                self.rect.move_ip(*self.velocity)
        class Wallv(pygame.sprite.Sprite):
            def __init__(self,xset,yset):
                pygame.sprite.Sprite.__init__(self)
                self.x = xset
                self.y = yset
                #self.image = pygame.Surface((32, 32))
                #self.image.fill(WHITE)
                #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
                self.rect = pygame.Rect(self.x,self.y,3400, 50)
                self.velocity = [0, 0]
            def update(self):
                self.rect.move_ip(*self.velocity)
        class Css(pygame.sprite.Sprite):
            def __init__(self,xset,yset):
                pygame.sprite.Sprite.__init__(self)
                self.x = xset
                self.y = yset
                self.image = pygame.image.load('css.png')
                #self.image = pygame.Surface((32, 32))
                #self.image.fill(WHITE)
                #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
                self.rect = pygame.Rect(self.x,self.y,108, 68)
                self.velocity = [0, 0]
            def update(self):
                self.rect.move_ip(*self.velocity)
        class Sat(pygame.sprite.Sprite):
            def __init__(self,xset,yset):
                pygame.sprite.Sprite.__init__(self)
                self.x = xset
                self.y = yset
                self.image = pygame.image.load('sat.png')
                #self.image = pygame.Surface((32, 32))
                #self.image.fill(WHITE)
                #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
                self.rect = pygame.Rect(self.x,self.y,30, 22)
                self.velocity = [0, 0]
            def update(self):
                self.rect.move_ip(*self.velocity)
        class Goal(pygame.sprite.Sprite):
            def __init__(self,xset,yset):
                pygame.sprite.Sprite.__init__(self)
                self.x = xset
                self.y = yset
                self.image = pygame.image.load('radio.png')
                #self.image = pygame.Surface((32, 32))
                #self.image.fill(WHITE)
                #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
                self.rect = pygame.Rect(self.x,self.y,69, 120)
                self.velocity = [0, 0]
            def update(self):
                self.rect.move_ip(*self.velocity)
        class Ast(pygame.sprite.Sprite):
            def __init__(self,xset,yset):
                pygame.sprite.Sprite.__init__(self)
                self.x = xset
                self.y = yset
                self.image = pygame.image.load('asteroid.png')
                #self.image = pygame.Surface((32, 32))
                #self.image.fill(WHITE)
                #self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
                self.rect = pygame.Rect(self.x,self.y,108, 78)
                self.velocity = [0, 0]
            def update(self):
                self.rect.move_ip(*self.velocity)
        player = Player(12,190)
        css1 = Css(400,190)
        css2 = Css(500,400)
        sat1 = Sat(550,-100)
        sat2 = Sat(600,100)
        goal = Goal(3000,-100)
        ast1 = Ast(120,200)
        ast2 = Ast(300,100)
        ast3 = Ast(500,150)
        wall1 = Wallh(-100,-200)
        wall2 = Wallh(3100,-200)
        wall3 = Wallv(-200,-200)
        wall4 = Wallv(-200,800)
        background = Background()
        supernova = Supernova()
        antenna = Antenna()
        running = True
        live = True
        complete = False
        debug = False # This set debug mode
        #rect = pygame.Rect((0, 0), (32, 32))
        #image = pygame.Surface((32, 32))
        #image.fill(WHITE)
        start_time = pygame.time.get_ticks()
        runtime = 0
        while running:
            dt = clock.tick(FPS) / 1000
            #screen.fill(BLACK)
            datetime.datetime.now()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            #ax and ay are for left stick
            ax = joystick.get_axis(0)
            ay = joystick.get_axis(1)
            if gamepad == 1:
                #bx and by are for right stick
                bx = joystick.get_axis(2)
                by = joystick.get_axis(3)
            elif gamepad == 2:
                #bx and by are for right stick
                bx = joystick.get_axis(3)
                by = joystick.get_axis(4)
            #b0 is for cross button on ds4
            b0 = joystick.get_button(0)
            #b1 is for circle button on ds4
            b1 = joystick.get_button(1)
            #b2 is for triangle button on ds4
            b2 = joystick.get_button(2)
            #b3 is for square button on ds4
            b3 = joystick.get_button(3)
            if live:
                runtime = pygame.time.get_ticks() - start_time
                if (live & debug == False):
                    if pygame.sprite.collide_rect(player, wall3):
                        if ay < 0:
                            ay = 0
                    elif pygame.sprite.collide_rect(player, wall4):
                        if ay > 0:
                            ay = 0
                    if pygame.sprite.collide_rect(player, wall1):
                        if ax < 0:
                            ax = 0
                    elif pygame.sprite.collide_rect(player, wall2):
                        if ax > 0:
                            ax = 0
                    if pygame.sprite.collide_rect(background, wall3):
                        if by < 0:
                            by = 0
                    elif pygame.sprite.collide_rect(background, wall4):
                        if by > 0:
                            by = 0
                    if pygame.sprite.collide_rect(background, wall1):
                        if bx < 0:
                            bx = 0
                    elif pygame.sprite.collide_rect(background, wall2):
                        if bx > 0:
                            bx = 0
                    if pygame.sprite.collide_rect(player, css1):
                        live = False
                        pygame.mixer.music.stop()
                        csfx.play()
                    elif pygame.sprite.collide_rect(player, css2):
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
                    elif pygame.sprite.collide_rect(player, goal):
                        live = False
                        complete = True
                        pygame.mixer.music.stop()
                        lcfx.play()
                player.velocity[0] = int(600 * dt * (ax - bx))
                player.velocity[1] = int(600 * dt * (ay - by))
                css1.velocity[0] = int(-600 * dt * bx)
                css1.velocity[1] = int(-600 * dt * by)
                css2.velocity = css1.velocity
                sat1.velocity = css1.velocity
                sat2.velocity = css1.velocity
                goal.velocity = css1.velocity
                wall1.velocity = css1.velocity
                wall2.velocity = css1.velocity
                wall3.velocity = css1.velocity
                wall4.velocity = css1.velocity
                ast1.velocity[0] = int(-200 * dt * bx)
                ast1.velocity[1] = int(-200 * dt * by)
                ast2.velocity[0] = int(-150 * dt * bx)
                ast2.velocity[1] = int(-150 * dt * by)
                ast3.velocity[0] = int(-120 * dt * bx)
                ast3.velocity[1] = int(-120 * dt * by)
            if b0:
                #this stop music playback
                pygame.mixer.music.stop()
            elif b1:
                #this start music playback
                pygame.mixer.music.play(-1)
            elif (b2 & debug):
                #this trigger spaceship crash event
                live = False
                pygame.mixer.music.stop()
                csfx.play()
            elif b3:
                #this restart the game
                player = Player(12,190)
                css1 = Css(400,190)
                css2 = Css(500,400)
                sat1 = Sat(550,-100)
                sat2 = Sat(600,100)
                goal = Goal(3000,-100)
                ast1 = Ast(120,200)
                ast2 = Ast(300,100)
                ast3 = Ast(500,150)
                wall1 = Wallh(-100,-200)
                wall2 = Wallh(3100,-200)
                wall3 = Wallv(-200,-200)
                wall4 = Wallv(-200,800)
                live = True
                complete = False
                pygame.mixer.music.play(-1)
                start_time = pygame.time.get_ticks()
            player.update()
            css1.update()
            css2.update()
            sat1.update()
            sat2.update()
            goal.update()
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
                screen.blit(ast1.image, ast2.rect)
                screen.blit(ast1.image, ast1.rect)
                screen.blit(player.image, player.rect)
                screen.blit(css1.image, css1.rect)
                screen.blit(css2.image, css2.rect)
                screen.blit(sat1.image, sat1.rect)
                screen.blit(sat2.image, sat2.rect)
                screen.blit(goal.image, goal.rect)
            elif complete:
                playhr = (int(runtime / 3600000))
                playmin = (int(runtime / 60000) - (playhr * 60))
                playsec = (int(runtime / 1000) - (playmin * 60) - (playhr * 3600))
                playmsec = (runtime - (playsec * 1000) - (playmin * 60000) - (playhr * 3600000))
                playtime = "%d:%02d:%02d:%03d" % (playhr, playmin, playsec, playmsec)
                screen.blit(antenna.image, antenna.rect)
                yourtimetext = font.render(str("Your Time"), True, pygame.Color('white'))
                screen.blit(yourtimetext, (450, 500))
                yourtime = font.render(str(playtime), True, pygame.Color('white'))
                screen.blit(yourtime, (450, 540))
            else:
                playhr = (int(runtime / 3600000))
                playmin = (int(runtime / 60000) - (playhr * 60))
                playsec = (int(runtime / 1000) - (playmin * 60) - (playhr * 3600))
                playmsec = (runtime - (playsec * 1000) - (playmin * 60000) - (playhr * 3600000))
                playtime = "%d:%02d:%02d:%03d" % (playhr, playmin, playsec, playmsec)
                screen.blit(supernova.image, supernova.rect)
                yourtimetext = font.render(str("Your Time"), True, pygame.Color('white'))
                screen.blit(yourtimetext, (450, 500))
                yourtime = font.render(str(playtime), True, pygame.Color('white'))
                screen.blit(yourtime, (450, 540))
            rfps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
            screen.blit(rfps, (50, 50))
            if debug:
                sysclock = font.render(str(datetime.datetime.utcnow()), True, pygame.Color('white'))
                cpuarch = font.render(str(platform.machine()), True, pygame.Color('white'))
                playcount = font.render(str(runtime), True, pygame.Color('white'))
                #infox = font.render(str(bx), True, pygame.Color('white'))
                #infoy = font.render(str(by), True, pygame.Color('white'))
                screen.blit(sysclock, (120, 50))
                screen.blit(cpuarch, (50, 80))
                screen.blit(playcount, (160, 80))
            #screen.blit(infox, (50, 110))
            #screen.blit(infoy, (50, 140))
            pygame.display.update()
    else:
        print ("Unknown Joystick Detected")
