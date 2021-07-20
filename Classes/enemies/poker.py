"""
MIT License

Copyright (c) 2021 Emc235

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from typing import Tuple

import pygame
import random


class Poker:
    def __init__(self, WIN: pygame.surface.Surface, y: int, vel: int=2):
        load_img = pygame.image.load
        self.WIN: pygame.surface.Surface = WIN
        self.x: int = self.WIN.get_width() + 50
        self.y: int = y - 60
        self.vel: int = vel
        self.parts_num: int = random.randint(1, 3)
        self.block_size: Tuple[int, int] = (20, 20)
        self.mad: pygame.surface.Surface = pygame.transform.scale(load_img("assets/images/Enemies/pokerMad.png"), (20, 60))
        self.sad: pygame.surface.Surface = pygame.transform.scale(load_img("assets/images/Enemies/pokerSad.png"), (20, 60))
        self.current_image: pygame.surface.Surface = self.mad

    def get_rect(self) -> pygame.Rect:
        """
        it returns the rect of the current image
        :return: pygame.rect.Rect
        """
        return self.current_image.get_rect()

    def get_width(self) -> int:
        """
        it returns the width of the current image
        :return: int
        """
        return self.get_rect().width

    def get_height(self) -> int:
        """
        it returns the height of the current image
        :return: int
        """
        return self.get_rect().height

    def move(self) -> bool:
        """
        it moves the enemy
        :return: bool
        """
        self.x -= self.vel
        if self.x <= -100:
            return True
        return False

    def draw(self) -> None:
        """
        it draws the enemy on the screen
        :return: None
        """
        self.WIN.blit(self.current_image, (self.x, self.y))
