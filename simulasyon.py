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