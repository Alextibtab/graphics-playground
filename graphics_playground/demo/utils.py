import pygame


class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


class Line:
    def __init__(self, start_point, end_point):
        self.__start = start_point
        self.__end = end_point

    def draw(self, surface, fill_color):
        pygame.draw.line(
            surface,
            fill_color,
            (self.__start.get_x(), self.__start.get_y()),
            (self.__end.get_x(), self.__end.get_y()),
            width=2,
        )


class Cell:
    def __init__(self, walls, x1, x2, y1, y2, win, wall_color, bg_color):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        self.__center = Point((x1 + x2) / 2, (y1 + y2) / 2)

        self.__wall_color = wall_color
        self.__bg_color = bg_color
        self.__win = win

        self.__visited = False

        self.__walls = {
            "top": {
                "visible": walls[0],
                "line": Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)),
            },
            "right": {
                "visible": walls[1],
                "line": Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)),
            },
            "bottom": {
                "visible": walls[2],
                "line": Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)),
            },
            "left": {
                "visible": walls[3],
                "line": Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)),
            },
        }

    def is_visited(self):
        return self.__visited

    def visit(self):
        self.__visited = True

    def unvisit(self):
        self.__visited = False

    def break_top(self):
        self.__walls["top"]["visible"] = False

    def break_right(self):
        self.__walls["right"]["visible"] = False

    def break_bottom(self):
        self.__walls["bottom"]["visible"] = False

    def break_left(self):
        self.__walls["left"]["visible"] = False

    def has_top_wall(self):
        return self.__walls["top"]["visible"]

    def has_right_wall(self):
        return self.__walls["right"]["visible"]

    def has_bottom_wall(self):
        return self.__walls["bottom"]["visible"]

    def has_left_wall(self):
        return self.__walls["left"]["visible"]

    def update_wall_visibility(self, walls):
        self.__walls["top"]["visible"] = walls[0]
        self.__walls["right"]["visible"] = walls[1]
        self.__walls["bottom"]["visible"] = walls[2]
        self.__walls["left"]["visible"] = walls[3]

    def draw(self, surface):
        if self.__walls["top"]["visible"]:
            self.__walls["top"]["line"].draw(surface, self.__wall_color)
        else:
            self.__walls["top"]["line"].draw(surface, self.__bg_color)

        if self.__walls["right"]["visible"]:
            self.__walls["right"]["line"].draw(surface, self.__wall_color)
        else:
            self.__walls["right"]["line"].draw(surface, self.__bg_color)

        if self.__walls["bottom"]["visible"]:
            self.__walls["bottom"]["line"].draw(surface, self.__wall_color)
        else:
            self.__walls["bottom"]["line"].draw(surface, self.__bg_color)

        if self.__walls["left"]["visible"]:
            self.__walls["left"]["line"].draw(surface, self.__wall_color)
        else:
            self.__walls["left"]["line"].draw(surface, self.__bg_color)

    def draw_move(self, to_cell, surface, undo=False):
        color = (150, 150, 150) if undo else (0, 200, 0)
        Line(self.__center, to_cell.__center).draw(surface, color)
