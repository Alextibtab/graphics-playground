from graphics_playground.game import Game

if __name__ == "__main__":
    game = Game("Boot.dev Project")

    while game.running:
        game.playing = True
        game.game_loop()
