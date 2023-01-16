import math
import pygame

from pygame.locals import*

from pygame import mixer 



import pygame, sys
from button import Button

pygame.init()

check_errors = pygame.init()
if check_errors[1] == check_errors:
    print("An error has occured!")
else:
    print("Game has initilized successfully!")

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("şablonlar/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("şablonlar/font.ttf", size)

def play():
          
    while True:
        e: pygame.event.Event 
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        import simulasyon
        open(simulasyon)
        pygame.init()
        
        
        #PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        #PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        #SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        

        #PLAY_BACK = K_ESCAPE
        #Button(image=None, pos=(640, 460), 
                            # text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        
        #PLAY_BACK.changeColor(K_ESCAPE)
        #PLAY_BACK.update(SCREEN)

        # for event in pygame.event.get():
            
            
        #     if event.type == pygame.QUIT:
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == K_ESCAPE:
        #                 main_menu()


        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                False
            elif e.type == pygame.KEYDOWN:
                if e.__dict__["key"] == pygame.K_ESCAPE:
                    main_menu()

                
                pygame.quit()
                sys.exit()
        
                    
                    #if PLAY_BACK.checkForInput(K_ESCAPE):
                         

        pygame.display.update()
    
def guide():
    while True:
        GUIDE_MOUSE_POS = pygame.mouse.get_pos()
        kılavuz =pygame.image.load("kılavuz.png")
        #SCREEN.fill("white")

        # GUIDE_TEXT = get_font(45).render("This is the GUIDE screen.", True, "Black")
        # GUIDE_RECT = GUIDE_TEXT.get_rect(center=(640, 460))
        SCREEN.blit(kılavuz,(0,0))

        GUIDE_BACK = Button(image=None, pos=(640, 680), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        GUIDE_BACK.changeColor(GUIDE_MOUSE_POS)
        GUIDE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GUIDE_BACK.checkForInput(GUIDE_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("şablonlar/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        GUIDE_BUTTON = Button(image=pygame.image.load("şablonlar/Guide Rect.png"), pos=(640, 400), 
                            text_input="GUIDE", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("şablonlar/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, GUIDE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if GUIDE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    guide()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
