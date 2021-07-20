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


class SoundManager:
    def __init__(self):
        try:
            self._Ending = pygame.mixer.Sound("assets/music/background/Ending.wav"); self._Ending.set_volume(0.5)
            self._Level_1 = pygame.mixer.Sound("assets/music/background/Level 1.wav"); self._Level_1.set_volume(0.5)
            self._Level_2 = pygame.mixer.Sound("assets/music/background/Level 2.wav"); self._Level_2.set_volume(0.5)
            self._Level_3 = pygame.mixer.Sound("assets/music/background/Level 3.wav"); self._Level_3.set_volume(0.5)
            self._Title_Screen = pygame.mixer.Sound("assets/music/background/Title Screen.wav"); self._Title_Screen.set_volume(0.5)
            self._hit = pygame.mixer.Sound("assets/music/sfx/hit.wav"); self._hit.set_volume(0.5)
            self._pickup_coin = pygame.mixer.Sound("assets/music/sfx/Pickup_Coin.wav"); self._pickup_coin.set_volume(0.5)
            self._powerup = pygame.mixer.Sound("assets/music/sfx/.wav"); self._powerup.set_volume(0.5)
        except pygame.error:
            pass

    def ending(self):
        try:
            self._Ending.play()
        except Exception as e:
            print(e)

    def level_1(self):
        try:
            self._Level_1.play()
        except Exception as e:
            print(e)

    def level_2(self):
        try:
            self._Level_2.play()
        except Exception as e:
            print(e)

    def level_3(self):
        try:
            self._Level_3.play()
        except Exception as e:
            print(e)

    def title_screen(self):
        try:
            self._Title_Screen.play()
        except Exception as e:
            print(e)

    def hit(self):
        try:
            self._hit.play()
        except Exception as e:
            print(e)

    def pickup_coin(self):
        try:
            self._pickup_coin.play()
        except Exception as e:
            print(e)

    def powerup(self):
        try:
            self._powerup.play()
        except Exception as e:
            print(e)
