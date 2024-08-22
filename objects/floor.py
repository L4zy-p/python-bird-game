import pygame.sprite
import asset
import configs
from layer import Layer

class Floor(pygame.sprite.Sprite):
    def __init__(self,index,*groups):
        self._layer = Layer.FLOOR
        # ดึงรูป floor มาจาก asset.py
        self.image = asset.get_sprite("floor")
        self.rect = self.image.get_rect(bottomleft=(configs.SCREEN_WIDTH * index, configs.SCREEN_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)

        super().__init__(*groups)


    def update(self):
        # ให้ floor เลื่อนไปด้านซ้าย
        self.rect.x -= 2

        # เมื่อ floor เลื่อนจนเหลือ 0 ให้สลับรูป 
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH
            