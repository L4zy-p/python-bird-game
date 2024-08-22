import pygame.sprite

import asset
import configs
from layer import Layer


class Background(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        self._layer = Layer.BACKGROUND
        # ใช้ function เรียกรูปจาก asset.py
        self.image = asset.get_sprite("background")
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * index, 0))

        super().__init__(*groups)

    def update(self):
        # ทำให้ background เลื่อนไปทางขวา
        self.rect.x -= 2

        # เมื่อ backgrond เป็น 0 แล้วให้สลับ background
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH
