import math

import pygame


class Attractor:
    def __init__(self, game):
        self.game = game
        self.show_demo = True
        self.center_x = self.game.get_screen_width() / 2
        self.center_y = self.game.get_screen_height() / 2
        self.iterations = 25000
        self.coords = [(0, 0)] * self.iterations
        self.attractor = Clifford()
        self.generate_points()

    def draw(self):
        self.show_demo = True
        while self.show_demo:
            self.attractor.a += 0.001
            self.game.check_events()
            self.generate_points()
            self.draw_points()
            self.blit_screen()

    def generate_points(self):
        for iteration in range(1, self.iterations):
            self.coords[iteration] = self.attractor.equation(
                self.coords[iteration - 1][0], self.coords[iteration - 1][1]
            )

    def draw_points(self):
        self.game.canvas.fill(self.game.BLACK)
        for iteration in range(1, self.iterations):
            point = (
                self.center_x + self.coords[iteration][0] * self.attractor.scaleX,
                self.center_y + self.coords[iteration][1] * self.attractor.scaleY,
            )
            pygame.draw.circle(self.game.canvas, self.game.WHITE, point, 1)

    def blit_screen(self):
        self.game.window.blit(self.game.canvas, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class Clifford:
    def __init__(self):
        self.a = -1.3
        self.b = -1.3
        self.c = -1.8
        self.d = -1.9

        self.scaleX = 70
        self.scaleY = 70

    def equation(self, x, y):
        return math.sin(self.a * y) + self.c * math.cos(self.a * x), math.sin(
            self.b * x
        ) + self.d * math.cos(self.b * y)


class Svensson:
    def __init__(self):
        self.a = 1.4
        self.b = 1.56
        self.c = 1.4
        self.d = -6.56

        self.scaleX = 40
        self.scaleY = 70

    def equation(self, x, y):
        return self.d * math.sin(self.a * x) - math.sin(self.b * y), self.c * math.cos(
            self.a * x
        ) + math.cos(self.b * y)
