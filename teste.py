import sys

import pygame


class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Jogo')
        self.tela = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.img = pygame.image.load('/home/chrisistencial/Documentos/Faculdade/TrabalhoAEDII/Sprites/Carinha.png')
        #self.img.set_colorkey((0, 0, 0))

        self.img_pos = [160,260]
        self.movement = [False, False, False, False]

        self.area_colisao = pygame.Rect(50, 50, 300, 50)

    def run(self):
        while True:
            self.tela.fill((14, 219, 249))

            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            if img_r.colliderect(self.area_colisao):
                pygame.draw.rect(self.tela, (0, 100, 255), self.area_colisao)
            else:
                pygame.draw.rect(self.tela, (0, 50, 130), self.area_colisao)

            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.img_pos[0] += (self.movement[2] - self.movement[3]) * 5
            self.tela.blit(self.img, self.img_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[2] = True
                    if event.key == pygame.K_LEFT:
                        self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[2] = False
                    if event.key == pygame.K_LEFT:
                        self.movement[3] = False


            pygame.display.update()
            self.clock.tick(60)

Jogo().run()