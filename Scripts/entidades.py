import pygame

class PhysicsEntity:
    def __init__(self, jogo, e_tipo, pos, tam):
        self.jogo = jogo
        self.tipo = e_tipo
        self.pos = list(pos)
        self.tam = tam
        self.velocidade = [0, 0]
        self.colisoes = {'cima': False, 'baixo': False, 'esquerda': False, 'direita': False}
        self.action = ''
        self.animationOffset = (-17, -14)
        self.flip = False
        self.set_action('idle')

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.tam[0], self.tam[1])

    def set_action(self, action):
        if action != self.action:
            self.action = action
            self.animation = self.jogo.assets[self.tipo + '/' + self.action].copy()

    def update(self, tilemap, movement=(0, 0)):
        self.colisoes = {'cima': False, 'baixo': False, 'esquerda': False, 'direita': False}
        frame_movement = (movement[0] + self.velocidade[0], movement[1] + self.velocidade[1])

        self.pos[0] += frame_movement[0]
        entidade_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entidade_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entidade_rect.right = rect.left
                    self.colisoes['direita'] = True
                if frame_movement[0] < 0:
                    entidade_rect.left = rect.right
                    self.colisoes['esquerda'] = True
                self.pos[0] = entidade_rect.x

        self.pos[1] += frame_movement[1]
        entidade_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entidade_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entidade_rect.bottom = rect.top
                    self.colisoes['baixo'] = True
                if frame_movement[1] < 0:
                    entidade_rect.top = rect.bottom
                    self.colisoes['cima'] = True 
                self.pos[1] = entidade_rect.y

        if movement[0] > 0:
            self.flip = False
        if movement[0] < 0:
            self.flip = True 

        self.velocidade[1] = min(5, (self.velocidade[1] + 0.1))
        if self.colisoes['baixo'] or self.colisoes['cima']:
            self.velocidade[1] = 0
        self.animation.update()
            

    def renderiza(self, surf):
        surf.blit(pygame.transform.flip(self.animation.img(), self.flip, False), (self.pos[0] + self.animationOffset[0], self.pos[1] + self.animationOffset[1]) )

class Player(PhysicsEntity):
    def __init__(self, jogo, pos, size):
        super().__init__(jogo, 'player', pos, size)
        self.airtime = 0

    def update(self, tilemap, movement=(0, 0)):
        super().update(tilemap, movement=movement)

        self.airtime += 1
        if self.colisoes['baixo']:
            self.airtime = 0
        if self.airtime > 4:
            self.set_action('jump')
        elif movement[0] != 0:
            self.set_action('run')
        else:
            self.set_action('idle')

class Node:
    def init(self, key):
        self.left = None
        self.right = None
        self.value = key

    fisrtnode = Node("Olá")
    secondnode = Node("Meu nome é Orimaj")
    fisrtnode.left = secondnode
    thirdnode = Node("Tchau")
    fisrtnode.right = thirdnode
    fourthnode = Node("Nada demais...")
    fifthnode = Node("Infelizmente sim, os criadores superestimaram a dificuldade do projeto...")
    secondnode.left = fourthnode
    secondnode.right = fifthnode