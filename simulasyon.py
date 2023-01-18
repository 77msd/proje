import math
import pygame

from pygame.locals import*

from pygame import mixer 



import pygame, sys
from button import Button
from pygame import mixer 
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


def make_window(width: int, height: int, caption: str) -> pygame.Surface:
    """Bir pygame penceresi oluşturun ve döndürün."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen

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

def play():
          
    while True:
        e: pygame.event.Event 
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        main()
        
        
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

def yazi_yaz(yazi , font , renk , surface ,x , y ):
    textobj= font.render(yazi, 1 ,renk  )
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def main() -> None:
    """GÖRÜNTÜYÜ HAREKET ETTİRMEK İÇİN."""
    # DEĞİŞKENLERE AÇIKLAMA EKLEME
    SCREEN_HEIGHT: int = 720
    SCREEN_WIDTH: int = 1280
    screen: pygame.Surface
    background: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    projectile: pygame.Surface
    flag: pygame.Surface
    start_x: float = -8
    start_y: float = -100
    x: float = start_x
    y: float = start_y
    time: float = 0
    shoot: bool = False
    angle: float = 45 
    speed: float = 180
    gravity:float= 98.1

    # Gerekenleri Kur.
    screen = make_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Angle: 45 Speed: 180 ")
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background= pygame.image.load("arka_plan.png")
    projectile = pygame.image.load("large_ball.png")
    #HAVAN EKLEYELİM #
    havanImg = pygame.image.load("top9.png")
    havanX = -38
    havanY = 673
    
    havanX_change = 0
    havanY_change = 0

    #SİMULASYONA İCON EKLEME 
    icon = pygame.image.load("top9.png")
    pygame.display.set_icon(icon)


    projectile = projectile.convert_alpha()
    flag = pygame.image.load("ottoflg.png")
    flag = flag.convert_alpha()
    start_y = screen.get_height() - projectile.get_height()
    y = start_y
    clock: pygame.time.Clock = pygame.time.Clock()
    

    
    while not user_quit:
        # Saniyede 30 kez döngü
         
        clock.tick(30)

        for e in pygame.event.get():
            # Çıkma seçimini işleyin.
            if e.type == pygame.QUIT:
                user_quit = True
             
            # Açıyı ayarlamak ve çekim yapmak için işlem tuşları.
            elif e.type == pygame.KEYDOWN and not shoot:
                if e.__dict__["key"] == pygame.K_UP and angle < 90:
                    angle += 5
                elif e.__dict__["key"] == pygame.K_DOWN and angle >= 10:
                    angle -= 5
                elif e.__dict__["key"] == pygame.K_RIGHT:
                    speed += 10
                elif e.__dict__["key"] == pygame.K_LEFT and speed >= 10:
                    speed -= 10
                # YERÇEKİMİNİ ARTIRIP AZALTMAK İÇİN

                elif e.__dict__["key"] == pygame.K_u:
                    gravity += 10
                elif e.__dict__["key"] == pygame.K_j:
                    gravity -= 10

                # HAVANI YATAY VE DÜŞEY YÖNDE HAREKET ETTİRMEK #

                elif e.__dict__["key"] == pygame.K_w:
                    havanY += -10
                    start_y += -10  
                    y += -10 
                elif e.__dict__["key"] == pygame.K_s:
                    havanY += 10
                    start_y += 10
                    y += 10
                elif e.__dict__["key"] == pygame.K_d:
                    havanX += 10
                    start_x += 10
                    x  += 10
                elif e.__dict__["key"] == pygame.K_a:
                    havanX += -10
                    start_x += -10
                    x += -10
                
                elif e.__dict__["key"] == pygame.K_ESCAPE:
                    

                    main_menu()

                elif e.__dict__["key"] == pygame.K_SPACE:
                    shoot = True
                    

                    #Karıştırıcıyı başlat
                    mixer.init()

                    #ses dosyasını yükle
                    mixer.music.load('cannon_shot.mp3')

                    #Tercih edilen ses seviyesini ayarla
                    mixer.music.set_volume(5)

                    #Müziği çal
                    mixer.music.play()

                    # Mermiyi havada hareket ettirmek için
        if shoot:
            # Artış süresi
            time += 1/15
           
            # merminin x ekseninde aldığı yolu hesaplamak için
            print(round(math.cos(math.radians(angle)) * speed * time), "metre x ekseninde yol aldı.")
            
            

            #Konumu hesaplamak için
            x = (start_x
                        + math.cos(math.radians(angle)) * speed * time)
            y = (start_y
                        - (math.sin(math.radians(angle)) * speed * time)
                        + .5 * gravity * time**2)
                # BURADA YER ÇEKİMİNİ 98.1 ALIYORUZ  VE 1/2 X G X ZAMANIN KARESİ FORMÜLÜNDEN YARARLANIYORUZ. #
                        
# Yere çarpıp çarpmadığını kontrol edelim
            if y + projectile.get_height() >= screen.get_height():
                time = 0
                shoot = False
# Düştüğü yere bayrak koyalım
                background.blit(flag, (x, screen.get_height() - flag.get_height()))
# Bayrak koyduktan sonra başlangıca dönsün

                #Karıştırıcıyı başlat
                mixer.init()

                #ses dosyasını yükle
                mixer.music.load('landing_effect.mp3')

                #Tercih edilen ses seviyesini ayarla
                mixer.music.set_volume(5)

                #Müziği çal
                mixer.music.play()

                x = start_x
                y = start_y

 # Ekrana çizin ve gösterin.
        pygame.display.set_caption("Angle: " + str(angle) + " Speed: " + str(speed) +     "  Gravity:  " + str(gravity)   )
        screen.blit(background, (0, 0))
        screen.blit(projectile, (x, y))
        screen.blit(havanImg ,(havanX ,havanY))
        
        pygame.display.flip()

    pygame.quit()

main_menu()