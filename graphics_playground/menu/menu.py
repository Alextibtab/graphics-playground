import pygame

from ..game import Game


class Menu:
    def __init__(self, game: "Game"):
        self.__game = game
        self.__cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.center_x = self.__game.__DISPLAY_W / 2
        self.center_y = self.__game.__DISPLAY_H / 2
        self.display_menu = True
        self.option_offset = -100

    def draw_cursor(self):
        self.__game.draw_text(
            "*", 15, self.__cursor_rect.x, (0, 0, 0), self.__cursor_rect.y
        )

    def blit_screen(self):
        self.__game.window.blit(self.__game.canvas, (0, 0))
        pygame.display.update()
        self.__game.reset_keys()
