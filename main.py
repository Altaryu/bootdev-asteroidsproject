import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    clock=pygame.time.Clock()
    dt=0
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while(True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            clock.tick(60)
            dt=clock.tick(60)/1000
            #print(dt)
            
        screen.fill("black")
        pygame.display.flip()
            

if __name__ == "__main__":
    main()
