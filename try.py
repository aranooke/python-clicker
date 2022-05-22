import pygame
from pygame.draw import *;
from random import*

pygame.init();

# Поймай шарик
BLACK = (0,0,0);
FPS = 10;
clock = pygame.time.Clock();
screen = pygame.display.set_mode((400,400));
finished = False;

def audio():
    pygame.mixer.music.load("gradsky.mp3");
    pygame.mixer.music.play();

def textCounter(counter = 0):
    
    pygame.font.init();
    font = pygame.font.SysFont('arial',32);
    text = font.render("Счетчик попаданий:{0}".format(counter),False,(255,255,255));
    screen.blit(text,(60,20));
    
def clear_window():
    rect(screen,BLACK,(0,0,400,400));
    
def rand():
    global x,y,radius;
    color1,color2,color3 = randint(0,255),randint(0,255),randint(0,255);
    x = randint(30,350);
    y = randint(30,350);
    radius = randint(5,20);
    circle(screen,(color1,color2,color3),(x,y),radius);

def click():
    print("x: ",x,"y: ",y,"r: ",radius);

def check_click():
                    
                    xSide1 = x + radius;
                    xSide2 = x - radius;
                    
                    ySide1 = y + radius;
                    ySide2 = y - radius;
                    
                    if xSide2 < event.pos[0] < xSide1 and ySide2 < event.pos[1] < ySide1:
                        print("Ты попал");
                        
                    else:
                        print("Не попал");

audio();
while not finished:
    clock.tick(FPS);
    pygame.display.update();
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            finished = True;
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                
                clear_window();
                textCounter();
                rand();
            if event.button == 1:
                check_click();
                click();
                
            
        

pygame.display.update();
pygame.quit();

