from typing import Tuple
import pygame

from .menu_system.menu_types import MainMenu


class Game:
    Color = Tuple[int, int, int]

    def __init__(self, title: str, width: int, height: int):
        pygame.init()
        pygame.font.init()
        self.running = True
        self.playing = False
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.ESC_KEY = False
        self.__DISPLAY_W = width
        self.__DISPLAY_H = height
        self.canvas = pygame.Surface((self.__DISPLAY_W, self.__DISPLAY_H))
        self.window = pygame.display.set_mode(((self.__DISPLAY_W, self.__DISPLAY_H)))
        pygame.display.set_caption(title)
        self.font_name = pygame.font.get_default_font()

        self.current_menu = MainMenu(self, ["Select Demo", "Options", "Exit"])

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

    def get_screen_width(self):
        return self.__DISPLAY_W

    def get_screen_height(self):
        return self.__DISPLAY_H

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.canvas.fill(self.WHITE)
            self.draw_text(
                "Personal Project Numero Uno",
                18,
                self.BLACK,
                self.__DISPLAY_W / 2,
                self.__DISPLAY_H / 2,
            )
            self.window.blit(self.canvas, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def draw_text(self, text: str, size: int, color: Color, x: int, y: int):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.canvas.blit(text_surface, text_rect)

    def draw_menu(self):
        self.current_menu.draw_menu()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                self.current_menu.show_menu = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.ESC_KEY = True

    def reset_keys(self):
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.ESC_KEY = False
