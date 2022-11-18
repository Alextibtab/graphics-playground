from .menu import Menu
from ..game import Game


class MainMenu(Menu):
    def __init__(self, game: "Game"):
        super().__init__(game)
        self.state = "Start!"
