#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
import  pygame
import time
from random import*
from serial import *
from threading import Thread 
import threading 
import time
global b 
global time_img 
time_img=0
b=-1


global dictio
dictio={}
dictio={0:'flame_purplebackgraound-0.png'}
dictio[1]='flame_purplebackgraound-1.png'
dictio[2]='flame_purplebackgraound-2.png'
dictio[3]='flame_purplebackgraound-3.png'
dictio[4]='flame_purplebackgraound-4.png'
dictio[5]='flame_purplebackgraound-5.png'
dictio[6]='flame_purplebackgraound-6.png'
dictio[7]='flame_purplebackgraound-7.png'
dictio[8]='flame_purplebackgraound-8.png'
dictio[9]='flame_purplebackgraound-9.png'
dictio[10]='flame_purplebackgraound-10.png'
dictio[11]='flame_purplebackgraound-11.png'
dictio[12]='flame_purplebackgraound-12.png'
dictio[13]='flame_purplebackgraound-13.png'
dictio[14]='flame_purplebackgraound-14.png'
dictio[15]='flame_purplebackgraound-15.png'


global dictio1
dictio1={}
dictio1={0:'flame_purplebackgraound-0 (copie).png'}
dictio1[1]='flame_purplebackgraound-1 (copie).png'
dictio1[2]='flame_purplebackgraound-2 (copie).png'
dictio1[3]='flame_purplebackgraound-3 (copie).png'
dictio1[4]='flame_purplebackgraound-4 (copie).png'
dictio1[5]='flame_purplebackgraound-5 (copie).png'
dictio1[6]='flame_purplebackgraound-6 (copie).png'
dictio1[7]='flame_purplebackgraound-7 (copie).png'
dictio1[8]='flame_purplebackgraound-8 (copie).png'
dictio1[9]='flame_purplebackgraound-9 (copie).png'
dictio1[10]='flame_purplebackgraound-10 (copie).png'
dictio1[11]='flame_purplebackgraound-11 (copie).png'
dictio1[12]='flame_purplebackgraound-12 (copie).png'
dictio1[13]='flame_purplebackgraound-13 (copie).png'
dictio1[14]='flame_purplebackgraound-14 (copie).png'
dictio1[15]='flame_purplebackgraound-15 (copie).png'






port_serie= Serial(port="/dev/ttyACM0", baudrate=9600, timeout=1, writeTimeout=1)
global Buttton
def KKKey(port_serie):
	global Buttton 
        while True :
                ligne = port_serie.readline()
                ligne=ligne[:(len(ligne)-2)]
                ligne=str(ligne)
                l=ligne.split(' ')
                print(l)
                X=l[0]
                Y=l[1]
        	if Y[-1]=="'":
            		Y=Y[:(len(Y)-1)]            
        	print(Y)
        	if int(Y) <= 2400 :
           		 Buttton=True
	   		 print(Buttton)
            
       		else :
			Buttton=False
	 		print(Buttton)

#-------------------------------------------------------------------------------------------------
#t=Thread(target=KKKey)
#t.daemon=True
#t.start()
#--------------------------------------------------------------------------------------------------
thread = threading.Thread(target=KKKey, args=(port_serie,))
thread.start()

blue = (37,37,46)
white = (255,255,255)

pygame.init()

surfaceW = 800
surfaceH = 500
ballonW = 50
ballonH = 66
nuageW = 300
nuageH = 300

img = pygame.image.load('Ballon01.png')  

surface = pygame.display.set_mode((surfaceW,surfaceH))
#pygame.display.set_caption("Le projet DEV c'est génial")
clock = pygame.time.Clock()


def score(compte) :
    police = pygame.font.Font('BradBunR.ttf', 16)
    texte = police.render("score : " + str(compte), True, white)
    surface.blit(texte, [10,0])

def nuages(x_nuage, y_nuage, espace):
    global b
    global dictio
    global time_img

    if abs(time_img-time.time())>0.05:
	b=b+1
        time_img=time.time()
    b=b%15
    img_nuage01 = pygame.image.load(dictio1[b])
    img_nuage02 = pygame.image.load(dictio[b])
    surface.blit(img_nuage01, (x_nuage, y_nuage))
    surface.blit(img_nuage02,(x_nuage,y_nuage+ nuageH +espace))




def rejoueOuQuitte():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP:
            continue
        return event.key

    return  None

def creaTexteObjs (texte, font):
    texteSurface = font.render(texte,True,white)
    return texteSurface, texteSurface.get_rect()


def msgSurface (texte):
    GOTexte = pygame.font.Font('BradBunR.ttf', 150)
    petitTexte = pygame.font.Font('BradBunR.ttf',20)

    titreTexteSurf, titreTexteRect = creaTexteObjs(texte, GOTexte)
    titreTexteRect.center = surfaceW/2,((surfaceH/2)-50)
    surface.blit(titreTexteSurf, titreTexteRect)

    petitTexteSurf, petitTexteRect = creaTexteObjs\
        ("appuyer sur une touche pour continuer", petitTexte )
    petitTexteRect.center = surfaceW/2, ((surfaceH/2) +50)
    surface.blit(petitTexteSurf, petitTexteRect)

    pygame.display.update()
    time.sleep(2)

    while rejoueOuQuitte() == None :
        clock.tick()

    main()

def gameOver():
    msgSurface("Boom!")

def ballon(x,y, image):
    surface.blit(image, (x,y))

def main():
    global Buttton
    global time_img
    global b
    print("YYYYYYYYYYYYYY",Buttton)
    a=0
    x=150
    y=200
    y_move=0

    x_nuage = surfaceW/4
    y_nuage = randint(-200,100)
    espace = ballonH*3
    nuage_vitesse = 1

    score_actuel = 0

    game_over = False

    while not game_over:
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #game_over= True
        if Buttton :#up
            y_move = -0.4
            print(Buttton)

        else :#down
            y_move = 0.4
            print(Buttton)

        y += y_move

        surface.fill(blue)
        ballon(x,y,img)

        nuages(x_nuage,y_nuage, espace)

        score(score_actuel)

        x_nuage -=nuage_vitesse


        if y>surfaceH -40 or y <-10:
            gameOver()

        if x_nuage < (-0.1*nuageW):
            x_nuage = surfaceW
            y_nuage = randint(-200,100)

            if 3 <= score_actuel < 5:
                nuage_vitesse = 1.2
                espace = ballonH*2.8
            if 5 <= score_actuel < 7 :
                nuage_vitesse = 1.5
                espace = ballonH*2.7
            if 7 <= score_actuel < 10 :
                nuage_vitesse = 1.8
                espace = ballonH*2.5
            if 10 <= score_actuel <22:
                nuage_vitesse = 2.2
                espace = ballonH*2.2
            if 22 <= score_actuel:
                nuage_vitesse = 2.5
                espace = ballonH*2



        if x +ballonW > x_nuage + 40 :
            if y < y_nuage + nuageH  -50:
                if x - ballonW < x_nuage +nuageW -20 :
                    #print("touche haut!!!")
                    gameOver()
        
        if x +ballonW >x_nuage + 40 :
            if y +ballonH > y_nuage + nuageH + espace +50 :
                if x -ballonW < x_nuage+ nuageW - 20:
                    #print("touche bas!!!")
                    gameOver()

        if x_nuage < x <x_nuage+nuageW :
	    a=a+1
	    if a > nuageW:
		score_actuel +=1
		a=0


        pygame.display.update()



main()
pygame.quit()
quit()
