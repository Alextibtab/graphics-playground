from typing import List

import pygame

from .menu import Menu
from ..demo.mandelbrot import Mandelbrot
from ..demo.attractor import Attractor
from ..demo.maze import Maze


class MainMenu(Menu):
    def __init__(self, game, options: List[str]):
        super().__init__(game)
        self.menu_options = [{"value": value, "state": False} for value in options]
        self.menu_options[0]["state"] = True
        self._set_offsets()
        self.option_length = len(self.menu_options)
        self.cursor_rect.midtop = (
            self.center_x,
            self.menu_options[0]["offset"] - 2,
        )

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.menu_options[0]["state"]:
                self.game.current_menu = DemoMenu(
                    self.game, ["Maze Demo", "Mandelbrot Demo", "Strange Attractors"]
                )
            if self.menu_options[1]["state"]:
                self.game.current_menu = OptionMenu(
                    self.game, ["Option 1", "Option 2", "Option 3", "Back"]
                )
            if self.menu_options[2]["state"]:
                pygame.quit()
            self.show_menu = False
        if self.game.ESC_KEY:
            self.show_menu = False
            pygame.quit()


class OptionMenu(Menu):
    def __init__(self, game, options: List[str]):
        super().__init__(game)
        self.menu_options = [{"value": value, "state": False} for value in options]
        self.menu_options[0]["state"] = True
        self._set_offsets()
        self.option_length = len(self.menu_options)
        self.cursor_rect.midtop = (
            self.center_x,
            self.menu_options[0]["offset"] - 2,
        )

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.menu_options[3]["state"]:
                self.game.current_menu = MainMenu(
                    self.game, ["Select Demo", "Options", "Exit"]
                )
            if self.menu_options[1]["state"]:
                pass
            if self.menu_options[2]["state"]:
                pygame.quit()
            self.show_menu = False
        if self.game.ESC_KEY:
            self.game.current_menu = MainMenu(
                self.game, ["Select Demo", "Options", "Exit"]
            )
            self.show_menu = False


class DemoMenu(Menu):
    def __init__(self, game, options: List[str]):
        super().__init__(game)
        self.menu_options = [{"value": value, "state": False} for value in options]
        self.menu_options[0]["state"] = True
        self._set_offsets()
        self.option_length = len(self.menu_options)
        self.offset -= 25
        self.cursor_rect.midtop = (
            self.center_x,
            self.menu_options[0]["offset"] - 2,
        )

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.menu_options[0]["state"]:
                self.game.demo = Maze(
                    self.game,
                    self.center_x - 300,
                    self.center_y,
                    25,
                    25,
                    10,
                    10,
                    False,
                    1,
                )
                self.game.playing = True
            if self.menu_options[1]["state"]:
                self.game.demo = Mandelbrot(self.game)
                self.game.playing = True
            if self.menu_options[2]["state"]:
                self.game.demo = Attractor(self.game)
                self.game.playing = True
            self.show_menu = False
        if self.game.ESC_KEY:
            self.game.current_menu = MainMenu(
                self.game, ["Select Demo", "Options", "Exit"]
            )
            self.show_menu = False
