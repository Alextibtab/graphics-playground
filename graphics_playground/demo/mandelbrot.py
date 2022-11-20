import math
from typing import Tuple

import pygame


class Mandelbrot:
    Color = Tuple[int, int, int]

    def __init__(self, game):
        self.game = game
        self.iterations = 1
        self.exponent = 2
        self.__iter_or_expo = True
        self.surface = pygame.Surface(
            (game.get_screen_width(), game.get_screen_height())
        )
        self.generate_mandelbrot()

    def generate_mandelbrot(self):
        self.pixelArray = pygame.PixelArray(self.surface)
        max_x = self.pixelArray.shape[0]
        max_y = self.pixelArray.shape[1]
        for x in range(0, max_x):
            for y in range(0, max_y):
                a = self.normalize_value(x, 0, max_x, -2, 2)
                b = self.normalize_value(y, 0, max_y, -2, 2)

                start_a = a
                start_b = b

                n = 0

                while n < self.iterations:
                    next_a = math.pow(abs(a), self.exponent) - math.pow(
                        abs(b), self.exponent
                    )
                    next_b = 2 * a * b
                    a = next_a + start_a
                    b = next_b + start_b
                    if abs(a + b) > 16:
                        break

                    n += 1

                brightness = round(self.normalize_value(n, 0, self.iterations, 0, 255))
                if n == self.iterations:
                    brightness = 0
                self.pixelArray[x, y] = (brightness, brightness, brightness)
        self.pixelArray.close()

    def generate_julia_set(self, cx: int, cy: int):
        self.pixelArray = pygame.PixelArray(self.surface)
        max_x = self.pixelArray.shape[0]
        max_y = self.pixelArray.shape[1]
        cx = self.normalize_value(cx, 0, max_x, -2, 2)
        cy = self.normalize_value(cy, 0, max_y, -2, 2)
        for x in range(0, max_x):
            for y in range(0, max_y):
                a = self.normalize_value(x, 0, max_x, -2, 2)
                b = self.normalize_value(y, 0, max_y, -2, 2)

                n = 0
                while n < self.iterations:
                    next_a = math.pow(abs(a), self.exponent) - math.pow(
                        abs(b), self.exponent
                    )
                    b = 2 * a * b + cy
                    a = next_a + cx
                    if abs(a + b) > 16:
                        break

                    n += 1

                brightness = round(self.normalize_value(n, 0, self.iterations, 0, 255))
                if n == self.iterations:
                    brightness = 0
                self.pixelArray[x, y] = (brightness, brightness, brightness)
        self.pixelArray.close()

    def normalize_value(self, value, old_min, old_max, new_min, new_max):
        old_range = old_max - old_min
        new_range = new_max - new_min
        return (((value - old_min) * new_range) / old_range) + new_min

    def draw(self):
        self.show_demo = True
        while self.show_demo:
            self.game.check_events()
            self.check_input()
            self.draw_text(
                f"Iterations: {self.iterations}",
                18,
                (255, 255, 255),
                70,
                10,
            )
            self.draw_text(
                f"Exponent: {round(self.exponent, 2)}", 18, (255, 255, 255), 70, 25
            )
            self.draw_text(
                "+ increase iteration",
                14,
                (255, 255, 255),
                70,
                40,
            )
            self.draw_text(
                "- decrease iteration",
                14,
                (255, 255, 255),
                70,
                55,
            )
            self.blit_screen()

    def blit_screen(self):
        self.game.window.blit(self.surface, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def draw_text(self, text: str, size: int, color: Color, x: int, y: int):
        font = pygame.font.Font(self.game.font_name, size)
        text_surface = font.render(text, True, color, self.game.BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.surface.blit(text_surface, text_rect)

    def check_input(self):
        if self.game.PLUS_KEY:
            if self.__iter_or_expo:
                self.iterations += 1
            else:
                self.exponent += 0.1
        if self.game.MINUS_KEY:
            if self.__iter_or_expo:
                if self.iterations - 1 > 0:
                    self.iterations -= 1
            else:
                self.exponent -= 0.1
        if self.game.I_KEY:
            self.__iter_or_expo = not self.__iter_or_expo
        if self.game.START_KEY:
            self.generate_mandelbrot()
        if self.game.LEFT_CLICK:
            pos = pygame.mouse.get_pos()
            self.generate_julia_set(pos[0], pos[1])
        if self.game.ESC_KEY:
            self.show_demo = False
            self.game.playing = False
