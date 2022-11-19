from typing import List

from .menu import Menu


class MainMenu(Menu):
    def __init__(self, game, options: List[str]):
        super().__init__(game)
        self.state = "Start!"
        self.__start_x = self.center_x
        self.__start_y = self.center_y
        self.__menu_options = [{"value": value} for value in options]
        self._set_offsets()

    def _set_offsets(self):
        for offset, option in enumerate(self.__menu_options):
            option["offset"] = self.__start_y + ((offset + 2) * 20)

    def draw_menu(self):
        self.show_menu = True
        while self.show_menu:
            self.game.check_events()
            self.game.canvas.fill(self.game.WHITE)
            for option in self.__menu_options:
                self.game.draw_text(
                    option["value"],
                    18,
                    self.game.BLACK,
                    self.__start_x,
                    option["offset"],
                )
            self.draw_cursor()
            self.blit_screen()
