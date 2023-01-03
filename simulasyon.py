import math
import pygame
pygame.init()

def make_window(width: int, height: int, caption: str) -> pygame.Surface:
    """Bir pygame penceresi oluşturun ve döndürün."""
    screen: pygame.Surface
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen


def main() -> None:
    """GÖRÜNTÜYÜ HAREKET ETTİRMEK İÇİN."""
    # DEĞİŞKENLERE AÇIKLAMA EKLEME
    SCREEN_HEIGHT: int = 480
    SCREEN_WIDTH: int = 640
    screen: pygame.Surface
    background: pygame.Surface
    user_quit: bool = False
    e: pygame.event.Event
    projectile: pygame.Surface
    flag: pygame.Surface
    start_x: float = 0
    start_y: float = -100
    x: float = start_x
    y: float = start_y
    time: float = 0
    shoot: bool = False
    angle: float = 0 
    speed: float = 100


    # Gerekenleri Kur.
    screen = make_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Angle: 0 Speed: 200")
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill((222, 237, 244))
    projectile = pygame.image.load("large_ball.png")
    #HAVAN EKLEYELİM #
    havanImg = pygame.image.load("top9.png")
    havanX = -30
    havanY = 550
    
    havanX_change = 0
    havanY_change = 0

    projectile = projectile.convert_alpha()
    flag = pygame.image.load("flag.png")
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
                    angle += 10
                elif e.__dict__["key"] == pygame.K_DOWN and angle >= 10:
                    angle -= 10
                elif e.__dict__["key"] == pygame.K_RIGHT:
                    speed += 10
                elif e.__dict__["key"] == pygame.K_LEFT and speed >= 10:
                    speed -= 10
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



                elif e.__dict__["key"] == pygame.K_SPACE:
                    shoot = True

                    # Mermiyi havada hareket ettirmek için
        if shoot:
            # Artış süresi
            time += 1/15
            #Konumu hesaplamak için
            x = (start_x
                        + math.cos(math.radians(angle)) * speed * time)
            y = (start_y
                        - (math.sin(math.radians(angle)) * speed * time)
                        + .5 * 72 * time**2)
                        
# Yere çarpıp çarpmadığını kontrol edelim
            if y + projectile.get_height() >= screen.get_height():
                time = 0
                shoot = False
# Düştüğü yere bayrak koyalım
                background.blit(flag, (x, screen.get_height() - flag.get_height()))
# Bayrak koyduktan sonra başlangıca dönsün

                x = start_x
                y = start_y

 # Ekrana çizin ve gösterin.
        pygame.display.set_caption("Angle: " + str(angle) + " Speed: " + str(speed))
        screen.blit(background, (0, 0))
        screen.blit(projectile, (x, y))
        screen.blit(havanImg ,(havanX ,havanY))
        
        pygame.display.flip()
         
    pygame.quit()

main()