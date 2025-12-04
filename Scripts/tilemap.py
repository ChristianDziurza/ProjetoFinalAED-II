class TileMap:
    def __init__(self, jogo, tile_size=16):
        self.jogo = jogo
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tilemap[str(3+i) + ';10'] = {'tipo': 'grama', 'variante': 1, 'pos': (3+i, 10)}
            self.tilemap['10:' + str(5+i)] = {'tipo': 'pedra', 'variante': 1, 'pos': (10, 5+i)}

    def renderiza(self, surf):
        for tile in self.offgrid_tiles:
            surf.blit(self.jogo.assets[tile['tipo']][tile['variante']], tile['pos'])

        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(self.jogo.assets[tile['tipo']][tile['variante']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))
