import pygame
from gameclass import *
import sys

win = pygame.display.set_mode((1000,1000))

#username vars

inputFont = pygame.font.Font(None,64)
inputNameText = 'Enter Name'
inputName = inputFont.render(inputNameText,True,(255,255,255))
inputNameRect = inputName.get_rect()
inputNameRect.center = (pygame.display.get_window_size()[0]/2,pygame.display.get_window_size()[1]/2)
userName = ''
userNameFlag = True

#get username 

while userNameFlag:
    
    for eve in pygame.event.get():
            
        if eve.type==pygame.QUIT:
            pygame.quit()

        if eve.type == pygame.KEYDOWN:
            if eve.key == pygame.K_RETURN:
                print('hljals')
                userNameFlag = False
            userName += eve.unicode


    inputNameRect = inputName.get_rect()
    inputNameRect.center = (pygame.display.get_window_size()[0]/2,pygame.display.get_window_size()[1]/2)

    if len(userName):

        inputName = inputFont.render(userName,True,(255,255,255))

    win.fill((0,0,0))

    win.blit(inputName,inputNameRect)

    pygame.display.update()

network = clientNetwork('localhost',9090)      
p1 = network.connect(userName)

clock = pygame.time.Clock()

enemyLis = []

run = True

while run:

    for eve in pygame.event.get():
            
        if eve.type==pygame.QUIT:
            pygame.quit()


    win.fill((0,0,0))

    if p1.collisionSelf():
        break

    p1.update(win)
    displayName(p1,win)

    enemyLis = network.exchange(p1)

    
    for ene in enemyLis:
        if ene:
            if p1.collisionEnemy(ene):
                run = False
                
            ene.drawPlayer(win)
            displayName(ene,win)

    pygame.display.update()

    clock.tick(60)


network.close()    
pygame.quit()

    

