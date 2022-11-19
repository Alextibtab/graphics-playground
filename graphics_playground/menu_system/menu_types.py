from typing import List

import pygame

from .menu import Menu


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
                self.game.playing = True
            if self.menu_options[1]["state"]:
                self.game.current_menu = OptionMenu(
                    self.game, ["Option 1", "Option 2", "Option 3", "Back"]
                )
            if self.menu_options[2]["state"]:
                pygame.quit()
            self.show_menu = False


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
