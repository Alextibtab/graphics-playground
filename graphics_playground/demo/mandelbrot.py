import pygame


class Mandelbrot:
    def __init__(self, game):
        self.game = game
        self.iterations = 100
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
                a = self.normalize_value(x, 0, max_x, -2, 1)
                b = self.normalize_value(y, 0, max_y, -1, 1)

                start_a = a
                start_b = b

                n = 0

                while n < self.iterations:
                    next_a = a * a - b * b
                    next_b = 2 * a * b
                    a = next_a + start_a
                    b = next_b + start_b
                    if abs(a + b) > 16:
                        break

                    n += 1

                brightness = round(self.normalize_value(n, 0, self.iterations, 0, 255))
                if n == 100:
                    brightness = 0
                self.pixelArray[x, y] = (brightness, brightness, brightness)
        self.pixelArray.close()

    def normalize_value(self, value, old_min, old_max, new_min, new_max):
        old_range = old_max - old_min
        new_range = new_max - new_min
        return (((value - old_min) * new_range) / old_range) + new_min

    def draw(self):
        self.blit_screen()

    def blit_screen(self):
        self.game.window.blit(self.surface, (0, 0))
        pygame.display.update()
        self.game.reset_keys()
