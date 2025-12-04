import pygame

class PhysicsEntity:
    def __init__(self, jogo, e_tipo, pos, tam):
        self.jogo = jogo
        self.tipo = e_tipo
        self.pos = list(pos)
        self.tam = tam
        self.velocidade = [0, 0]

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.tam[0], self.tam[1])

    def update(self, tilemap, movement=(0, 0)):
        frame_movement = (movement[0] + self.velocidade[0], movement[1] + self.velocidade[1])

        self.pos[0] += frame_movement[0]
        entidade_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entidade_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entidade_rect.right = rect.left
                if frame_movement[0] < 0:
                    entidade_rect.left = rect.right
                self.pos[0] = entidade_rect.x

        self.pos[1] += frame_movement[1]
        for rect in tilemap.physics_rects_around(self.pos):
            if entidade_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entidade_rect.bottom = rect.top
                if frame_movement[1] < 0:
                    entidade_rect.top = rect.bottom
                self.pos[1] = entidade_rect.y

        self.velocidade[1] = min(5, (self.velocidade[1] + 0.1))

    def renderiza(self, surf):
        surf.blit(self.jogo.assets['player'], self.pos)