import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Morski Shah')
clock = pygame.time.Clock()

#timers
timer = 0
timerstart = False

#img loading
background = pygame.image.load("img/bg.png")
background_rect = background.get_rect(topleft=(0,0))

crossimg = pygame.image.load("img/x.png")
cross_rect = crossimg.get_rect(topleft=(0,0))

circleimg = pygame.image.load("img/circle.png")
circle_rect = circleimg.get_rect(topleft=(0,0))



randomint = random.randint(0,1)
turns = ["cross","circle"]
turn = turns[randomint]
crosspos = []
circlepos = []

#fonts
text_font = pygame.font.SysFont("Arial",40)

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

#important variables
gameended = False
winner = None

class Kvadrat:
    def __init__(self,x,y,used,tip):
        self.x = x
        self.y = y
        self.used = used
        self.tip = tip
        self.img = pygame.image.load("img/kvadrat.png")
        self.rect = self.img.get_rect(topleft=(self.x,self.y))

kvadrat1 = Kvadrat(0,0,False,None)
kvadrat2 = Kvadrat(266,0,False,None)
kvadrat3 = Kvadrat(532,0,False,None)
kvadrat4 = Kvadrat(0,200,False,None)
kvadrat5 = Kvadrat(266,200,False,None)
kvadrat6 = Kvadrat(532,200,False,None)
kvadrat7 = Kvadrat(0,400,False,None)
kvadrat8 = Kvadrat(266,400,False,None)
kvadrat9 = Kvadrat(532,400,False,None)

