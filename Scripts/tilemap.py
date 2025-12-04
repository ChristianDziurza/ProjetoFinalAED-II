import pygame

NEIGHBOR_OFFSETS = [(-1,0), (-1,-1), (0,-1), (1,0), (0,0), (-1,1), (0,1), (1,1), (2,0), (2,1), (2,2), (-2,0), (-2,1), (-2,2), (1,2), (1,-2), (2,-1), (-2,-1), (-1,2), (-1,-2), (2,-2), (-2,2)]
PHYSYCS_TILES = {'grama', 'pedra'}

class TileMap:
    def __init__(self, jogo, tile_size=16):
        self.jogo = jogo
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tilemap[str(3+i) + ';10'] = {'tipo': 'grama', 'variante': 1, 'pos': (3+i, 10)}
            self.tilemap['10;' + str(5+i)] = {'tipo': 'pedra', 'variante': 1, 'pos': (10, 5+i)}

    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles

    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['tipo'] in PHYSYCS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects

    def renderiza(self, surf):
        for tile in self.offgrid_tiles:
            surf.blit(self.jogo.assets[tile['tipo']][tile['variante']], tile['pos'])

        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(self.jogo.assets[tile['tipo']][tile['variante']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))
