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


class Blocker:
    def __init__(self, WIN: pygame.surface.Surface, y: int, vel: int=2):
        load_img = pygame.image.load
        self.WIN: pygame.surface.Surface = WIN
        self.x: int = self.WIN.get_width() + 50
        self._y: int = y
        self.vel: int = vel
        self.parts_num: int = random.randint(1, 3)
        self.block_size: Tuple[int, int] = (20, 20)
        self.y: int = self._y - self.block_size[1] * self.parts_num
        self.body = pygame.transform.scale(load_img("assets/images/Enemies/blockerBody.png"), self.block_size)
        self.mad  = pygame.transform.scale(load_img("assets/images/Enemies/blockerMad.png"),  self.block_size)
        self.sad  = pygame.transform.scale(load_img("assets/images/Enemies/blockerSad.png"),  self.block_size)
        self.parts: list = self._build()
        self.x: int = self.parts[0][1][0]

    def _build(self) -> list:
        """
        it builds the enemy
        :return: list
        """
        parts = []
        for i in range(self.parts_num):
            parts.append([])
            if i != self.parts_num - 1:
                parts[i].append(self.body)
                parts[i].append([self.x, self._y - (self.block_size[0] * (i + 1))])
            else:
                parts[i].append(self.mad)
                parts[i].append([self.x, self._y - (self.block_size[0] * (i + 1))])

        return parts

    def get_rect(self) -> pygame.Rect:
        """
        it returns the rect of the current image
        :return: pygame.rect.Rect
        """
        return pygame.Rect(self.x, self._y - self.block_size[1] * self.parts_num, self.block_size[0], self.block_size[1] * self.parts_num)

    def get_width(self) -> int:
        """
        it returns the width of the current image
        :return: int
        """
        return self.block_size[0]

    def get_height(self) -> int:
        """
        it returns the height of the current image
        :return: int
        """
        return self.block_size[1] * self.parts_num

    def move(self) -> bool:
        """
        it moves the enemy
        :return: bool
        """
        self.x: int = self.parts[0][1][0]
        for i in range(len(self.parts)):
            self.parts[i][1][0] -= self.vel

            if self.parts[i][1][0] <= -self.block_size[0]:
                return True
        return False

    def draw(self) -> None:
        """
        it draws the enemy on the screen
        :return: None
        """
        for sprite, cords in self.parts:
            self.WIN.blit(sprite, cords)
