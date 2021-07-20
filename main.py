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


from Classes import *


import pygame
import random


pygame.init()
pygame.font.init()


class Game:
    def __init__(self):

        self.WIDTH, self.HEIGHT = 800, 400
        self.WIN: pygame.surface.Surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.player: Player = Player(self.WIN, 50, 275)
        self.ground: Ground = Ground(self.WIN, 311, self.HEIGHT - 311, vel=8)
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.enemies: list = [Blocker(self.WIN, 311, vel=8)]
        self.SM = SoundManager
        self.score = 0
        self.font = pygame.font.SysFont("comicsans", 30)
        self.bg = pygame.transform.scale(pygame.image.load("assets/images/bg.png"), (self.WIDTH, self.HEIGHT))
        self.clouds: list = [
            [
                pygame.image.load(f"""assets/images/items/cloud{random.randint(1, 3)}.png"""),
                [random.randrange(800, 1200), random.randrange(0, 250)]
            ] for _ in range(random.randint(5, 10))
        ]
        self.clouds_vel = 1

    def move_clouds(self):
        for i in range(len(self.clouds)):
            self.clouds[i][1][0] -= self.clouds_vel

            if self.clouds[i][1][0] <= -150:
                print(True)
                self.clouds[i][1][0] = random.randrange(800, 1200)

    def draw(self):
        """
        it draws things in the screen
        :return: None
        """
        # it fills the screen to a base color
        self.WIN.fill((64, 64, 64))

        # draw the bg
        self.WIN.blit(
            self.bg, (0, 0)
        )

        # draw clouds
        self.move_clouds()
        for image, cords in self.clouds:
            self.WIN.blit(
                image, cords
            )

        # draw the score
        self.WIN.blit(
            self.font.render(f"""score: {self.score}""", True, BLACK), (5, 5)
        )

        # draw FPS
        self.WIN.blit(
            self.font.render(str(round(self.clock.get_fps())), True, BLACK), (self.WIDTH - 30, 5)
        )

        # enemies
        for enemy in self.enemies:
            if isinstance(enemy, Blocker):
                pass
            if self.player.collision(enemy):
                self.lost()
            enemy.draw()
            try:
                enemy.animate()
            except AttributeError:
                pass
            except Exception as e:
                print(f"""[EXCEPTION] {e} | {type(e)}""")
            if enemy.move():
                self.score += 1
                self.enemies.pop(self.enemies.index(enemy))
                self.enemies.append(
                    random.choice(
                        [
                            Slime(self.WIN, 311, vel=8),
                            Blocker(self.WIN, 311, vel=8),
                            Poker(self.WIN, 311, vel=8)
                        ]
                    )
                )

        # player
        self.player.animate()
        self.player.draw()
        self.player.move()

        # ground
        self.ground.draw()
        self.ground.move()

        # update the screen
        pygame.display.update()

    def event_handler(self):
        """
        it handles all of the events
        :return: None
        """
        for event in pygame.event.get():
            self.player.event_handler(event)
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit(-1)

    def lost(self):
        # it fills the screen to a base color
        self.WIN.fill((64, 64, 64))

        # draw the bg
        self.WIN.blit(
            self.bg, (0, 0)
        )

        # draw clouds
        self.move_clouds()
        for image, cords in self.clouds:
            self.WIN.blit(
                image, cords
            )

        # draw FPS
        self.WIN.blit(
            self.font.render(str(round(self.clock.get_fps())), True, BLACK), (self.WIDTH - 40, 5)
        )

        # draw the score
        self.WIN.blit(
            self.font.render(f"""score: {self.score}""", True, BLACK), (5, 5)
        )

        # enemies
        for enemy in self.enemies:
            enemy.draw()

        # player
        self.player.animate()
        self.player.draw()
        self.player.move()

        # ground
        self.ground.draw()
        self.ground.move()

        # update the screen
        pygame.display.update()

        while True:
            self.clock.tick(60)

            for event in pygame.event.get():
                self.player.event_handler(event)
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit(-1)

    def run(self):
        while 1:
            self.clock.tick(60)
            self.draw()
            self.event_handler()


game = Game()
game.run()
