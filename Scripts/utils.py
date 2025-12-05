import os
import pygame

BASE_IMG_PATH = 'Sprites'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + '/' + path).convert()
    img.set_colorkey(('black'))
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + '/' + path)):
        images.append(load_image(path + '/' + img_name))
    return images

import pygame

class Animation:
    def __init__(self, imagens, imgDur=5, loop = True):
        self.imagens = imagens
        self.imgDur = imgDur
        self.loop = loop
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.imagens, self.imgDur, self.loop)

    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.imgDur * len(self.imagens))
        else:
            self.frame = min(self.frame + 1, self.imgDur * len(self.imagens) - 1)
            if self.frame >= self.imgDur * len(self.imagens)-1:
                self.done = True

    def img(self):
        return self.imagens[int(self.frame/self.imgDur)]