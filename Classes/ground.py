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


import pygame


class Ground:
    def __init__(self, WIN: pygame.surface.Surface, y: int, h: int, amount_of_images: int=3, vel: int=2):
        self.WIN: pygame.surface.Surface = WIN
        self.y: int = y
        self.w: int = int(self.WIN.get_width() / 10)
        self.h: int = h
        self.amount_of_images: int = amount_of_images
        self.vel: int = vel
        self.grass_block: pygame.surface.Surface = pygame.transform.scale(pygame.image.load("""assets/images/Tiles/grassMid.png"""),    (self.w, self.w))
        self.dirt_block: pygame.surface.Surface =  pygame.transform.scale(pygame.image.load("""assets/images/Tiles/grassCenter.png"""), (self.w, self.w))
        self.image: pygame.surface.Surface = self._setup_image()
        self.images: list = self._generate_images()

    def _setup_image(self) -> pygame.surface.Surface:
        image = pygame.surface.Surface([self.WIN.get_width(), (int(self.h / self.w) + 1 if "." in str(self.h / self.w) else int(self.h / self.w))*self.w])
        x, y = self.w, self.w
        x_needed = int(self.WIN.get_width() / self.w)
        y_needed = int(self.h / self.w) + 1 if "." in str(self.h / self.w) else int(self.h / self.w)
        for j in range(y_needed):
            for i in range(x_needed):
                image.blit(self.grass_block if j == 0 else self.dirt_block, (x*i, y*j))

        return image

    def _generate_images(self) -> list:
        images = []
        x = 0
        for i in range(self.amount_of_images):
            images.append([])
            images[i].append(self.image)
            images[i].append([x, self.y])
            x += self.WIN.get_width()

        return images

    def move(self):
        """
        it moves the ground
        :return: None
        """
        for i, info in enumerate(self.images):
            image, cords = info
            self.images[i][1][0] -= self.vel
            x, y = cords

            if x <= -self.WIN.get_width():
                self.images[i][1][0] = self.WIN.get_width()*(self.amount_of_images - 1)

    def draw(self) -> None:
        """
        it draws the ground
        :return: None
        """
        for image, cords in self.images:
            self.WIN.blit(image, cords)
