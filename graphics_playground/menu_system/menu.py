import pygame


class Menu:
    def __init__(self, game):
        self.game = game
        self.__cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.center_x = self.game.get_screen_width() / 2
        self.center_y = self.game.get_screen_height() / 2
        self.display_menu = True

    def draw_cursor(self):
        self.game.draw_text(
            "*", 15, self.game.BLACK, self.__cursor_rect.x, self.__cursor_rect.y
        )

    def blit_screen(self):
        self.game.window.blit(self.game.canvas, (0, 0))
        pygame.display.update()
        self.game.reset_keys()
