import pygame


class Menu:
    def __init__(self, game):
        self.game = game
        self.cursor_rect = pygame.Rect(0, 0, 18, 18)
        self.center_x = self.game.get_screen_width() / 2
        self.center_y = self.game.get_screen_height() / 2
        self.show_menu = True
        self.offset = -60

    def draw_cursor(self):
        self.game.draw_text(
            ">",
            18,
            self.game.WHITE,
            self.cursor_rect.x + self.offset,
            self.cursor_rect.y,
        )

    def draw_menu(self):
        self.show_menu = True
        while self.show_menu:
            self.game.check_events()
            self.check_input()
            self.game.canvas.fill(self.game.BLACK)
            for option in self.menu_options:
                self.game.draw_text(
                    option["value"],
                    18,
                    self.game.WHITE,
                    self.center_x,
                    option["offset"],
                )
            self.draw_cursor()
            self.blit_screen()
            self.game.reset_keys()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            for index, option in enumerate(self.menu_options):
                if option["state"]:
                    next_index = (index + 1) % self.option_length
                    self.cursor_rect.midtop = (
                        self.center_x,
                        self.menu_options[next_index]["offset"],
                    )
                    option["state"] = False
                    self.menu_options[next_index]["state"] = True
                    break

        if self.game.UP_KEY:
            for index, option in enumerate(self.menu_options):
                if option["state"]:
                    next_index = (index - 1) % self.option_length
                    self.cursor_rect.midtop = (
                        self.center_x,
                        self.menu_options[next_index]["offset"],
                    )
                    option["state"] = False
                    self.menu_options[next_index]["state"] = True
                    break

    def _set_offsets(self):
        for offset, option in enumerate(self.menu_options):
            option["offset"] = self.center_y + ((offset + 2) * 20)

    def blit_screen(self):
        self.game.window.blit(self.game.canvas, (0, 0))
        pygame.display.update()
        self.game.reset_keys()
