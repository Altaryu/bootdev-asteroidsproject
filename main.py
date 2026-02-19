import pygame
import sys
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    asteroids=pygame.sprite.Group()
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    Player.containers=(updatable, drawable)
    Asteroid.containers=(asteroids, updatable, drawable)
    AsteroidField.containers=(updatable)
    AsteroidField()
    player=Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
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
            #clock.tick(60)
            #print(dt)
            
        screen.fill("black")
        #player.update(dt)
        updatable.update(dt)

        for ast in asteroids:
            result=ast.collides_with(player)
            if result == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        #player.draw(screen)
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()

        dt=clock.tick(60)/1000
            

if __name__ == "__main__":
    main()
