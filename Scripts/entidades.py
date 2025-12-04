import pygame

class PhysicsEntity:
    def __init__(self, jogo, e_tipo, pos, tam):
        self.jogo = jogo
        self.tipo = e_tipo
        self.pos = list(pos)
        self.tam = tam
        self.velocidade = [0, 0]

    def update(self, movement=(0, 0)):
        frame_movement = (movement[0] + self.velocidade[0], movement[1] + self.velocidade[1])

        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]

    def renderiza(self, surf):
        surf.blit(self.jogo.assets['player'], self.pos)