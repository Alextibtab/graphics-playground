import time
import random

import pygame

from .utils import Cell


class Maze:
    def __init__(
        self, game, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None
    ):
        self.game = game
        self.__x1 = int(x1)
        self.__y1 = int(y1)
        self.__num_rows = int(num_rows)
        self.__num_cols = int(num_cols)
        self.__cell_size_x = int(cell_size_x)
        self.__cell_size_y = int(cell_size_y)
        self.__win = win

        if seed:
            self.__seed = random.seed(seed)

    def _create_cells(self):
        self.__cells = [
            [
                Cell(
                    [True] * 4,
                    column_offset,
                    column_offset + self.__cell_size_x,
                    row_offset,
                    row_offset + self.__cell_size_y,
                    self.__win,
                    (255, 255, 255),
                    (0, 0, 0),
                )
                for row_offset in range(
                    self.__x1,
                    self.__x1 + self.__num_rows * self.__cell_size_y,
                    self.__cell_size_y,
                )
            ]
            for column_offset in range(
                self.__y1,
                self.__y1 + self.__num_cols * self.__cell_size_x,
                self.__cell_size_x,
            )
        ]
        for column in self.__cells:
            for cell in column:
                cell.draw(self.game.canvas)
                self._animate(0.001)

    def _break_entrance_and_exit(self):
        self.__cells[0][0].update_wall_visibility([False, True, True, True])
        self.__cells[0][0].draw(self.game.canvas)
        self._animate(0.5)

        self.__cells[-1][-1].update_wall_visibility([True, True, False, True])
        self.__cells[-1][-1].draw(self.game.canvas)
        self._animate(0.5)

    def _break_walls_r(self, column, row):
        self.__cells[column][row].visit()
        while True:
            to_visit = [None] * 4

            # Check top cell
            if row > 0 and not self.__cells[column][row - 1].is_visited():
                to_visit[0] = [column, row - 1]

            # Check right cell
            if (
                column < self.__num_cols - 1
                and not self.__cells[column + 1][row].is_visited()
            ):
                to_visit[1] = [column + 1, row]

            # Check bottom cell
            if (
                row < self.__num_rows - 1
                and not self.__cells[column][row + 1].is_visited()
            ):
                to_visit[2] = [column, row + 1]

            # Check left cell
            if column > 0 and not self.__cells[column - 1][row].is_visited():
                to_visit[3] = [column - 1, row]

            valid_directions = [i for i, v in enumerate(to_visit) if v is not None]
            if len(valid_directions) == 0:
                self.__cells[column][row].draw(self.game.canvas)
                return

            direction = random.choice(valid_directions)
            self._break_walls(column, row, direction)
            self._break_walls_r(to_visit[direction][0], to_visit[direction][1])

    def _break_walls(self, column, row, direction):
        # Top direction
        if direction == 0:
            self.__cells[column][row].break_top()
            self.__cells[column][row - 1].break_bottom()
            self.__cells[column][row - 1].draw(self.game.canvas)

        # Right direction
        if direction == 1:
            self.__cells[column][row].break_right()
            self.__cells[column + 1][row].break_left()
            self.__cells[column + 1][row].draw(self.game.canvas)

        # Bottom direction
        if direction == 2:
            self.__cells[column][row].break_bottom()
            self.__cells[column][row + 1].break_top()
            self.__cells[column][row + 1].draw(self.game.canvas)

        # Left direction
        if direction == 3:
            self.__cells[column][row].break_left()
            self.__cells[column - 1][row].break_right()
            self.__cells[column - 1][row].draw(self.game.canvas)

        self.__cells[column][row].draw(self.game.canvas)
        self._animate(0.001)

    def _reset_cells_visited(self):
        for column in self.__cells:
            for cell in column:
                cell.unvisit()

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, column, row):
        self._animate(0.05)
        self.__cells[column][row].visit()
        if column == self.__num_cols - 1 and row == self.__num_rows - 1:
            return True

        # Check top cell
        if (
            row > 0
            and not self.__cells[column][row - 1].is_visited()
            and not self.__cells[column][row].has_top_wall()
        ):
            self.__cells[column][row].draw_move(
                self.__cells[column][row - 1], self.game.canvas
            )
            if self._solve_r(column, row - 1):
                return True
            else:
                self.__cells[column][row].draw_move(
                    self.__cells[column][row - 1], self.game.canvas, True
                )

        # Check right cell
        if (
            column < self.__num_cols - 1
            and not self.__cells[column + 1][row].is_visited()
            and not self.__cells[column][row].has_right_wall()
        ):
            self.__cells[column][row].draw_move(
                self.__cells[column + 1][row], self.game.canvas
            )
            if self._solve_r(column + 1, row):
                return True
            else:
                self.__cells[column][row].draw_move(
                    self.__cells[column + 1][row], self.game.canvas, True
                )

        # Check bottom cell
        if (
            row < self.__num_rows - 1
            and not self.__cells[column][row + 1].is_visited()
            and not self.__cells[column][row].has_bottom_wall()
        ):
            self.__cells[column][row].draw_move(
                self.__cells[column][row + 1], self.game.canvas
            )

            if self._solve_r(column, row + 1):
                return True
            else:
                self.__cells[column][row].draw_move(
                    self.__cells[column][row + 1], self.game.canvas, True
                )

        # Check left cell
        if (
            column > 0
            and not self.__cells[column - 1][row].is_visited()
            and not self.__cells[column][row].has_left_wall()
        ):
            self.__cells[column][row].draw_move(
                self.__cells[column - 1][row], self.game.canvas
            )

            if self._solve_r(column - 1, row):
                return True
            else:
                self.__cells[column][row].draw_move(
                    self.__cells[column - 1][row], self.game.canvas, True
                )

        return False

    def draw(self):
        self.show_demo = True
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self.solve()
        while self.show_demo:
            self.game.check_events()
            self.check_input()
            self.blit_screen()

    def _animate(self, duration):
        self.blit_screen()
        time.sleep(duration)

    def blit_screen(self):
        self.game.window.blit(self.game.canvas, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def check_input(self):
        if self.game.ESC_KEY:
            self.show_demo = False
            self.game.playing = False
