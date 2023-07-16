import pygame 
from pygame import *
import math
import random
import asyncio
from Libraries.game_objects import *

#to send it write "pyinstaller --onefile --windowed main.py"

pygame.init() 

window = pygame.display.set_mode((680, 400))
pygame.display.set_caption("Photon Play")
font = pygame.font.Font('comicsans.ttf',11)


status = True
game_phase = 0 #tittle =0 #ball selection =1 #door selection =2
current_ball = 0
chosen_ball_color = (0,0,0)
current_door = 0
second_ball = current_ball
message = "Choose a photon. Press enter to select it. "
message2 = ""
message3 = ""
message4 = ""
balls = []
for i in range(0,6):
    balls.append(Ball((100*i+25, 280))) 

doors = []
for i in range(0,5):
    ball = balls[random.randrange(0,6)]
    doors.append(Door((132*i+25, 80)))
    
doors[random.randrange(0,5)].chosen = True
    
select2 = Selector(25,30, 4)

select3 = Selector(25,230,5)
    
select = Selector(25,230,5)

    
while status:
    for e in pygame.event.get():
            if e.type == pygame.QUIT:
                status = False
            if e.type == pygame.KEYDOWN:
                if game_phase == 0:
                   if e.key == pygame.K_RETURN:
                        game_phase = 7
                elif game_phase == 7:
                    if e.key == pygame.K_RETURN:
                        game_phase = 1
                elif game_phase == 1:
                    if e.key == pygame.K_RIGHT:
                        select.right(100)
                        current_ball = (current_ball+1) % 6
                                                
                    if e.key == pygame.K_RETURN:
                        game_phase = 2 
                        message = "Photon Chosen. Press your right key and select a Metal door."
                elif game_phase == 2:
                        
                    if e.key == pygame.K_RIGHT:
                        select2.right(130)
                        current_door = (current_door +1) % 5
                        
                        if balls[current_ball].color == [255,0,0]:
                            balls[current_ball].energy = 1
                        elif balls[current_ball].color == [128,0,0]:
                            balls[current_ball].energy = 2
                        elif balls[current_ball].color == [0,255,255]:
                            balls[current_ball].energy = 3
                        elif balls[current_ball].color == [224,225,255]:
                            balls[current_ball].energy = 4
                        elif balls[current_ball].color == [0,128,128]:
                            balls[current_ball].energy = 5
                                  
                    if e.key == pygame.K_RETURN:
                        game_phase = 3
                        message = "Metal Door Chosen. Press Enter to Continue"

                elif game_phase == 3:
                    if balls[current_ball].color == doors[current_door].color:
                        doors[current_door].state = 1
                        message = "Thresold Frequency Matched, press left key to increase intensity. Then press right key."
                        if e.key == pygame.K_LEFT:
                            doors[current_door].jiggle = True
                            game_phase = 4
                    else: 
                        if e.key == pygame.K_RETURN:
                            game_phase = 1
                            message = "Try Again. Select another door. Press enter to continue."
                            
                elif game_phase == 4:
                    message = "You now need to select a photon with a higher frequency than your current one. Your current frequency is: "+str(balls[current_ball].energy)+"hz"
                    if e.key == pygame.K_RIGHT:
                        select3.right(100)
                        second_ball = (second_ball +1) % 6
                        
                    if e.key == pygame.K_RETURN:
                        message3 = ""
                        if balls[second_ball].energy >= balls[current_ball].energy:
                            game_phase = 5
                            message2 = "Good job, you have correctly selected a higher frequency. Press enter"
                        else:
                            message2 = "Try again because the frequency was lower. Press left and then right to use selector again."
                    if e.key == pygame.K_LEFT:
                        message3 = "                                                                                  :)                                                                                                                               "
                elif game_phase == 5:
                    if doors[current_door].chosen == True:
                        if e.key == pygame.K_RETURN:
                            game_phase = 1
                            doors[0].state = 0
                            doors[0].chosen = False
                            doors[1].state = 0
                            doors[1].chosen = False
                            doors[2].state = 0
                            doors[2].chosen = False
                            doors[3].state = 0
                            doors[3].chosen = False
                            doors[4].state = 0
                            doors[4].chosen = False
                            doors[0].jiggle = False
                            doors[1].jiggle = False
                            doors[2].jiggle = False
                            doors[3].jiggle = False
                            doors[4].jiggle = False
                            doors[0].color = [224,255,255]
                            doors[1].color = [255,0,0]
                            doors[2].color = [128,0,0]
                            doors[3].color = [0,255,255]
                            doors[4].color = [0,128,128]
                        
                            doors[random.randrange(0,5)].chosen = True
                            message = "You played well and you can now escape. Well Done! Move arrow keys to select another photon."
                            message2 = "eScApE!!!!"
                    else:   
                        if e.key == pygame.K_RETURN:
                            game_phase = 1
                            message ="Not the right door to escape. Select another Photon." 
                            message2 = "You can do it this time!!"
                    
    if game_phase == 0:
        img = pygame.image.load("Images/newest.png").convert()
        img = pygame.transform.scale(img, (640,400))
        window.blit(img, (20,0))
    
    elif game_phase == 7:
        img = pygame.image.load("Images/introduc.png").convert()
        img = pygame.transform.scale(img, (640,400))
        window.blit(img, (20,0))
        
    elif game_phase == 1 or game_phase == 2 or game_phase == 3 or game_phase == 4 or game_phase == 5:
        window.fill((255,255,255))
        for item in doors:
            item.draw(window)
        for item in balls:
            item.draw(window)
        if game_phase == 1:
            select.draw(window)
        elif game_phase == 2:
            select2.draw(window)
        elif game_phase == 4:
            select3.draw(window)
        game_message = font.render(message,True, (0,0,0),(255,255,255))
        window.blit(game_message,(20,350,640,60))
        gamer_message = font.render(message2,True, (0,0,0), (255,255,255))
        window.blit(gamer_message,(20,370,640,60))
        games_message = font.render(message3, True, (0,0,0), (255,255,255))
        window.blit(games_message, (20,370,640,60))
        gamey_message = font.render(message4, True, (0,0,0), (255,255,255))
        window.blit(games_message, (20,370,640,60))

                        
    pygame.display.flip()