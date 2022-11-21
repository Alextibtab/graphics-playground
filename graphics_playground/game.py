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
        self.demo = None
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.ESC_KEY = False
        self.PLUS_KEY = False
        self.MINUS_KEY = False
        self.I_KEY = False
        self.LEFT_CLICK = False
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
            self.canvas.fill(self.BLACK)
            self.check_events()
            if self.ESC_KEY:
                self.playing = False
            self.demo.draw()

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
                self.demo.show_demo = False
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
                if event.key == pygame.K_EQUALS:
                    self.PLUS_KEY = True
                if event.key == pygame.K_MINUS:
                    self.MINUS_KEY = True
                if event.key == pygame.K_i:
                    self.I_KEY = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    self.LEFT_CLICK = True

    def reset_keys(self):
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.ESC_KEY = False
        self.PLUS_KEY = False
        self.MINUS_KEY = False
        self.I_KEY = False
        self.LEFT_CLICK = False
