from graphics_playground.game import Game

if __name__ == "__main__":
    game = Game("Boot.dev Project", 720, 480)

    while game.running:
        # game.playing = True
        game.draw_menu()
        game.game_loop()
