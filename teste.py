import sys

import pygame

from Scripts.utils import load_image, load_images, Animation
from Scripts.entidades import PhysicsEntity, Player
from Scripts.tilemap import TileMap

class Jogo:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Jogo')
        self.tela = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320,240))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]
        self.assets = {
            'grama': load_images('tiles/gramas'),
            'pedra': load_images('tiles/pedra'),
            'player' : load_image('Carinha.png'),
            'player/idle' : Animation(load_images('anim/idle'), imgDur=100),
            'player/run' : Animation(load_images('anim/run'), imgDur=4),
            'player/jump' : Animation(load_images('anim/run'), imgDur=2)


        }

        self.player = Player(self, (50,150), (10, 18))

        self.tilemap = TileMap(self, tile_size=16)

    def run(self):
        while True:
            self.display.fill((14, 219, 249))

            self.tilemap.renderiza(self.display)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.renderiza((self.display))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocidade[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            self.tela.blit(pygame.transform.scale(self.display, self.tela.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Jogo().run()