running = True
while running:
    mousepos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                kvadrat1.tip = None
                kvadrat2.tip = None
                kvadrat3.tip = None
                kvadrat4.tip = None
                kvadrat5.tip = None
                kvadrat6.tip = None
                kvadrat7.tip = None
                kvadrat8.tip = None
                kvadrat9.tip = None
                winner = None
                kvadrat1.used = False
                kvadrat2.used = False
                kvadrat3.used = False
                kvadrat4.used = False
                kvadrat5.used = False
                kvadrat6.used = False
                kvadrat7.used = False
                kvadrat8.used = False
                kvadrat9.used = False
                crosspos = []
                circlepos = []
                gameended = False
                randomint = random.randint(0,1)
                turn = turns[randomint]
                timerstart = False
                timer = 0

        if event.type == pygame.MOUSEBUTTONDOWN:            
            if kvadrat1.rect.collidepoint(mousepos) and kvadrat1.used == False and gameended == False:
                kvadrat1.used = True
                if turn == "cross":
                    crosspos.append([50,30])
                    kvadrat1.tip = 1
                    turn = "circle"
                elif turn == "circle":
                    circlepos.append([50,30])
                    kvadrat1.tip = 0
                    turn = "cross"
            elif kvadrat2.rect.collidepoint(mousepos) and kvadrat2.used == False and gameended == False:
                kvadrat2.used = True
                if turn == "cross":
                    crosspos.append([320,30])
                    kvadrat2.tip = 1
                    turn = "circle"
                elif turn == "circle":
                    circlepos.append([320,30])
                    kvadrat2.tip = 0
                    turn = "cross"
            elif kvadrat3.rect.collidepoint(mousepos) and kvadrat3.used == False and gameended == False:
                kvadrat3.used = True
                if turn == "cross":
                    crosspos.append([590,30])
                    kvadrat3.tip = 1
                    turn = "circle"
                elif turn == "circle":
                    circlepos.append([590,30])
                    kvadrat3.tip = 0
                    turn = "cross"
            elif kvadrat4.rect.collidepoint(mousepos) and kvadrat4.used == False and gameended == False:
                kvadrat4.used = True
                if turn == "cross":
                    crosspos.append([50,230])
                    kvadrat4.tip = 1
                    turn = "circle"
                elif turn == "circle":
                    circlepos.append([50,230])
                    kvadrat4.tip = 0
                    turn = "cross"
            elif kvadrat5.rect.collidepoint(mousepos) and kvadrat5.used == False and gameended == False:
                kvadrat5.used = True
                if turn == "cross":
                    crosspos.append([320,230])
                    kvadrat5.tip = 1
                    turn = "circle"
                elif turn == "circle":
                    circlepos.append([320,230])
                    kvadrat5.tip = 0
                    turn = "cross"
            elif kvadrat6.rect.collidepoint(mousepos) and kvadrat6.used == False and gameended == False:
                kvadrat6.used = True
                if turn == "cross":
                    crosspos.append([590,230])
                    kvadrat6.tip = 1
                    turn = "circle"
                elif turn == "circle":
                    circlepos.append([590,230])
                    kvadrat6.tip = 0
                    turn = "cross"
            elif kvadrat7.rect.collidepoint(mousepos) and kvadrat7.used == False and gameended == False:
                kvadrat7.used = True
                if turn == "cross":
                    crosspos.append([50,430])
                    kvadrat7.tip = 1
                    turn = "circle"
                elif turn == "circle":
                    circlepos.append([50,430])
                    kvadrat7.tip = 0
                    turn = "cross"
            elif kvadrat8.rect.collidepoint(mousepos) and kvadrat8.used == False and gameended == False:
                kvadrat8.used = True
                if turn == "cross":
                    crosspos.append([320,430])
                    kvadrat8.tip = 1
                    turn = "circle"
                elif turn == "circle":
                    circlepos.append([320,430])
                    kvadrat8.tip = 0
                    turn = "cross"
            elif kvadrat9.rect.collidepoint(mousepos) and kvadrat9.used == False and gameended == False:
                kvadrat9.used = True
                if turn == "cross":
                    crosspos.append([590,430])
                    kvadrat9.tip = 1
                    turn = "circle"
                elif turn == "circle":
                    circlepos.append([590,430])
                    kvadrat9.tip = 0
                    turn = "cross"
    
    #timer for gameend so the last choice is shown. Without this the game will end without showing the last choice
    if timerstart == True:
        timer += 1
    if timer == 60:
        timerstart = False
        timer = 0
        gameended = True

    #Horizontal X wins 
    if kvadrat1.tip == 1 and kvadrat2.tip == 1 and kvadrat3.tip == 1:
        winner = "X"
        timerstart = True
    elif kvadrat4.tip == 1 and kvadrat5.tip == 1 and kvadrat6.tip == 1:
        winner = "X"
        timerstart = True
    elif kvadrat7.tip == 1 and kvadrat8.tip == 1 and kvadrat9.tip == 1:
        winner = "X" 
        timerstart = True    

    #Vertical X wins
    if kvadrat1.tip == 1 and kvadrat4.tip == 1 and kvadrat7.tip == 1:
        winner = "X"
        timerstart = True
    elif kvadrat2.tip == 1  and kvadrat5.tip == 1 and kvadrat8.tip == 1:
        winner = "X"
        timerstart = True
    elif kvadrat3.tip == 1 and kvadrat6.tip == 1 and kvadrat9.tip == 1:
        winner = "X"
        timerstart = True

    #Diagonal X wins
    if kvadrat1.tip == 1 and kvadrat5.tip == 1 and kvadrat9.tip == 1:
        winner = "X"
        timerstart = True
    elif kvadrat3.tip == 1 and kvadrat5.tip == 1 and kvadrat7.tip == 1:
        winner = "X"
        timerstart = True




    #Horizontal O wins 
    if kvadrat1.tip == 0 and kvadrat2.tip == 0 and kvadrat3.tip == 0:
        winner = "O"
        timerstart = True
    elif kvadrat4.tip == 0 and kvadrat5.tip == 0 and kvadrat6.tip == 0:
        winner = "O"
        timerstart = True
    elif kvadrat7.tip == 0 and kvadrat8.tip == 0 and kvadrat9.tip == 0:
        winner = "O"
        timerstart = True

    #Vertical O wins
    if kvadrat1.tip == 0 and kvadrat4.tip == 0 and kvadrat7.tip == 0:
        winner = "O"
        timerstart = True
    elif kvadrat2.tip == 0  and kvadrat5.tip == 0 and kvadrat8.tip == 0:
        winner = "O"
        timerstart = True
    elif kvadrat3.tip == 0 and kvadrat6.tip == 0 and kvadrat9.tip == 0:
        winner = "O"
        timerstart = True

    #Diagonal O wins
    if kvadrat1.tip == 0 and kvadrat5.tip == 0 and kvadrat9.tip == 0:
        winner = "O"
        timerstart = True
    elif kvadrat3.tip == 0 and kvadrat5.tip == 0 and kvadrat7.tip == 0:
        winner = "O"
        timerstart = True

    screen.blit(background,background_rect)    
    if gameended == False:
        screen.blit(kvadrat1.img,kvadrat1.rect)
        screen.blit(kvadrat2.img,kvadrat2.rect)
        screen.blit(kvadrat3.img,kvadrat3.rect)
        screen.blit(kvadrat4.img,kvadrat4.rect)
        screen.blit(kvadrat5.img,kvadrat5.rect)
        screen.blit(kvadrat6.img,kvadrat6.rect)
        screen.blit(kvadrat7.img,kvadrat7.rect)
        screen.blit(kvadrat8.img,kvadrat8.rect)
        screen.blit(kvadrat9.img,kvadrat9.rect)
    if gameended == False:
        for p in crosspos:
            cross_rect.topleft = p
            screen.blit(crossimg,cross_rect)
        for m in circlepos:
            circle_rect.topleft = m
            screen.blit(circleimg,circle_rect) 
    if gameended == True:
        draw_text("Играта свърши " + winner + " е победител",text_font,(0,0,0),100,250)
        draw_text("Натисни R за да рестартираш",text_font,(18,18,243),100,285)    
    pygame.display.flip()
    clock.tick(60)

