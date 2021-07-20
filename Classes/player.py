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

from .functions import load_image
from typing import Tuple

import pygame


class Player:
    def __init__(self,
                 WIN: pygame.surface.Surface, x: int, y: int, player_num: int=1, size: Tuple[int, int]=(27, 36)):
        self.WIN: pygame.surface.Surface = WIN
        self.x: int = x
        self.y: int = y
        self.time: int = 0
        self.index: int = 0
        self.animation_time: int = 1
        self.player_num: int = player_num
        self.jump_count: int = 10
        self.is_jumping: bool = False
        self.size: Tuple[int, int] = size
        self.walk_animation = []
        self._load_images()
        self.current_rect: pygame.rect.Rect = None
        self.current_image: pygame.surface.Surface = None
        self.jumping_image: pygame.surface.Surface = pygame.transform.scale(load_image(f"""assets/images/Player/p{self.player_num}_jump.png"""), self.size)
        self.animate()

    def _load_images(self) -> None:
        self.walk_animation = []
        for i in range(11):
            self.walk_animation.append(
                pygame.transform.scale(
                    load_image(
                        f"""assets/images/Player/p{self.player_num}_walk/PNG/p{self.player_num}_walk{i + 1 if len(str(i + 1)) == 2 else "0" + str(i + 1)}.png"""
                    ), self.size
                )
            )

    def animate(self) -> None:
        # FPS is going to be 60 anything else will break this
        self.time += 1

        if   self.time == self.animation_time * 1:  self.index = 0
        elif self.time == self.animation_time * 2:  self.index = 1
        elif self.time == self.animation_time * 3:  self.index = 2
        elif self.time == self.animation_time * 4:  self.index = 3
        elif self.time == self.animation_time * 5:  self.index = 4
        elif self.time == self.animation_time * 6:  self.index = 5
        elif self.time == self.animation_time * 7:  self.index = 6
        elif self.time == self.animation_time * 8:  self.index = 7
        elif self.time == self.animation_time * 9:  self.index = 8
        elif self.time == self.animation_time * 10: self.index = 9
        elif self.time == self.animation_time * 11: self.index = 10
        elif self.time == self.animation_time * 12: self.index = 11; self.time = 0; self.index = 0

        if not self.is_jumping:
            self.current_image = self.walk_animation[self.index]
        elif self.is_jumping:
            self.current_image = self.jumping_image

    def get_rect(self) -> pygame.Rect:
        """
        it returns the rect of the current image
        :return: pygame.rect.Rect
        """
        return self.current_image.get_rect()

    def get_width(self) -> float:
        """
        it returns the width of the current image
        :return: int
        """
        return self.get_rect().width

    def get_height(self) -> float:
        """
        it returns the height of the current image
        :return: int
        """
        return self.get_rect().height

    def draw(self) -> None:
        """
        it draws the player in the screen
        :return:
        """
        try:
            self.WIN.blit(
                self.current_image, (
                    self.x, self.y
                )
            )
        except Exception:
            print(f"""the player is not animated and it doesnt have any images to blit | drawing the default image""")
            self.WIN.blit(
                pygame.transform.scale(
                    load_image(
                        f"""assets/images/Player/p{self.player_num}_stand.png"""
                    ), (
                        9 * 3, 12 * 3
                    )
                ), (
                    self.x, self.y
                )
            )

    def move(self) -> None:
        """
        it handles the players movements
        :return: None
        """
        if self.is_jumping:
            if self.jump_count >= -10:
                self.y -= (self.jump_count * abs(self.jump_count)) / 2
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.is_jumping = False

    def event_handler(self, event: pygame.event.Event):
        """
        it handles the events that this class can accept
        :param event: pygame.event.Event
        :return: None
        """
        if event.type == pygame.KEYDOWN:
            # check for jumping
            if event.key == pygame.K_SPACE and not self.is_jumping:
                self.is_jumping = True

    def collision(self, obj):
        """
        it can collide with any object that has: a .get_rect() method with .x and .x attributes
        :param obj: Any
        :return: bool
        """
        if pygame.Rect(
                self.x, self.y, self.get_width(), self.get_height()
        ).colliderect(
                pygame.Rect(
                    obj.x, obj.y, obj.get_width(), obj.get_height()
                )
        ):
            return True
        return False
